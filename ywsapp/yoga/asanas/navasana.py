#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  navasana.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import *


class Navasana(BaseAsana):
    def __init__(self, **kwargs):
        super().__init__(name="navasana", caption="Навасана")
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=10))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=45))
        self.update_props(kwargs)
        
        self.tasks.append(BaseTask(
            caption=self.caption + "\n(подготовка)",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=[f"navasana{x}" for x in range(1,5)]
        ))
        self.pool("name").append("name_navasana1")
        self.pool("name").append("name_navasana2")
        self.pool("name").append("name_navasana3")
        self.pool("name").append("name_navasana4")
        self.pool("name").append("name_navasana5")
        self.pool("end").append("enter_navasana1")
        self.pool("end").append("enter_navasana2")

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images
        ))
        self.pool("start").append(FIKSIRUEM)
        self.pool("float").append("descr_navasana1", float_on_start = True)
        self.pool("float").append("descr_navasana3", float_on_start = True)
        self.pool("float").append("descr_navasana4", float_on_start = True)
        self.pool("float").append("descr_navasana2", float_on_start = True)
        self.pool("float").append("descr_navasana5", float_on_start = True)
        self.pool("float").append("common_duhanie_rovnoe_estestvennoe")
        self.pool("float").append("common_sledim_za_geometriei_kak_zadumanno")
        self.pool("float").append("common_vsie_budet_horosho")
        self.pool("float").append("common_uluchshenie_krovosnabshenia_pozvonochnika")
        self.pool("end").append(SND_RASSLABILIS + SND_EXHALE + SND_ZAKONCHILI_DALSHE)
