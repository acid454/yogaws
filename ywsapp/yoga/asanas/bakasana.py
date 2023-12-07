#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bakasana.py
#  
#  Copyright 2023 Repnikov Dmitry <acid454@yoga7>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import *


class Bakasana(BaseAsana):
    def __init__(self, side = 'middle', **kwargs):
        if side == 'left':
            caption_side = '\n(левая сторона)'
        elif side == 'right':
            caption_side = '\n(правая сторона)'
        else:
            caption_side = ''
        super().__init__(name="bakasana", caption="Бакасана%s"%(caption_side))
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=16))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=50))
        self.properties.append(IntProperty(caption="выход", short="tm_exit", default=5))
        self.update_props(kwargs)
        
        self.tasks.append(BaseTask(
            caption=self.caption + "\n(подготовка)",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=[f"bakasana{x}" for x in range(1,2)]
        ))
        if side == 'middle':
            self.pool("continue").append("enter_bakasana1")
            self.pool("continue").append("enter_bakasana2")
        elif side == 'left':
            self.pool("continue").append("left_side1")
            self.pool("continue").append("left_side2")
        else:
            self.pool("continue").append("upr_skrutka_vpravo")


        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images
        ))
        self.pool("float").append("common3")
        self.pool("float").append("common4")
        self.pool("float").append("common6")
        self.pool("float").append("common7")
        self.pool("float").append("common10")
        self.pool("float").append("common12")
        self.pool("continue").append("common_i_postojat'_podushat'")
        self.pool("float").append("common_esli_chto_to_ne_poluchaetsia")
        self.pool("continue").append("descr_ardhachandrasana_common1")
        self.pool("continue").append("descr_ardhachandrasana_zameret'")

        self.tasks.append(BaseTask(
            caption=self.caption + "\n(выход)",
            property=self.tm_exit,
            metronome=MetronomeRest(),
            images=self.tasks[-1].images
        ))
        self.pool("start").append("otlichno")
        self.pool("start").append("i_s_vidohom_na_ladoni_ruk")
        for i in SND_EXHALE + SND_RASSLABILIS:
            self.pool("start").append(i)

    def build(self, workout, _set):
        super().build(workout, _set)
        prev_asana = workout.prev_item(self)
        if issubclass(type(prev_asana), Bakasana):
            t = self.task(self.tm_prepare)
            t.pool("start").clear()
            for i in SND_NA_DRUGUJU_STORONU:
                t.pool("start").append(i)
            return
        
        with self.task(self.tm_prepare) as t:
            t.pool("name").append("name_bakasana1")
            t.pool("name").append("name_bakasana2")
            t.pool("name").append("name_bakasana3")
        with self.task(self.tm_exit) as t:
            for i in SND_ZAKONCHILI_DALSHE:
                t.pool("start").append(i)
    