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
#MAIN_BACKGROUND_IMAGES = os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 
#                                            'static', 'ywsapp', 'res', 'mainbg'))
#ACTIVE_BACKGROUND_IMAGES = os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 
#                                            'static', 'ywsapp', 'res', 'activebg'))
#


class ResourcesManager():
    WORKOUTS_PATH = "workouts"
    GLOBAL_PYTHON_PATHS = [ "", "sets", "common", "containers", "asanas" ]

    def __init__(self):
        random.seed()
        base_path = os.path.dirname(os.path.abspath(__file__))
        res_path = os.path.join(base_path, 'static', 'ywsapp', 'res')

        for p in ResourcesManager.GLOBAL_PYTHON_PATHS + [ResourcesManager.WORKOUTS_PATH]:
            sys.path.append(os.path.join(base_path, 'yoga', p))

        self.main_bg_images = os.listdir(os.path.join(res_path, 'mainbg'))
        self.active_bg_images = os.listdir(os.path.join(res_path, 'activebg'))
        self.workout_files_list = list(filter(lambda x: x.endswith(".py"),
                            os.listdir(os.path.join(base_path, 'yoga', ResourcesManager.WORKOUTS_PATH)) ))
    
    def main_bg_image(self):
        return self.main_bg_images[random.randrange(len(self.main_bg_images))]
    
    def active_bg_image(self):
        return self.active_bg_images[random.randrange(len(self.active_bg_images))]
    
    def workout_files(self):
        return self.workout_files_list
