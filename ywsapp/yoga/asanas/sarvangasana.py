#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sarvangasana.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import *


class Sarvangasana(BaseAsana):
    def __init__(self, **kwargs):
        super().__init__(name="sarvangasana", caption="Сарвангасана")
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=11))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=60))
        self.properties.append(IntProperty(caption="выход", short="tm_exit", default=7))
        self.update_props(kwargs)
        
        self.tasks.append(BaseTask(
            caption=self.caption + "\n(подготовка)",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=["sarvangasana1"]
        ))
        self.pool("name").append("name_sarvangasana1")
        self.pool("continue").append("enter_sarvangasana1")
        self.pool("end").append("i_pristavliajem_ruki_k_spine")
        self.pool("end").append(None)

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images
        ))
        self.pool("float").append("common_duhanie_estestvennoe_long")
        self.pool("float").append("common_delaite_to_chto_poluchaetsia")
        self.pool("float").append("common_dlya_spinu_i_pozvonochnika")
        self.pool("float").append("common_prirost_navikov")
        self.pool("float").append("common_samokontrol'_primenit'_k_sebe")
        self.pool("float").append("common3")
        self.pool("float").append("common12")
        self.pool("float").append("common_duhanie_rovnoe_estestvennoe")

        self.tasks.append(BaseTask(
            caption=self.caption + "\nвыход",
            property=self.tm_exit,
            metronome=MetronomeRest(),
            images=self.tasks[-1].images
        ))
        self.pool("start").append(SND_OPUSTILIS)
        self.pool("end").append(SND_ZAKONCHILI_DALSHE)