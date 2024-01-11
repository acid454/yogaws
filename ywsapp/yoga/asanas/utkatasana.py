#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  utkatasana.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import *


class Utkatasana(BaseAsana):
    def __init__(self, **kwargs):
        super().__init__(name="most", caption="Уткатасана")
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=7))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=40))
        self.update_props(kwargs)
        
        self.tasks.append(BaseTask(
            caption=self.caption + " (подготовка)",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=["utkatasana1"]
        ))
        self.pool("start").append("name_utkatasana")
        self.pool("continue").append("enter_utkatasana", overlapse = True)

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images
        ))
        self.pool("float").append("common_derzimsia_dushim")
        self.pool("float").append("common_dushim_derzim_t'anemsia")
        self.pool("float").append("common1")
        self.pool("float").append("common3")
        self.pool("float").append("common4")
        self.pool("float").append("common6")
        self.pool("float").append("common7")
        self.pool("float").append("common10")
        for i in SND_EXHALE + SND_RASSLABILIS + SND_ZAKONCHILI_DALSHE:
            self.pool("end").append(i)
