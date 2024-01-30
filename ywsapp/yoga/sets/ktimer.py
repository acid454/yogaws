#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ktimer.py
#  
#  Copyright 2024 Repnikov Dmitry <acid454@yoga7>
#  

from base import BaseSet, BaseWorkout
from properties import IntProperty
from asanas import Asanas


class KTimer(BaseSet):
    def __init__(self, **kwargs):
        super().__init__(caption="Таймер для упражнений Кегеля")
        self.properties.append(IntProperty(caption="количество циклов", short="cnt", default=6))
        self.properties.append(IntProperty(caption="фиксация", short="tm_action", default=2))
        self.properties.append(IntProperty(caption="расслабление", short="tm_relax", default=2))
        self.update_props(kwargs)
    
    def build(self, workout):
        for i in range(self.cnt.value):
            # Construct new one asana classes every time
            self.asanas.append(Asanas.breath.Breath(_inhale = True, action_text = "фиксация", tm_main = self.tm_action.value))
            self.asanas.append(Asanas.breath.Breath(_inhale = False, action_text = "расслабление", tm_main = self.tm_relax.value))
        
        prev_asana = workout.prev_item(self.asanas[0])
        if type(prev_asana) not in [Asanas.breath.Breath]:
            self.asanas[0].pool("start").append("tts_audio_convert_65b2b1efcd6ba243709482")
        
        super().build(workout)


class KTimerX3(BaseSet):
    def __init__(self, **kwargs):
        super().__init__(caption="Упражнения Кегеля (полный цикл)")
        self.properties.append(IntProperty(caption="нормальные циклы", short="cnt_normal", default=22))
        self.properties.append(IntProperty(caption="замедленные циклы", short="cnt_slow", default=13))
        self.properties.append(IntProperty(caption="быстрые циклы", short="cnt_fast", default=10))
        self.update_props(kwargs)
    
    def build(self, workout):
        for c in [(self.cnt_normal.value, 2, 2), (self.cnt_slow.value, 5, 2), (self.cnt_fast.value, 1, 1)]:
            k = KTimer(visible = False, subcaption=" (быстрый)", tm_action=c[1], tm_relax=c[2], cnt=c[0])
            workout.sets.insert(workout.sets.index(self)+1, k)
            k.build(workout)
            self.asanas += workout.sets.pop(workout.sets.index(self)+1).asanas
