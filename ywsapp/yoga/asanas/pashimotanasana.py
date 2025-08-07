#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pashimotanasana.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import *


class Pashimotanasana(BaseAsana):
    def __init__(self, **kwargs):
        super().__init__(name="pashimotanasana", caption="Пашчимоттанасана")
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=12))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=120))
        self.update_props(kwargs)
        
        self.tasks.append(BaseTask(
            caption=self.caption + " (подготовка)",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=[f"pashimotanasana{x}" for x in range(1,3)]
        ))
        self.pool("start").append(NOGI_PERED_SOBOI)
        self.pool("name").append("name_pashimotanasana1")
        self.pool("name").append("name_pashimotanasana2")
        self.pool("name").append("name_pashimotanasana4")
        self.pool("end").append("enter_pashimotanasana1")
        self.pool("end").append("enter_pashimotanasana2")
        self.pool("end").append("enter_pashimotanasana3")
        self.pool("end").append("enter_pashimotanasana4")

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images
        ))
        self.pool("start").append("descr_pashimotanasana1")
        self.pool("start").append("descr_pashimotanasana2")
        self.pool("start").append("descr_pashimotanasana3")
        self.pool("float").append("common_podrasslabitsia")
        self.pool("float").append("common_ne_pererastjagivaem_mushci")
        self.pool("float").append("common_rasslabit'_lico_plechi")
        self.pool("float").append("common_delaem_plavno")
        self.pool("float").append("common_prirost_navikov")
        self.pool("float").append("common_telo_prosedajet")
        self.pool("float").append("common8")
        self.pool("float").append("common9")
        self.pool("float").append("common11")
        self.pool("float").append("common_delaite_to_chto_poluchaetsia")
        self.pool("float").append("common_duhanie_rovnoe_estestvennoe")
        self.pool("float").append("common_sbrasivaete_napriajenie_s_litca_s_shivota")
        self.pool("float").append("common_isportit'_usediem")
        self.pool("end").append(SND_COMPLETION_OTHERS + SND_ZAKONCHILI_DALSHE)
