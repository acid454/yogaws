#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dzathara_parivartanasana.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import SND_NA_DRUGUJU_STORONU, SND_VERNULIS, SND_COMPLETION_OTHERS, SND_I_DALSHE
from plug import Plug


class Dzathara_Parivartanasana(BaseAsana):
    def __init__(self, **kwargs):
        super().__init__(name="dzathara_parivartanasana", caption="Джатхара Паривартанасана")
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=13))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=50))
        self.properties.append(IntProperty(caption="переход", short="tm_swap", default=17))
        self.properties.append(IntProperty(caption="выход", short="tm_exit", default=6))
        self.update_props(kwargs)
        self.preview_img = "dzathara_parivartanasana_right1"

        self.tasks.append(BaseTask(
            caption=self.caption + "\nлевый бок, подготовка",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=["nogi_vverh_ruki_v_storoni"]
        ))
        self.pool("start").append("podniali_nogi", mandatory = True)
        self.pool("name").append("upr_razvodim_ruki_v_storoni")
        self.pool("continue").append("upr_razvorot_vlevo", mandatory = True)

        self.tasks.append(BaseTask(
            caption=self.caption + "\nлевый бок",
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=[f"dzathara_parivartanasana_left{x}" for x in range(1,3)]
        ))
        self.dzathara_float_sounds()

        self.tasks.append(BaseTask(
            caption=self.caption + "\nправый бок, подготовка",
            property=self.tm_swap,
            metronome=MetronomeRest(),
            images=["nogi_vverh_ruki_v_storoni", "dzathara_parivartanasana_right1", "dzathara_parivartanasana_right2"]
        ))
        self.pool("start").append("podniali_nogi", mandatory = True)
        self.pool("continue").append(SND_NA_DRUGUJU_STORONU, mandatory = True)

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
        self.pool("start").append(SND_VERNULIS + SND_COMPLETION_OTHERS)
        self.pool("end").append(SND_I_DALSHE)


    def dzathara_float_sounds(self):
        self.pool("float").append("descr_dzathara_parivartanasana")
        self.pool("float").append("common4_dushim_dershimsia")
        self.pool("float").append("common7")
        self.pool("float").append("common8")
        self.pool("float").append("common9")
        self.pool("float").append("common10")
        self.pool("float").append("common11")
        self.pool("float").append("common12")
        self.pool("float").append("common_potianut'_pojasnichnue_mishzi_zameret'")
        self.pool("float").append("common_delaite_to_chto_poluchaetsia")
        self.pool("float").append("common_uluchshenie_krovosnabshenia_pozvonochnika")
        self.pool("float").append("common_isportit'_usediem")
    
    def build(self, workout, _set):
        super().build(workout, _set)
        if not issubclass(type(workout.prev_item(self)), Plug):
            self.task(self.tm_prepare).pool("start").append("vernuli_nogi_vverh", mandatory = True)