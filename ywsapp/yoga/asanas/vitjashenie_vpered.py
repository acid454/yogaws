#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  vitjashenie_vpered.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork


class VitjashenieVpered(BaseAsana):
    def __init__(self, **kwargs):
        BaseAsana.__init__(self, name="vitjashenie_vpered", caption="Наклон вперёд")
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=13))
        self.update_props(kwargs)

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=["upr_vitjashenie_vpered1", "upr_vitjashenie_vpered2"]))
        
        self.pool("name").append("upr_potjanulis_vpered1")
        self.pool("name").append("upr_potjanulis_vpered2")
        self.pool("name").append("upr_potjanulis_vpered3")
        self.pool("name").append("upr_potjanulis_vpered4")
        self.pool("name").append("upr_potjanulis_vpered5")
        self.pool("name").append("upr_potjanulis_vpered6")
        self.pool("name").append("upr_potjanulis_vpered7")
        
        self.pool("continue").append("descr_potjanulis_vpered1")
        self.pool("continue").append("descr_potjanulis_vpered2")
        self.pool("continue").append("descr_potjanulis_vpered3")
        self.pool("continue").append("descr_potjanulis_vpered4")
        self.pool("continue").append("descr_potjanulis_vpered5")
        self.pool("continue").append("common_dushim_derzim_t'anemsia")
        self.pool("continue").append("common_tianemsia_2x")
        