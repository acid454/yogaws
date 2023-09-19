#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sobaka_mordoi_vverh.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork

class SobakaMordoiVverh(BaseAsana):
    def __init__(self, transition_type=None):
        BaseAsana.__init__(self, name="sobaka_mordoi_vverh", caption="собака мордой вверх")
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=40))

        # ToDo: transition time
        
        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=["sobaka_mordoi_vverh1", "sobaka_mordoi_vverh2"]
        ))
        
        self.pool("continue").append("name_sobaka_mordoi_vverh1")
        self.pool("continue").append("name_sobaka_mordoi_vverh2_vikatilis'")
        self.pool("continue").append("name_sobaka_mordoi_vverh3_i_vikatilis'")
        if transition_type == "up":
            self.pool("start").append("upr_podnimaemsia_vverh1")
            self.pool("start").append("upr_podnimaemsia_vverh2")
            self.pool("start").append("so_vdohom_vverh1")
            self.pool("start").append("so_vdohom_vverh2")
            self.pool("start").append("trans_gorka_sobaka_mordoi_vverh1_up")
            self.pool("start").append("trans_gorka_sobaka_mordoi_vverh2_up")
            self.pool("start").append("trans_vstaem_na_noski_puskaem_volnu")
        elif transition_type == "down":
            self.pool("start").append("delaem_nirok")
            self.pool("start").append("otzhimaetes'")
            self.pool("start").append("cherez_niz")

