#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  virabhadrasana.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

import random
from base import BaseTask
from parshvaconasana_base import BaseParshvaconasana
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import *

# Class for main virabhadrasana (with preparation)
class VirabhadrasanaBase(BaseParshvaconasana):
    def __init__(self, _side, _caption):
        super().__init__(name="virabhadrasana_%s"%(_side), caption=_caption, side = _side, prepare_tm_for_swap_hands = 4)
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=8))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=40))

        self.tasks.append(BaseTask(
            caption=self.caption + "\nподготовка",
            property=self.tm_prepare,
            metronome=MetronomeRest()
        ))

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork()
        ))

        # virabhadrasana_snds goes here - all this goes to main fixation task
        self.pool("continue").append("enter_virabhadrasana1")
        self.pool("continue").append("enter_virabhadrasana2")
        self.pool("continue").append("enter_virabhadrasana3")
        self.pool("continue").append("enter_virabhadrasana4")
        self.pool("float").append("descr_virabhadrasana1")
        self.pool("continue" if random.randint(0, 1) else "float").append("descr_virabhadrasana3", tags="enter,long")
        self.pool("float").append("descr_virabhadrasana4")
        self.pool("float").append("descr_virabhadrasana5")
        self.pool("float").append("descr_virabhadrasana6")
        self.pool("continue").append("descr_virabhadrasana7")
        self.pool("float").append("descr_virabhadrasana8")
        self.pool("float").append("descr_virabhadrasana9")
        self.pool("continue").append("descr_virabhadrasana10")
        self.pool("float").append("descr_virabhadrasana11")
        self.pool("continue").append("descr_virabhadrasana12")
        self.pool("float").append("descr_virabhadrasana13")
        self.pool("float").append("descr_virabhadrasana14")
        self.pool("float").append("common_povtoriaushiesia_pozu")

        #!!!!!!! TODO: short sounds
        self.pool("end").append(SND_RASSLABILIS + SND_EXHALE + SND_S_VIDOHOM_VNIZ) 
    
    def build_snd_name(self, prev_asana):
        if issubclass(type(prev_asana), VirabhadrasanaBase):
            return
        self.tasks[0].pool("name").append("name_virabhadrasana1")
        self.tasks[0].pool("name").append("name_virabhadrasana2")
        self.tasks[0].pool("name").append("name_virabhadrasana3")
        self.tasks[0].pool("name").append("name_virabhadrasana4")
        self.tasks[0].pool("name").append("name_virabhadrasana5")

class VirabhadrasanaLeft(VirabhadrasanaBase):
    def __init__(self, **kwargs):
        super().__init__('left', "Вирабхадрасана (левая нога)")
        self.update_props(kwargs)
        self.update_all_tasks_images([f"virabhadrasana_left{x}" for x in range(1,5)])

class VirabhadrasanaRight(VirabhadrasanaBase):
    def __init__(self, **kwargs):
        super().__init__('right', "Вирабхадрасана (правая нога)")
        self.update_props(kwargs)
        self.update_all_tasks_images([f"virabhadrasana_right{x}" for x in range(1,5)])
