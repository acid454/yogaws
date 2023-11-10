#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  baddha_konasana.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeRest, MetronomeWork
from snd_pools import SND_ZAKONCHILI_DALSHE


class BaddhaKonasana(BaseAsana):
    def __init__(self, **kwargs):
        super().__init__(name="baddha_konasana", caption="Баддха Конасана")
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=10))
        self.properties.append(IntProperty(caption="прогиб вперёд", short="tm_progib", default=50))
        self.properties.append(IntProperty(caption="переход", short="tm_legs_change", default=5))
        self.properties.append(IntProperty(caption="ноги к себе", short="tm_squared", default=50))
        self.update_props(kwargs)

        self.tasks.append(BaseTask(
            caption=self.caption + "\n(подготовка, ноги вытянуты)",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=["baddha_konasana_romb1", "baddha_konasana_romb2"]
        ))
        self.pool("start").append("name_baddha_konasana1")
        self.pool("start").append("name_baddha_konasana2")
        self.pool("continue").append("descr_baddha_konasana_tjanemsia_vpered")

        self.tasks.append(BaseTask(
            caption=self.caption + "\n(прогиб вперёд)",
            property=self.tm_progib,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images))
        self.pool("float").append("common3")
        self.pool("float").append("descr_baddha_konasana_pokachatsia")
        self.pool("float").append("common7")
        self.pool("float").append("common8")
        self.pool("float").append("common9")
        self.pool("float").append("common10")
        self.pool("float").append("common11")
        self.pool("float").append("common12")
        self.pool("float").append("common_ne_pererastjagivaem_mushci")
        self.pool("float").append("common_rasslabit'_lico_plechi")
        self.pool("float").append("common_akcentiruite_vidohi")

        self.tasks.append(BaseTask(
            caption=self.caption + "\n(подтягиваем ноги к себе)",
            property=self.tm_legs_change,
            metronome=MetronomeRest(),
            images=["baddha_konasana1", "baddha_konasana2"]
        ))
        self.pool("start").append("nogi_blishe")
        self.pool("start").append("enter_baddha_konasana_overlapse")    # overlapse

        self.tasks.append(BaseTask(
            caption=self.caption + "\n(шевелим коленями)",
            property=self.tm_squared,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images))
        self.pool("start").append("descr_baddha_konasana_shevelim_kolenijami")
        self.pool("float").append("common3")
        self.pool("float").append("descr_baddha_konasana_pokachatsia")
        self.pool("float").append("common7")
        self.pool("float").append("common8")
        self.pool("float").append("common9")
        self.pool("float").append("common10")
        self.pool("float").append("common11")
        self.pool("float").append("common12")

        for i in SND_ZAKONCHILI_DALSHE:
            self.pool("end").append(i)