#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  scorpion.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import *


class Scorpion(BaseAsana):
    def __init__(self, **kwargs):
        super().__init__(name="scorpion", caption="Скорпион")
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=11))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=30))
        self.properties.append(IntProperty(caption="переход", short="tm_swap", default=9))
        self.update_props(kwargs)
        
        self.tasks.append(BaseTask(
            caption=self.caption + "\n(подготовка, правая рука)",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=["scorpion_left"]
        ))

        #ToDo: ????????? Why SND_OPUSTILIS_NA_KOLENI doubled, in say, yoga home training?
        #for i in SND_OPUSTILIS_NA_KOLENI:
        #    self.pool("start").append(i)
        self.pool("name").append("enter_scorpion_left", overlapse = True)

        self.tasks.append(BaseTask(
            caption=self.caption + "\n(правая рука)",
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images
        ))
        self.pool("float").append("descr_scorpion_vse_mushci")
        self.pool("float").append("descr_scorpion")

        #for i in SND_RASSLABILIS + SND_EXHALE:
        #    self.pool("start").append(i)
        #ToDo: this is also from dzathara
        for i in SND_COMPLETION_OTHERS:
            self.pool("end").append(i)
        self.pool("end").append("vernulis'_v_ishodnuju")


        self.tasks.append(BaseTask(
            caption=self.caption + "\n(подготовка, левая рука)",
            property=self.tm_swap,
            metronome=MetronomeRest(),
            images=["scorpion_right"]
        ))
        for i in SND_MENIAJEM_NOGI:
            self.pool("name").append(i)
        
        self.tasks.append(BaseTask(
            caption=self.caption + "\n(левая рука)",
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images
        ))
        self.pool("float").append("descr_scorpion_vse_mushci")
        self.pool("float").append("descr_scorpion")
        self.pool("end").append("i_opustilis'_na_koleni")
        for i in SND_RASSLABILIS + SND_EXHALE + SND_ZAKONCHILI_DALSHE + SND_COMPLETION_OTHERS:
            self.pool("end").append(i)

