#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  resmanager.py
#  
#  Copyright 2025 Repnikov Dmitry <acid454@yoga7>
#  

import os
import sys
import random

#
# It is a PATH MANAGER, not resources!
class ResourcesManager():
    WORKOUTS_PATH = "workouts"
    SETS_PATH = "sets"
    ASANAS_PATH = "asanas"
    SOUND_COMPOSER_EXEC = "sound_composer"
    GLOBAL_PYTHON_PATHS = [ "", "sets", "common", "containers", "asanas" ]

    #
    # Singleton class for resources manager
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ResourcesManager, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        random.seed()
        base_path = os.path.dirname(os.path.abspath(__file__))
        
        self.res_path = os.path.join(base_path, 'static', 'ywsapp', 'res')
        sys.path.append(os.path.join(base_path))
        for p in ResourcesManager.GLOBAL_PYTHON_PATHS + [ResourcesManager.WORKOUTS_PATH]:
            sys.path.append(os.path.join(base_path, 'yoga', p))

        self.main_bg_images = os.listdir(os.path.join(self.res_path, 'mainbg'))
        self.active_bg_images = os.listdir(os.path.join(self.res_path, 'activebg'))
        self.workout_files_list = list(filter(lambda x: x.endswith(".py"),
                            os.listdir(os.path.join(base_path, 'yoga', ResourcesManager.WORKOUTS_PATH)) ))
        self.sound_composer_exec = os.path.join(base_path, '..', 'scripts', 'sound_composer')
        self.sets_files_list = list(filter(lambda x: x.endswith(".py"),
                            os.listdir(os.path.join(base_path, 'yoga', ResourcesManager.SETS_PATH)) ))
        self.asanas_files_list = list(filter(lambda x: x.endswith(".py"),
                            os.listdir(os.path.join(base_path, 'yoga', ResourcesManager.ASANAS_PATH)) ))
    
    def main_bg_image(self):
        return self.main_bg_images[random.randrange(len(self.main_bg_images))]
    
    def active_bg_image(self):
        return self.active_bg_images[random.randrange(len(self.active_bg_images))]
    
    def workout_files(self):
        return self.workout_files_list
    
    def wave_config_file(self):
        return os.path.join(self.res_path, 'wavs', 'wavs.json')
    
    def wave_file(self, w):
        return os.path.join(self.res_path, 'wavs', w)
    
    def sound_file(self, s):
        return os.path.join(self.res_path, 'sounds', s + '.mp3')
    
    def sound_composer(self):
        return self.sound_composer_exec
    
    def list_sets_files(self):
        return self.sets_files_list

    def list_asanas_files(self):
        return self.asanas_files_list

#=============== Initialize (-create) res manager on import ===============
_ = ResourcesManager()
