#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dhanurasana.py
#  
#  Copyright 2023 Repnikov Dmitry <acid454@yoga7>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import *


class Dhanurasana(BaseAsana):
    def __init__(self, **kwargs):
        super().__init__(name="dhanurasana", caption="Дханурасана")
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=13))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=30))
        self.properties.append(IntProperty(caption="выход", short="tm_exit", default=5))
        self.update_props(kwargs)
        
        self.tasks.append(BaseTask(
            caption=self.caption + " (подготовка)",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=[f"dhanusana{x}" for x in range(1,3)]
        ))
        self.pool("name").append("name_dhanurasana1")
        self.pool("name").append("name_dhanurasana2")
        self.pool("continue").append("enter_dhanurasana1")
        self.pool("end").append("i_tjanemsia_vverh")
        self.pool("end").append("so_vdohom_vverh1")
        self.pool("end").append("vitalkivaemsia_vverh")
        self.pool("end").append("upr_vitajshenie_vverh1")
        self.pool("end").append("upr_vitajshenie_vverh2")
        self.pool("end").append("upr_vitajshenie_vverh3_na_vdohe")

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images
        ))
        self.pool("float").append("common_dlya_spinu_i_pozvonochnika")
        self.pool("float").append("common_prirost_navikov")
        self.pool("float").append("common_samokontrol'_primenit'_k_sebe")
        self.pool("float").append("common12")
        self.pool("float").append("common3")
        self.pool("float").append("common_duhanie_rovnoe_estestvennoe")
        self.pool("float").append("common_sledim_za_geometriei_kak_zadumanno")
        self.pool("float").append("common_tianemsia_intensovno_vverh")
        self.pool("float").append("common_uluchshenie_krovosnabshenia_pozvonochnika")
        self.pool("end").append(SND_EXHALE + SND_RASSLABILIS)

        self.tasks.append(BaseTask(
            caption=self.caption + " (выход)",
            property=self.tm_exit,
            metronome=MetronomeRest(),
            images=self.tasks[-1].images
        ))
        self.pool("start").append(SND_OPUSTILIS)
        self.pool("end").append(SND_ZAKONCHILI_DALSHE)