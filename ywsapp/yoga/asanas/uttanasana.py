#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  uttanasana.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest


class Uttanasana(BaseAsana):
    def __init__(self):
        BaseAsana.__init__(self, name="uttanasana", caption="Уттанасана")
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=40))
        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.get_prop("tm_main"),
            metronome=MetronomeWork()
        ))

class Uttanasana_ruki_v_zamke(BaseAsana):
    def __init__(self):
        BaseAsana.__init__(self, name="uttanasana_ruki_v_zamke", caption="Уттанасана (руки в замке)")
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=40))
        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.get_prop("tm_main"),
            metronome=MetronomeWork()
        ))