#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  utthita.py
#  
#  Copyright 2025 Dmitry Repnikov <acid454@yoga7>
#  

from base import BaseTask
from parshvaconasana_base import BaseParshvaconasana
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import *


# Class for main utthita (with preparation)
class UtthitaBase(BaseParshvaconasana):
    def __init__(self, _side, _caption):
        super().__init__(name="utthita_%s"%(_side), caption=_caption, side=_side)
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=12))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=30))

        self.tasks.append(BaseTask(
            caption=self.caption + "\nподготовка",
            property=self.tm_prepare,
            metronome=MetronomeRest()
        ))
        self.preparation_sounds_with_hand()

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork()
        ))
        self.utthita_parivritta_main_sounds()

    def build(self, workout, _set):
        super().build(workout, _set)
        if self.is_prev_asana_same_leg(workout):
            self.tm_prepare.default = 11    # We are somewhere with same leg - only hands changes

    def build_snd_name(self, prev_asana):
        print(f"utthita base build snd name, is prev utthita: {issubclass(type(prev_asana), UtthitaBase)}")
        if issubclass(type(prev_asana), UtthitaBase):
            return
        self.tasks[0].pool("name").append("name_utthita_parshvakonasana")


class UtthitaLeft(UtthitaBase):
    def __init__(self, **kwargs):
        super().__init__('left', "Уттхита Паршваконасана\n(левая нога)")
        self.update_props(kwargs)
        self.update_all_tasks_images([f"utthita_parshvakonasana_left{x}" for x in range(1,3)])
    
    def build_snd_name(self, prev_asana):
        print("utthita left build snd name")
        super().build_snd_name(prev_asana)
        self.tasks[0].pool("continue").append("short_enter_utthita_left", overlapse = True)
        self.tasks[-1].pool("end").append("vernuli_pravuju_ruku")


class UtthitaRight(UtthitaBase):
    def __init__(self, **kwargs):
        super().__init__('right', "Уттхита Паршваконасана\n(правая нога)")
        self.update_props(kwargs)
        self.update_all_tasks_images([f"utthita_parshvakonasana_right{x}" for x in range(1,3)])
    
    def build_snd_name(self, prev_asana):
        print("utthita right build snd name")
        super().build_snd_name(prev_asana)
        #self.tasks[0].pool("continue").append("short_enter_parivritta_parshvakonasana_right1")
        #self.tasks[0].pool("continue").append("short_enter_parivritta_parshvakonasana_right2")
        #self.tasks[0].pool("continue").append("short_enter_parivritta_parshvakonasana_right3")
