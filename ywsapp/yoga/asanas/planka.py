#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  planka.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import SND_ZAKONCHILI_DALSHE


class Planka(BaseAsana):
    def __init__(self):
        BaseAsana.__init__(self, name="planka", caption="Планка")
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=4))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=40))
        
        self.tasks.append(BaseTask(
            caption=self.caption + " (подготовка)",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=["planka1", "planka2"]
        ))
        self.pool("start").append("opustilis'_1")
        self.pool("start").append("opustilis'_2")
        self.pool("start").append("opustilis'_3")
        self.pool("start").append("opustilis'_4")
        self.pool("name").append("name_planka1")
        self.pool("name").append("name_planka2")
        self.pool("name").append("name_planka3")

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=["planka1", "planka2"]
        ))
        self.pool("start").append("descr_planka1")
        self.pool("start").append("descr_planka2")
        self.pool("start").append("descr_planka3")
        self.pool("start").append("descr_planka4")
        self.pool("continue").append("derzhim1")
        self.pool("continue").append("derzhim2")
        self.pool("continue").append("stoim_derzhim")
        self.pool("float").append("common3")
        self.pool("float").append("common4")
        self.pool("float").append("common6")
        self.pool("float").append("common7")
        self.pool("float").append("common10")
        self.pool("float").append("common12")
        for i in SND_ZAKONCHILI_DALSHE:
            self.pool("end").append(i)
