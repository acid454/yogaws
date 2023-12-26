#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  most.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import *


class Most(BaseAsana):
    def __init__(self, **kwargs):
        super().__init__(name="most", caption="Чакрасана")
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=17))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=35))
        self.properties.append(IntProperty(caption="выход, компенсация", short="tm_exit", default=8))
        self.update_props(kwargs)
        
        self.tasks.append(BaseTask(
            caption=self.caption + " (подготовка)",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=[f"most{x}" for x in range(1,7)]
        ))
        self.pool("start").append("name_chakrasana1")
        self.pool("start").append("name_chakrasana2")
        self.pool("continue").append("enter_most1")
        self.pool("continue").append("enter_most2")
        self.pool("end").append("enter_most_so_vdohom_vverh")
        self.pool("end").append("enter_most_smukaem_lopatki_i_vitalkivaemsia")

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images
        ))
        self.pool("start").append("descr_most1")
        self.pool("start").append(None)
        self.pool("float").append("descr_most2")
        self.pool("float").append("descr_most3")
        self.pool("float").append("common3")
        self.pool("float").append("common4")
        self.pool("float").append("common5_v_vitalkivanii")
        self.pool("float").append("common6")
        self.pool("float").append("common7")
        self.pool("float").append("common8")
        for i in SND_EXHALE + SND_RASSLABILIS:
            self.pool("end").append(i)

        self.tasks.append(BaseTask(
            caption=self.caption + " (выход, компенсация)",
            property=self.tm_exit,
            metronome=MetronomeRest(),
            images=[f"most_compensate{x}" for x in range(1,4)]
        ))
        self.pool("start").append("delaem_kompensaciju")
        self.pool("start").append("most_kompensacija")
        self.pool("end").append("otlichno")
        for i in SND_ZAKONCHILI_DALSHE:
            self.pool("end").append(i)