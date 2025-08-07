#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  vitjashenie_vverh.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork


class VitjashenieVverh(BaseAsana):
    def __init__(self, **kwargs):
        BaseAsana.__init__(self, name="vitjashenie_vverh", caption="Вытягивание вверх")
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=25))
        self.update_props(kwargs)

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=["upr_vitjashenie_vverh1", "upr_vitjashenie_vverh2"]))
        self.pool("name").append("vitiagivaemsia_vverh")
        self.pool("name").append("upr_podnimaemsia_vverh1")
        self.pool("name").append("upr_podnimaemsia_vverh2")
        self.pool("name").append("upr_vitajshenie_vverh1")
        self.pool("name").append("upr_vitajshenie_vverh2")
        self.pool("name").append("upr_vitajshenie_vverh3_na_vdohe")
        
        self.pool("continue").append("descr_vitashenie_vverh1")
        self.pool("continue").append("descr_vitashenie_vverh2")
        self.pool("continue").append("descr_vitashenie_vverh3")
        self.pool("continue").append("descr_vitashenie_vverh4")
        self.pool("continue").append("descr_vitashenie_vverh5")
        self.pool("continue").append("descr_vitashenie_vverh6")