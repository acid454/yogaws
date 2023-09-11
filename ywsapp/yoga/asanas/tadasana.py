#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tadasana.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest


class Tadasana(BaseAsana):
    def __init__(self):
        BaseAsana.__init__(self, name="tadasana", caption="Тадасана")
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=40))

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork()
        ))
