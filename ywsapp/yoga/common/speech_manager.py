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
    used: bool = False


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
        self.mp3_files = {}
        for fl in mp3_files:
            self.mp3_files[fl[:-4]] = SoundElement(
                    file = fl,
                    length = math.ceil(MP3(os.path.join(mp3_path, fl)).info.length))


    # Select (uses) one of pool's sounds (random), which is ok with length (time)
    def select_random_sound(self, pool_items, time, can_be_empty, only_mandatory, voice_acting):
        result = []
        
        # First, filter all sounds, long/short enought
        for item in pool_items:
            fl_name = item['file']
            can_overlapse = item.get('overlapse', False)
            if fl_name.endswith('_overlapse'):
                can_overlapse = True
                fl_name = fl_name[:-len('_overlapse')]
                print(f"WARNING! Old overlapse name format for {fl_name}")
            
            if only_mandatory and not item.get('mandatory', False):
                continue

            voice_actings = item.get('only_actings', None)
            if voice_actings is not None:
                if not (voice_acting in voice_actings):
                    continue

            if self.mp3_files[fl_name].length <= time or can_overlapse:
                r = replace(self.mp3_files[fl_name])        # replace is from dataclasses. It just creates a copy of element
                r.pool_item = item                          #  add link to pool of this sound
                r.original = self.mp3_files[fl_name]        #  and also link to original item, just only to inc usage count
                result.append(r)

        if len(result) == 0:
            # No sounds good enought to choose from
            return SoundElement()

        if can_be_empty:
            result.append(SoundElement())
            result[-1].original = result[-1]

        selected_items = list(filter(lambda x: not x.original.used, result))
        if len(selected_items) == 0:
            for x in result:
                x.original.used = False
            selected_items = result
        itm = selected_items[random.randint(0, len(selected_items)-1)]
        itm.original.used = True
        return itm

    # Returns true if this pool is needed
    def check_only_mandatory_flag(self, pool_nm, voice_acting):
        if pool_nm == "name":
            return False        # Name allways
        
        if voice_acting == 4:
            return True
        
        if voice_acting == 3 and pool_nm == "end":
            return False
        
        if voice_acting == 2 and pool_nm in ["float", "continue"]:
            return True
        
        if voice_acting == 1 and pool_nm == "float":
            return True

        return False if voice_acting == 0 else True

    def do_generate_task_sounds(self, w, t, voice_acting, overlapse_offset = 0):
        remain_task_time = t.property.value     # Need this to know, how much time we got for float sound
        cur_time_idx = overlapse_offset
        float_time_idx = overlapse_offset

        for pool_nm in ["start", "name", "continue", "end"]:
            # ----- Select one random sound for this pool
            task_snd_pool = t.pool(pool_nm)

            # Check if this pool is used
            only_mandatory = self.check_only_mandatory_flag(pool_nm, voice_acting)

            s = self.select_random_sound(task_snd_pool.items,
                                         t.property.value - cur_time_idx,
                                         task_snd_pool.can_be_empty,
                                         only_mandatory,
                                         voice_acting)
            if s.length == 0:
                if not task_snd_pool.can_be_empty and len(task_snd_pool.items) > 0:
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
            only_mandatory = self.check_only_mandatory_flag("float", voice_acting)
            print(f"ONLY MANDATORY: {only_mandatory}")
            s = self.select_random_sound(t.pool("float").items, remain_task_time, empt, only_mandatory, voice_acting)
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


    def generate_sounds(self, workout, voice_acting):
        overlapse_tm = 0
        for s in workout.sets:
            for a in s.asanas:
                for t in a.tasks:
                    overlapse_tm = self.do_generate_task_sounds(workout, t, voice_acting, overlapse_tm)
