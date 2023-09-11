#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sobaka_mordoi_vverh.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest

class SobakaMordoiVverh(BaseAsana):
    def __init__(self):
        BaseAsana.__init__(self, name="sobaka_mordoi_vverh", caption="собака мордой вверх")
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=40))

        # ToDo: transition time
        
        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.get_prop("tm_main"),
            metronome=MetronomeWork()
        ))
