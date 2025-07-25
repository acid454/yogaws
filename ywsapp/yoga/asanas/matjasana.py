#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  matjasana.py
#  
#  Copyright 2023 Repnikov Dmitry <acid454@yoga7>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import *


class Matjasana(BaseAsana):
    def __init__(self, **kwargs):
        super().__init__(name="matjasana", caption="Матсьясана")
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=12))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=60))
        self.properties.append(IntProperty(caption="выход", short="tm_exit", default=5))
        self.update_props(kwargs)
        
        self.tasks.append(BaseTask(
            caption=self.caption + " (подготовка)",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=["matjasana1", "matjasana2"]
        ))
        self.pool("name").append("name_matjasana1")
        self.pool("end").append("enter_matjasana1")

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images
        ))
        self.pool("float").append("descr_matjasana1")
        self.pool("float").append("descr_matjasana2")
        self.pool("float").append("common_delaem_plavno")
        self.pool("float").append("common8")
        self.pool("float").append("common9")
        self.pool("float").append("common10")
        self.pool("float").append("marichiasana_common_sledim_za_pozvonochnikom")
        self.pool("float").append("common_vsie_budet_horosho")
        self.pool("float").append("common_vihodim_iz_asan_plavno")
        self.pool("end").append(SND_RASSLABILIS)
        
        self.tasks.append(BaseTask(
            caption=self.caption + " (выход)",
            property=self.tm_exit,
            metronome=MetronomeRest(),
            images=["matjasana1", "matjasana2"]
        ))
        self.pool("start").append(SND_VERNULIS)
        self.pool("end").append(SND_ZAKONCHILI_DALSHE)
        