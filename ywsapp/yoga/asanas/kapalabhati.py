#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kapalabhati.py
#  
#  Copyright 2025 Dmitry Repnikov <acid454@yoga7>
#  

import math
from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeRest, MetronomeKapalabhati
from snd_pools import SND_POEHALI, SND_COMPLETION_OTHERS, SND_I_DALSHE

class Kapalabhati(BaseAsana):
    def __init__(self, **kwargs):
        super().__init__(name="kapalabhati", caption="Капалабхати")
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=8))
        self.properties.append(IntProperty(caption="время выполнения", short="tm_main", default=50))
        self.properties.append(IntProperty(caption="отдых", short="tm_exit", default=10))
        self.update_props(kwargs)

        self.tasks.append(BaseTask(
            caption=self.caption + "\nподготовка",
            property=self.tm_prepare,
            images=["kapalabhati_prepare"],
            metronome = MetronomeRest()
        ))
        self.pool("name").append("name_kapalabhati1")
        self.pool("end").append(SND_POEHALI)

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            images=["kapalabhati_prepare"],
            metronome = MetronomeKapalabhati()
        ))
        #self.pool("start").append("kapalabhati_5sec_8cycles", mandatory = True)

        self.tasks.append(BaseTask(
            caption=self.caption + "\nотдых",
            property=self.tm_exit,
            images=["kapalabhati_prepare"],
            metronome = MetronomeRest()
        ))
        self.pool("name").append(SND_COMPLETION_OTHERS)
        self.pool("end").append(SND_I_DALSHE)