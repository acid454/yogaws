#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  speech_manager.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

import os, random, math
from mutagen.mp3 import MP3
from dataclasses import dataclass


BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@dataclass
class SoundElement:
    file: str = None
    length: int = 0
    used: int = 0


class SpeechManager:
    POOLS = ["start", "name", "continue", "float", "end"]
    # Singleton class for speech manager, see
    #  https://www.geeksforgeeks.org/singleton-pattern-in-python-a-complete-guide/
    #  The new method is a static method that belongs to the class itself.
    #  It's responsible for creating and returning a new instance of the class.
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SpeechManager, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        # List all sound files, their lengths
        mp3_path = os.path.join(BASE_PATH, 'static', 'ywsapp', 'res', 'sounds_merged')
        mp3_files = os.listdir(mp3_path)
        mp3_files = list(filter(lambda x: x.endswith(".mp3"), mp3_files))
        #print("MP3 files loaded: " + str(mp3_files))

        self.mp3_files = {}
        for fl in mp3_files:
            self.mp3_files[fl[:-4]] = SoundElement(
                    file = fl,
                    length = math.ceil(MP3(os.path.join(mp3_path, fl)).info.length))
        #print("MP3:")
        #print(self.mp3_files)

    def select_random_sound(self, files, time):
        result = []
        for f in files:
            if f is None:
                result.append(SoundElement())
            elif self.mp3_files[f].length < time:
                result.append(self.mp3_files[f])
        print("Selecting from files: %s"%(list(map(lambda x: x.file, result))))
        
        # ToDo: implement use count here
        if len(result) == 0: return SoundElement()
        return result[random.randrange(len(result))]


    def do_generate_task_sounds(self, w, t):
        cur_time_idx = 0
        remain_task_time = t.property.value

        float_time_idx = 0
        for pool_nm in ["start", "name", "continue", "end"]:
            print("Processing pool '%s'..."%(pool_nm))
            s = self.select_random_sound(t.pool(pool_nm).files, t.property.value - cur_time_idx)
            if s.length == 0: continue
            remain_task_time -= s.length
            if pool_nm == "end":
                cur_time_idx = t.property.value - s.length
            t.sounds[cur_time_idx] = s
            print("  %s selected, length %d; cur. tm: %d."%(t.sounds[cur_time_idx].file, t.sounds[cur_time_idx].length, cur_time_idx))
            cur_time_idx += t.sounds[cur_time_idx].length
            if pool_nm != "end":
                float_time_idx = cur_time_idx
        
        print("Processing float: remain task time %d, idx %d", remain_task_time, float_time_idx)
        s = self.select_random_sound(t.pool("float").files, remain_task_time)
        if s.length > 0:
            t.sounds[float_time_idx] = s
        print("Task %s sounds: %s"%(t.caption, str(t.sounds)))
        print()


    def generate_sounds(self, workout):
        for s in workout.sets:
            for a in s.asanas:
                for t in a.tasks:
                    self.do_generate_task_sounds(workout, t)
