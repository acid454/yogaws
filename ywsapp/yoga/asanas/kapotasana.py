#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kapotasana.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeRest, MetronomeWork
from snd_pools import *

class Kapotasana(BaseAsana):
    def __init__(self, **kwargs):
        super().__init__(name="kapotasana", caption="Капотасана")
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=13))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=25))
        self.properties.append(IntProperty(caption="смена ног", short="tm_swap", default=13))
        #self.properties.append(IntProperty(caption="выход", short="tm_exit", default=4))
        self.update_props(kwargs)

        self.tasks.append(BaseTask(
            caption=self.caption + "\nлевая нога, подготовка",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=["kapotasana_left1"]
        ))
        self.pool("name").append("name_kapotasana1")
        self.pool("name").append("name_kapotasana2")
        self.pool("name").append("name_kapotasana3")
        self.pool("continue").append("left_side1")
        self.pool("continue").append("left_side2")

        self.tasks.append(BaseTask(
            caption=self.caption + "\nлевая нога",
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images
        ))
        self.kapotasana_common_sounds()
        self.pool("end").append("vernulis'1")
        self.pool("end").append("vernulis'2")
        for i in SND_ZAKONCHILI_DALSHE:
            self.pool("end").append(i)
        
        self.tasks.append(BaseTask(
            caption=self.caption + "\nправая нога, подготовка",
            property=self.tm_swap,
            metronome=MetronomeRest(),
            images=["kapotasana_right1"]
        ))
        for i in SND_MENIAJEM_NOGI + SND_NA_DRUGUJU_STORONU:
            self.pool("start").append(i)

        self.tasks.append(BaseTask(
            caption=self.caption + "\nправая нога",
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images
        ))
        self.kapotasana_common_sounds()
        """
        self.tasks.append(BaseTask(
            caption=self.caption + "\nвыход",
            property=self.tm_exit,
            metronome=MetronomeRest(),
            images=self.tasks[-1].images
        ))
        for snd in SND_ZAKONCHILI_DALSHE:
            self.pool("end").append(snd)
        """

    def kapotasana_common_sounds(self):
        self.pool("float").append("descr_kapotasana")
        self.pool("float").append("common9")
        self.pool("float").append("common12")
        self.pool("float").append("common1")
        self.pool("float").append("common3")
        self.pool("float").append("common4")
        self.pool("float").append("common5_v_vitalkivanii")
        self.pool("float").append("common6")
        self.pool("float").append("common7")
        self.pool("float").append("common8")
        self.pool("float").append("common10")
