#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gorka.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest

class GorkaBase(BaseAsana):
    def __init__(self):
        BaseAsana.__init__(self, name="gorka", caption="Горка")
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=40))
        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=["gorka1", "gorka2", "gorka3", "gorka4"]
        ))

class GorkaNormal(GorkaBase):
    def __init__(self):
        GorkaBase.__init__(self)
        self.properties.insert(0, IntProperty(caption="подготовка", short="tm_prepare", default=4))
        self.tasks.append(BaseTask(
            caption=self.caption + " (подготовка)",
            property=self.tm_prepare,
            metronome=MetronomeRest()
        ))