#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  stol.py
#  
#  Copyright 2023 Repnikov Dmitry <acid454@yoga7>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import *


class Stol(BaseAsana):
    def __init__(self, **kwargs):
        super().__init__(name="stol", caption="Стол")
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=7))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=40))
        self.update_props(kwargs)
        
        self.tasks.append(BaseTask(
            caption=self.caption + " (подготовка)",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=["stol1"]
        ))
        self.pool("name").append("name_stol")


        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images
        ))
        self.pool("float").append("common1")
        self.pool("float").append("common3")
        self.pool("float").append("common4_dushim_dershimsia")
        self.pool("float").append("common5_v_vitalkivanii")
        self.pool("float").append("common6")
        self.pool("float").append("common10")
        self.pool("float").append("common_duhanie_rovnoe_estestvennoe")
        self.pool("float").append("common_sledim_za_geometriei_kak_zadumanno")
        self.pool("end").append(SND_COMPLETION_OTHERS + SND_ZAKONCHILI_DALSHE + SND_EXHALE + SND_RASSLABILIS)
