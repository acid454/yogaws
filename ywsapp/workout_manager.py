#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  workout_manager.py
#  
#  Copyright 2025 Repnikov Dmitry <acid454@yoga7>
#  

import logging
import hashlib
from .resmanager import ResourcesManager
logger = logging.getLogger("ywsapp")


class WorkoutManager:
    def __init__(self):
        self.workouts = {}
        logger.info("workout files:")
        logger.info("\n".join(ResourcesManager().workout_files()))

        # Prepare workouts on initialization
        for f in ResourcesManager().workout_files():
            try:
                workouts = __import__(f[:-3]).do_load_workouts()
                for w in workouts:
                    wid = hashlib.md5((f + ':' + w.__name__).encode()).hexdigest()
                    self.workouts[wid] = {
                        'class':w,
                        'default':w().build(None, wid),
                        'filenm':f,
                        'wid':wid
                    }
            except:
                logger.exception(f"exception while loading workout {f}")

    def list_workouts(self):
        return self.workouts.values()

    def load_workout(self, wid : str):
        return self.workouts.get(wid, None)

    def edit_setting(self, setting_name : str, value : str):
        pass

    def find_property_by_id(self, preperty_id):
        for workout_id in self.workouts.keys():
            result = self.workouts[workout_id]['default'].find_property_by_id(preperty_id)
            if result is not None:
                return result
