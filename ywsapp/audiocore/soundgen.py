#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  soundgen.py
#  
#  Copyright 2025 Repnikov Dmitry <acid454@yoga7>
#  

import io
import json
import subprocess
from resmanager import ResourcesManager
from speech_manager import SpeechManager


class SoundGenerator():
    #
    # Singleton class for resources manager
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SoundGenerator, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        # Loading resources...
        resman = ResourcesManager()
        metronomes = json.loads(open(resman.wave_config_file()).read())
        self.sound_compoer = resman.sound_composer()
        
        self.metronomes = {}
        for k in metronomes.keys():
            self.metronomes[k] = resman.wave_file(metronomes[k])
        
        self.audio_data = {}
        speech_man = SpeechManager()
        for k in speech_man.mp3_files.keys():
            self.audio_data[speech_man.mp3_files[k].file] = resman.sound_file(k)


    def call_composer(self, composer_lines):
        result = subprocess.run(self.sound_compoer, 
                                input=bytes('\n'.join(composer_lines), 'ascii'),
                                stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        if result.returncode != 0:
            return None
        return result.stdout
    
    def generate(self, workout):
        # Create main stream with ticks
        composer_lines = []
        for t in range(workout.total_time_int):
            current_task = workout.timetable[workout.schedule[t]]
            composer_lines.append("")
            # Bell or tick sound, at the start (end?) of each second
            if (t == workout.total_time_int-1) or (workout.schedule[t] != workout.schedule[t+1]):
                metronome_snd = self.metronomes[current_task.metronome.bell]
            else:
                metronome_snd = self.metronomes.get(current_task.metronome.tick, None)
            
            composer_lines[-1] = metronome_snd + ',' if metronome_snd is not None else ','
            
            for snd_start_tm in current_task.sounds.keys():
                if t == workout.schedule[t] + snd_start_tm:
                    k = current_task.sounds[snd_start_tm]
                    #print(self.audio_data)
                    composer_lines[-1] += self.audio_data[k.file] + ','
        
        return self.call_composer(composer_lines)
        