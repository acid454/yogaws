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
    def __init__(self, **kwargs):
        super().__init__(name="bakasana", caption="Бакасана")
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=16))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=50))
        self.update_props(kwargs)
        
        self.tasks.append(BaseTask(
            caption=self.caption + " (подготовка)",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=[f"bakasana{x}" for x in range(1,2)]
        ))
        self.pool("start").append("name_bakasana1")
        self.pool("start").append("name_bakasana2")
        self.pool("start").append("name_bakasana3")
        self.pool("continue").append("enter_bakasana1")
        self.pool("continue").append("enter_bakasana2")


        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images
        ))
        self.pool("start").append("common3")
        self.pool("start").append("common4")
        self.pool("start").append("common6")
        self.pool("start").append("common7")
        self.pool("start").append("common10")
        self.pool("start").append("common_i_postojat'_podushat'")
        self.pool("start").append("common_esli_chto_to_ne_poluchaetsia")
        self.pool("start").append("descr_ardhachandrasana_common1")
        self.pool("start").append("descr_ardhachandrasana_zameret'")
        self.pool("end").append("otlichno")
        self.pool("end").append("i_s_vidohom_na_ladoni_ruk")
        for i in SND_ZAKONCHILI_DALSHE + SND_EXHALE + SND_RASSLABILIS:
            self.pool("end").append(i)
