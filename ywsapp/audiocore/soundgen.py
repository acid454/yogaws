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
import multiprocessing
from resmanager import ResourcesManager
from speech_manager import SpeechManager


class SoundComposer():
    def __init__(self, lines):
        self.conn1, self.conn2 = multiprocessing.Pipe(duplex=False)
        self.proc = multiprocessing.Process(
            target=SoundComposer.call_composer,
            args=(self.conn2, lines,))
        self.proc.start()
        self.result = None
    
    def sound_ready(self):
        if self.result is None:
            return self.conn1.poll()
        return True
    
    def get_result(self):
        if self.result is not None:
            return self.result
        self.result = self.conn1.recv()
        self.proc.join()
        self.conn1.close()
        self.conn2.close()
        self.proc.close()
        return self.result

    @staticmethod
    def call_composer(connector, composer_lines):
        #print('\n'.join(composer_lines))
        composer_lines.append(',')   # ToDo: fix this, last bell sound longer, than just a second
        composer_lines.append(',')
        result = subprocess.run(ResourcesManager().sound_composer(), 
                                input=bytes('\n'.join(composer_lines), 'ascii'),
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        #print(result.stderr.decode("utf-8"))
        stdout = result.stdout if result.returncode == 0 else None
        connector.send(stdout)
        return


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
        
        self.metronomes = {}
        for k in metronomes.keys():
            self.metronomes[k] = resman.wave_file(metronomes[k])
        
        self.audio_data = {}
        speech_man = SpeechManager()
        for k in speech_man.mp3_files.keys():
            self.audio_data[speech_man.mp3_files[k].file] = resman.sound_file(k)
    
    def generate(self, workout):
        # Create main stream with ticks
        composer_lines = []
        for t in range(workout['total_time_int']):
            schedule = workout['schedule']
            current_task = workout['timetable'][schedule[t]]
            composer_lines.append("")
            # Bell or tick sound, at the start (end?) of each second
            if (t == workout['total_time_int']-1) or (schedule[t] != schedule[t+1]):
                metronome_snd = self.metronomes[current_task['metronome']['bell']]
            else:
                metronome_snd = self.metronomes.get(current_task['metronome']['tick'], None)
            
            composer_lines[-1] = metronome_snd + ',' if metronome_snd is not None else ','
            
            for snd_start_tm in current_task['sounds'].keys():
                if t == schedule[t] + snd_start_tm:
                    k = current_task['sounds'][snd_start_tm]
                    composer_lines[-1] += self.audio_data[k['file']] + ','
        
        return SoundComposer(composer_lines)
        