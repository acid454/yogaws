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


class Planka(BaseAsana):
    def __init__(self):
        BaseAsana.__init__(self, name="planka", caption="Планка")
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=4))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=40))
        
        self.tasks.append(BaseTask(
            caption=self.caption + "(подготовка)",
            property=self.get_prop("tm_prepare"),
            metronome=MetronomeRest(),
            images=["planka1", "planka2"]
        ))

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.get_prop("tm_main"),
            metronome=MetronomeWork(),
            images=["planka1", "planka2"]
        ))
