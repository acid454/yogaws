#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  utkatasana.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import *


class Utkatasana(BaseAsana):
    def __init__(self, **kwargs):
        super().__init__(name="most", caption="Уткатасана")
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=9))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=40))
        self.update_props(kwargs)
        
        self.tasks.append(BaseTask(
            caption=self.caption + " (подготовка)",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=[f"utkatasana{x}" for x in range(1,4)]
        ))
        self.pool("name").append("name_utkatasana1")
        self.pool("name").append("name_utkatasana2")
        self.pool("name").append("name_utkatasana3")
        self.pool("continue").append("enter_utkatasana1", overlapse = True)
        self.pool("continue").append("enter_utkatasana2", overlapse = True)
        self.pool("continue").append("enter_utkatasana3")


        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images
        ))
        self.pool("continue").append("descr_utkatasana")
        self.pool("float").append("common_derzimsia_dushim")
        self.pool("float").append("common_dushim_derzim_t'anemsia")
        self.pool("float").append("common1")
        self.pool("float").append("common3")
        self.pool("float").append("common4_dushim_dershimsia")
        self.pool("float").append("common6")
        self.pool("float").append("common7")
        self.pool("float").append("common10")
        self.pool("float").append("common_delaem_medlenno_pomogaja_duhaniem")
        self.pool("float").append("common_duhanie_rovnoe_estestvennoe")
        self.pool("float").append("common_sledim_za_geometriei_kak_zadumanno")
        self.pool("float").append("common_tianemsia_intensovno_vverh")
        self.pool("float").append("common_ne_zabuvaem_raspredeliat'_ravnovesie")
        self.pool("end").append(SND_EXHALE + SND_RASSLABILIS + SND_ZAKONCHILI_DALSHE)
