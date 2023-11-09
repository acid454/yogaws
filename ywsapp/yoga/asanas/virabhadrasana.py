#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  virabhadrasana.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import AsanaLegForward, BaseTask, SoundPool
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from surya_namaskar import SuryaNamaskar
from snd_pools import *

# Class for main virabhadrasana (with preparation)
class VirabhadrasanaBase(AsanaLegForward):
    def __init__(self, _side, _caption):
        super().__init__(name="virabhadrasana_%s"%(_side), caption=_caption)
        self.side = _side
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=4))
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
        self.pool("continue").append("descr_virabhadrasana3")
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

        #!!!!!!! TODO: short sounds

        for i in SND_RASSLABILIS + SND_EXHALE + SND_S_VIDOHOM_VNIZ:
            self.pool("end").append(i) 

    def build(self, workout, _set):
        # are we in suria? if yes - delete preparation
        if type(_set) is SuryaNamaskar:
            del self.tasks[0]
        
        prev_asana = workout.prev_item(self)
        if type(prev_asana) is AsanaLegForward:
            if prev_asana.side == self.side:
                # this and prev asana is same legs (same side), but different hands
                self.build_snd_swap_hands()
            else:
                # different leg forward
                for snd in SND_MENIAJEM_NOGI:
                    self.tasks[0].pool("start").append(snd)
        else:
            # prev asana was not leg-forwarded
            if self.side == 'left':
                self.tasks[0].pool("start").append("leg_left_forward1")
                self.tasks[0].pool("start").append("leg_left_forward2")
                self.tasks[0].pool("start").append("leg_left_forward3")
                self.tasks[0].pool("start").append("leg_left_forward4")
                self.tasks[0].pool("start").append("leg_left_forward5")
                self.tasks[0].pool("start").append("leg_left_forward6")
            else:
                for snd in SND_LEG_RIGHT_FORWARD:
                    self.tasks[0].pool("start").append(snd)
        
        if type(prev_asana) is not type(self):
            self.build_snd_name()
   
    def build_snd_swap_hands(self):
        self.tasks[0].pool("start").append("ladoni_ruk_menijautsia_mestami")
        self.tasks[0].pool("start").append("obratnaja_ei")  #?? not everytime
    
    def build_snd_name(self):
        self.tasks[0].pool("name").append("name_virabhadrasana1")
        self.tasks[0].pool("name").append("name_virabhadrasana2")
        self.tasks[0].pool("name").append("name_virabhadrasana3")
        self.tasks[0].pool("name").append("name_virabhadrasana4")
        self.tasks[0].pool("name").append("name_virabhadrasana5")

class VirabhadrasanaLeft(VirabhadrasanaBase):
    def __init__(self, **kwargs):
        super().__init__('left', "Вирабхадрасана (левая нога)")
        self.update_props(kwargs)
        self.tasks[0].images = ["virabhadrasana_left1", "virabhadrasana_left2", "virabhadrasana_left3", "virabhadrasana_left4"]
        self.tasks[1].images = self.tasks[0].images

class VirabhadrasanaRight(VirabhadrasanaBase):
    def __init__(self, **kwargs):
        super().__init__('right', "Вирабхадрасана (правая нога)")
        self.update_props(kwargs)
        self.tasks[0].images = ["virabhadrasana_right1", "virabhadrasana_right2", "virabhadrasana_right3", "virabhadrasana_right4"]
        self.tasks[1].images = self.tasks[0].images
