#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  breath.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  Асаны-таски для упражнений Кегеля
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeRest, MetronomeWork
from snd_pools import *

class Breath(BaseAsana):
    def __init__(self, _inhale=True, action_text=None, **kwargs):
        self.is_inhale = _inhale
        if action_text is None:
            action_text = 'вдох' if self.is_inhale else 'выдох'
        super().__init__(name="breath", caption="%s"%(action_text))
        self.properties.append(IntProperty(caption="время", short="tm_main", default=8))
        self.update_props(kwargs)

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            images=["chakra_PNG132"],
            metronome = MetronomeWork() if self.is_inhale else MetronomeRest()
        ))