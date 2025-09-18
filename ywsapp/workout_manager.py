#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  workout_manager.py
#  
#  Copyright 2025 Repnikov Dmitry <acid454@yoga7>
#  

import logging
import hashlib
import json
from uuid import UUID
from .yoga.common.base import BaseWorkout
from .models import User, UserWorkout
from .resmanager import ResourcesManager
logger = logging.getLogger("ywsapp")


class WorkoutManager:
    #
    # Singleton class for workout manager
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(WorkoutManager, cls).__new__(cls)
            cls.instance.user_workouts = {}
        return cls.instance
    
    def init_user_default_workouts(func):
        def _load_default_workouts(self, *args, **kwargs):
            user_id = args[0]
            if user_id not in self.user_workouts.keys():
                logger.info(f"New user {user_id} accessed. Workout files:\n" + "\n".join(ResourcesManager().workout_files()))
                
                
                # Load workouts from database first
                try:
                    _user = User.objects.get(id=user_id)
                    recs = UserWorkout.objects.filter(user = _user)
                except:
                    _user = None
                    recs = []
                
                self.user_workouts[user_id] = {}
                for user_workout in recs:
                    try:
                        logger.debug(f"USER WORKOUT {user_workout.caption}: {user_workout.items}")
                        workout = BaseWorkout.from_items(json.loads(user_workout.items))
                        workout.id = user_workout.workout_id
                        workout.caption = user_workout.caption
                        workout.group = user_workout.group
                        self.user_workouts[user_id][workout.id] = workout
                    except:
                        logger.exception(f"exception while loading user workout form DB, skip")
                
                # Second, load deafult workout templates, but watch for same id (if workout was saved)
                for f in sorted(ResourcesManager().workout_files()):
                    try:
                        workouts = __import__(f[:-3]).do_load_workouts()
                        for w in workouts:
                            wid = UUID(hashlib.md5((f + ':' + w.__name__).encode()).hexdigest())
                            if wid in self.user_workouts[user_id].keys():
                                w = self.user_workouts[user_id][wid]
                                del self.user_workouts[user_id][wid]
                                self.user_workouts[user_id][wid] = w
                                continue
                            self.user_workouts[user_id][wid] = w(id = wid) ##.build(_user, wid)   -- do not build workout here cause save in DB
                            #self.user_workouts[user_id][wid] = {
                            #    'class':w,
                            #    'default':w().build(None, wid),
                            #    'filenm':f,
                            #    'wid':wid
                            #}
                    except:
                        logger.exception(f"exception while loading workout form template {f}")

            return func(self, *args, **kwargs)
        return _load_default_workouts
    
    @init_user_default_workouts
    def list_workouts(self, user_id):
        return self.user_workouts[user_id].values()

    @init_user_default_workouts
    def load_workout(self, user_id, wid : str):
        return self.user_workouts[user_id].get(UUID(wid), None)
    

    def save_workout(self, user_id : str, workout_id : str):
        logger.debug(f"Workout {workout_id}, user {user_id}, keys: {self.user_workouts[user_id].keys()}")
        _user = User.objects.get(id=user_id)
        if not workout_id in self.user_workouts[user_id].keys():
            return False
        
        # ToDo: optimize
        try:
            UserWorkout.objects.get(user = _user, workout_id = workout_id).delete()
        except:
            pass
        
        db_workout = UserWorkout(user = _user, workout_id = workout_id)
        db_workout.caption = self.user_workouts[user_id].get(workout_id).caption
        db_workout.group = self.user_workouts[user_id].get(workout_id).group
        db_workout.items = json.dumps(self.user_workouts[user_id].get(workout_id).items())
        db_workout.save()
        logger.debug(f"Workout {workout_id} saved")
        return True


    @init_user_default_workouts
    def edit_property(self, user_id, property_id : str, value : str):
        logger.debug(f"Edit property {property_id} for user {user_id}, value {value}")

        for workout_id in self.user_workouts[user_id].keys():
            prop = self.user_workouts[user_id][workout_id].find_property_by_id(property_id)
            logger.debug(f"Edit property {property_id}, return {prop}")
            if prop is not None:
                try:
                    v = int(value)
                    if (v < prop.value_min) or (v > prop.value_max):
                        raise ValueError()
                except:
                    raise ValueError()

                prop.value = v
                logger.debug(f"Property {prop} {property_id} modified")
                return self.save_workout(user_id, workout_id)
        return False
