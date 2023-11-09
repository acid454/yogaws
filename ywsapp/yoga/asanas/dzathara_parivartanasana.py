#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dzathara_parivartanasana.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import AsanaLegsStayUp, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import *


class Dzathara_Parivartanasana(AsanaLegsStayUp):
    def __init__(self, **kwargs):
        super().__init__(name="dzathara_parivartanasana", caption="Джатхара Паривартанасана")
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=7))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=50))
        self.properties.append(IntProperty(caption="переход", short="tm_swap", default=15))
        self.properties.append(IntProperty(caption="выход", short="tm_exit", default=6))
        self.update_props(kwargs)

        self.tasks.append(BaseTask(
            caption=self.caption + "\nлевый бок, подготовка",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=[f"dzathara_parivartanasana_left{x}" for x in range(1,3)]
        ))
        self.pool("start").append("upr_razvodim_ruki_v_storoni")
        self.pool("continue").append("upr_razvorot_vlevo")

        self.tasks.append(BaseTask(
            caption=self.caption + "\nлевый бок",
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images
        ))
        self.dzathara_float_sounds()
        self.pool("end").append("otlichno")
        self.pool("end").append("vernulis'1")
        self.pool("end").append("vernulis'2")
        self.pool("end").append("vernulis'_v_ishodnuju")

        self.tasks.append(BaseTask(
            caption=self.caption + "\nправый бок, подготовка",
            property=self.tm_swap,
            metronome=MetronomeRest(),
            images=["nogi_vverh_ruki_v_storoni", "dzathara_parivartanasana_right1", "dzathara_parivartanasana_right2"]
        ))
        self.pool("start").append("podniali_nogi")
        for snd in SND_MENIAJEM_NOGI + SND_NA_DRUGUJU_STORONU:
            self.pool("continue").append(snd)

        self.tasks.append(BaseTask(
            caption=self.caption + "\nправый бок",
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=["dzathara_parivartanasana_right1", "dzathara_parivartanasana_right2"]
        ))
        self.dzathara_float_sounds()

        self.tasks.append(BaseTask(
            caption=self.caption + "\nвыход",
            property=self.tm_exit,
            metronome=MetronomeRest(),
            images=["nogi_vverh_ruki_v_storoni"]
        ))
        self.pool("start").append("podniali_nogi")

    def dzathara_float_sounds(self):
        self.pool("float").append("descr_dzathara_parivartanasana")
        self.pool("float").append("common4")
        self.pool("float").append("common7")
        self.pool("float").append("common8")
        self.pool("float").append("common9")
        self.pool("float").append("common10")
        self.pool("float").append("common11")
        self.pool("float").append("common12")
        self.pool("float").append("common_potianut'_pojasnichnue_mishzi_zameret'")
        self.pool("float").append("common_delaite_to_chto_poluchaetsia")