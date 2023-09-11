#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  snd_container.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

import os
from base import BASE_PATH


class SndContainer:
    # Singleton class for container, see
    #  https://www.geeksforgeeks.org/singleton-pattern-in-python-a-complete-guide/
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SndContainer, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        # List all sound files, their lengths
        mp3_files = os.listdir(os.path.join(BASE_PATH, 'static', 'ywsapp', 'res', 'sounds_merged'))
        mp3_files = list(filter(lambda x: x.endswith(".mp3"), mp3_files))
        print("MP3 files loaded: " + str(mp3_files))
