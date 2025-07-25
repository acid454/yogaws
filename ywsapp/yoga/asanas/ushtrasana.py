#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ushtrasana.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import *


class Ushtrasana(BaseAsana):
    def __init__(self, **kwargs):
        super().__init__(name="ushtrasana", caption="Уштрасана")
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=13))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=45))
        self.properties.append(IntProperty(caption="выход", short="tm_exit", default=4))
        self.update_props(kwargs)
        
        self.tasks.append(BaseTask(
            caption=self.caption + "\n(подготовка)",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=["ushtrasana"]
        ))
        self.pool("name").append("name_ushtrasana1")
        self.pool("name").append("name_ushtrasana2")
        self.pool("name").append("name_ushtrasana3")
        self.pool("name").append("name_ushtrasana4")
        self.pool("name").append("name_ushtrasana5")
        self.pool("continue").append("enter_ushtrasana1")
        self.pool("continue").append("enter_ushtrasana2")
        self.pool("continue").append("enter_ushtrasana3")

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images
        ))
        self.pool("start").append("vitiagivaemsia_vverh")
        self.pool("start").append("i_mu_pot'anulis'")
        self.pool("start").append("i_tjanemsia_vverh")
        self.pool("start").append("vitalkivaemsia_vverh")
        self.pool("start").append("enter_most_so_vdohom_vverh")
        self.pool("start").append("upr_podnimaemsia_vverh1")
        self.pool("start").append("upr_podnimaemsia_vverh2")
        self.pool("start").append("vigibaemsia")
        self.pool("float").append("common_tianemsia_2x")
        self.pool("float").append("descr_ushtarsana_vitiagivaemsia")
        self.pool("float").append("descr_ushtarsana_pomnim_pro_pajasnitsu")
        self.pool("float").append("descr_most2")
        self.pool("float").append("common1")
        self.pool("float").append("common3")
        self.pool("float").append("common4")
        self.pool("float").append("common5_v_vitalkivanii")
        self.pool("float").append("common6")
        self.pool("float").append("common10")
        self.pool("float").append("common_delaem_medlenno_pomogaja_duhaniem")
        self.pool("float").append("common_duhanie_rovnoe_estestvennoe")
        self.pool("float").append("common_sledim_za_geometriei_kak_zadumanno")
        self.pool("float").append("common_povtoriaushiesia_pozu")
        self.pool("float").append("marichiasana_common_sledim_za_pozvonochnikom")
        self.pool("float").append("common_vsie_budet_horosho")
        self.pool("float").append("common_tianemsia_intensovno_vverh")
        self.pool("end").append(SND_EXHALE + SND_RASSLABILIS)

        self.tasks.append(BaseTask(
            caption=self.caption + "\nвыход",
            property=self.tm_exit,
            metronome=MetronomeRest(),
            images=self.tasks[-1].images
        ))
        self.pool("end").append(SND_COMPLETION_OTHERS + SND_ZAKONCHILI_DALSHE)