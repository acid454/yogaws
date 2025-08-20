#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  workout_manager.py
#  
#  Copyright 2025 Repnikov Dmitry <acid454@yoga7>
#  

import logging
import hashlib
from .models import User, UserWorkoutProps
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
            try:
                recs = UserWorkoutProps.objects.filter(user = User.objects.get(id=user_id))
            except:
                recs = []
            
            if user_id not in self.user_workouts.keys():
                logger.info(f"New user {user_id} accessed. Workout files:")
                logger.info("\n".join(ResourcesManager().workout_files()))
                
                self.user_workouts[user_id] = {}
                for f in ResourcesManager().workout_files():
                    try:
                        workouts = __import__(f[:-3]).do_load_workouts()
                        for w in workouts:
                            wid = hashlib.md5((f + ':' + w.__name__).encode()).hexdigest()
                            self.user_workouts[user_id][wid] = {
                                'class':w,
                                'default':w().build(None, wid),
                                'filenm':f,
                                'wid':wid
                            }
                        
                        # Apply settings on default workout, if we can
                        for r in recs:
                            self.user_workouts[user_id][wid]['default'].apply_prop(r.prop_id, r.value)
                    except:
                        logger.exception(f"exception while loading workout {f}")
                        continue

            return func(self, *args, **kwargs)
        return _load_default_workouts
    
    @init_user_default_workouts
    def list_workouts(self, user_id):
        return self.user_workouts[user_id].values()

    @init_user_default_workouts
    def load_workout(self, user_id, wid : str):
        return self.user_workouts[user_id].get(wid, None)

    @init_user_default_workouts
    def edit_property(self, user_id, property_id : str, value : str):
        logger.debug(f"Edit property {property_id} for user {user_id}")
        for workout_id in self.user_workouts[user_id].keys():
            prop = self.user_workouts[user_id][workout_id]['default'].find_property_by_id(property_id)
            if prop is not None:
                try:
                    v = int(value)
                    if (v < prop.value_min) or (v > prop.value_max):
                        raise ValueError()
                except:
                    raise ValueError()

                prop.value = v
                logger.debug(f"Property {prop} {property_id} modified")

                try:
                    _user = User.objects.get(id=user_id)
                    try:
                        rec = UserWorkoutProps.objects.get(user = _user, prop_id = property_id)
                    except:
                        rec = UserWorkoutProps(user = _user, prop_id = property_id)
            
                    rec.value = v
                    rec.save()
                    logger.info(f"Parameter {prop.caption} saved for user {_user}")
                except:
                    # Unable to save prop in database for anonimous user
                    return False
                return True
                
