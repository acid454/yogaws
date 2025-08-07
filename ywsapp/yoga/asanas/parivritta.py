#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  parivritta.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseTask
from parshvaconasana_base import BaseParshvaconasana
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import *


# Class for main parivritta (with preparation)
class ParivrittaBase(BaseParshvaconasana):
    def __init__(self, _side, _caption):
        super().__init__(name="parivritta_%s"%(_side), caption=_caption, side=_side)
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
        self.pool("float").append("descr_parivritta_parshvakonasana1")
        self.pool("float").append("descr_parivritta_parshvakonasana4")
    
    def build(self, workout, _set):
        super().build(workout, _set)
        if self.is_prev_asana_same_leg(workout):
            self.tm_prepare.default = 8    # We are in utthita/parivritta, and leg is same - only swap hands

    def build_snd_name(self, prev_asana):
        if not issubclass(type(prev_asana), ParivrittaBase):
            self.tasks[0].pool("name").append("name_parivritta_pashvakonasana1")
            self.tasks[0].pool("name").append("name_parivritta_pashvakonasana2")


class ParivrittaLeft(ParivrittaBase):
    def __init__(self, **kwargs):
        super().__init__('left', "Паривритта Паршваконасана\n(левая нога)")
        self.update_props(kwargs)
        self.update_all_tasks_images([f"parivritta_parshvakonasana_left{x}" for x in range(1,5)])
    
    def build_snd_name(self, prev_asana):
        super().build_snd_name(prev_asana)
        self.tasks[0].pool("continue").append("short_enter_parivritta_parshvakonasana_left1")
        self.tasks[0].pool("continue").append("short_enter_parivritta_parshvakonasana_left2")
        self.tasks[0].pool("continue").append("enter_parivritta_parshvakonasana_left")


class ParivrittaRight(ParivrittaBase):
    def __init__(self, **kwargs):
        super().__init__('right', "Паривритта Паршваконасана\n(правая нога)")
        self.update_props(kwargs)
        self.update_all_tasks_images([f"parivritta_parshvakonasana_right{x}" for x in range(1,5)])
    
    def build_snd_name(self, prev_asana):
        super().build_snd_name(prev_asana)
        self.tasks[0].pool("continue").append("short_enter_parivritta_parshvakonasana_right1")
        self.tasks[0].pool("continue").append("short_enter_parivritta_parshvakonasana_right2")
        self.tasks[0].pool("continue").append("short_enter_parivritta_parshvakonasana_right3")
        self.tasks[-1].pool("end").append("vernuli_pravuju_ruku")
