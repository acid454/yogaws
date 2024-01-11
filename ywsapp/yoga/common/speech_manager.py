#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  speech_manager.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

import os, random, math
from mutagen.mp3 import MP3
from dataclasses import dataclass, replace


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

    def select_random_sound(self, pool_items, time, can_be_empty):
        result = []
        if can_be_empty:
            result.append(SoundElement())
        for item in pool_items:
            fl_name = item['file']
            can_overlapse = item.get('overlapse', False)
            if fl_name.endswith('_overlapse'):
                can_overlapse = True
                fl_name = fl_name[:-len('_overlapse')]
            
            if self.mp3_files[fl_name].length <= time or can_overlapse:
                r = replace(self.mp3_files[fl_name])        # replace is from dataclasses. It just creates a copy of element
                r.pool_item = item
                result.append(r)
        #print("Selecting from files: %s"%(list(map(lambda x: x.file, result))))
        
        if len(result) == 0:
            return SoundElement()
        
        # Select one of results, depending on usage count. Less usage - more probability to be selected.
        #  Detect max usage count - that is the lowest prob. Than detect prob = max - usage + 1 for each elem,
        #  and calculate sum of all. Take random of that sum, and for each elem substaract prob from that rand.
        #  If result <= 0 - that is our elem.
        max_usage = max(map(lambda x: x.used, result))
        rev = list(map(lambda x: max_usage - x.used + 1, result))
        #print("Selecting from usages: %s, max: %d, rev sum: %d"%(list(map(lambda x: x.used, result)), max_usage, sum(rev)))
        rand = random.randint(1, sum(rev))
        for x in range(len(rev)):
            rand -= rev[x]
            if rand <= 0:
                #print(f"Selected item #{x} with use count {result[x].used}")
                #print()
                result[x].used += 1
                return result[x]


    def do_generate_task_sounds(self, w, t, overlapse_offset = 0):
        cur_time_idx = overlapse_offset
        remain_task_time = t.property.value     # Need this to know, how much time we got for float sound

        float_time_idx = overlapse_offset
        for pool_nm in ["start", "name", "continue", "end"]:
            # ----- Select one random sound for this pool
            emtp = t.pool(pool_nm).can_be_empty
            s = self.select_random_sound(t.pool(pool_nm).items, t.property.value - cur_time_idx, emtp)
            if s.length == 0:
                if not emtp and len(t.pool(pool_nm).items) > 0:
                    print(f"WARNING! No sounds selected for task {t.caption} pool {pool_nm}")
                continue

            remain_task_time -= s.length                    # We place this sound...
            if pool_nm == "end":
                # ... the end case
                cur_time_idx = t.property.value - s.length
            t.sounds[cur_time_idx] = s                      # ...at cur_time_idx
            cur_time_idx += t.sounds[cur_time_idx].length   # and move index forward
            if pool_nm != "end":
                # also, move float time start index - index, where float sound can start
                float_time_idx = cur_time_idx
        
        #print(f"Processing float: remain task time {remain_task_time}, idx {float_time_idx}")
        if remain_task_time > 0:
            empt = t.pool("float").can_be_empty
            s = self.select_random_sound(t.pool("float").items, remain_task_time, empt)
            if s.length > 0:
                if remain_task_time > s.length:
                    if not s.pool_item.get('float_on_start'):
                        float_time_idx += random.randrange(remain_task_time - s.length)
                t.sounds[float_time_idx] = s
        
        # Some debug, if needed:
        #print(f"------------ {t.caption} ----------------")
        #for k in t.sounds.keys():
        #    print("  %03d .. %03d %s"%(k, k+t.sounds[k].length, t.sounds[k].file))

        # Ok, check for inter-tasks's overlapses - return longest sound element
        ret = 0
        for k in t.sounds.keys():
            v = k + t.sounds[k].length
            ret = max(v, ret)
        ret = ret - t.property.value
        return ret if ret > 0 else 0


    def generate_sounds(self, workout):
        overlapse_tm = 0
        for s in workout.sets:
            for a in s.asanas:
                for t in a.tasks:
                    overlapse_tm = self.do_generate_task_sounds(workout, t, overlapse_tm)
