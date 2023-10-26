#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  nogi_k_rukam.py
#  Объединяет прыжок и подход к рукам
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask, SoundPool
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest


class Nogi_k_Rukam(BaseAsana):
    def __init__(self, **kwargs):
        BaseAsana.__init__(self, name="nogi_k_rukam", caption="Подходим ногами к рукам")
        self.properties.append(IntProperty(caption="время выполнения", short="tm_main", default=5))
        self.update_props(kwargs)

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=["nogi_k_rukam1"]))
        
        self.pool("start").append("i_podoshli_nogami_k_rukam")

class Prizhok_k_Rukam(BaseAsana):
    def __init__(self, **kwargs):
        BaseAsana.__init__(self, name="prizhok_k_rukam", caption="Прыжок к ладоням рук")
        self.properties.append(IntProperty(caption="время выполнения", short="tm_main", default=2))

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=["prizhok_k_rukam"]))
        
        self.pool("start").append("upr_prizhok_k_rukam1")
        self.pool("start").append("upr_prizhok_k_rukam2")