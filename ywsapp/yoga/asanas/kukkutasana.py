#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kukkutasana.py
#  
#  Copyright 2023 Repnikov Dmitry <acid454@yoga7>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import *


class Kukkutasana(BaseAsana):
    def __init__(self, **kwargs):
        super().__init__(name="kukkutasana", caption="Куккутасана")
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=7))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=20))
        self.update_props(kwargs)
        
        self.tasks.append(BaseTask(
            caption=self.caption + " (подготовка)",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=["kukkutasana"]
        ))
        self.pool("name").append("name_nedokukkutasana")


        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images
        ))
        self.pool("float").append("descr_kukutasana")
        self.pool("float").append("common1")
        self.pool("float").append("common3")
        self.pool("float").append("common4")
        self.pool("float").append("common5_v_vitalkivanii")
        self.pool("end").append("otlichno")
        self.pool("end").append("i_s_vidohom_na_ladoni_ruk")
        for i in SND_ZAKONCHILI_DALSHE + SND_EXHALE + SND_RASSLABILIS:
            self.pool("end").append(i)
