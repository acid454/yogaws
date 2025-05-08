#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tadasana.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask, SoundPool
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest


class Tadasana(BaseAsana):
    def __init__(self):
        BaseAsana.__init__(self, name="tadasana", caption="Тадасана")
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=45))

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=["tadasana01", "tadasana02"]))
        
        self.pool("start").append("name_tadasana")
        self.pool("start").append("begin_nachinaete_s_poloshenija_stoja")
        self.pool("start").append("begin_vstaem_na_kovrik")
        self.pool("start").append("begin_tadasana")
        self.pool("start").append("begin_vstaem_rovno_ruki_vdol'_tulovisha")

        self.pool("float").append("descr_tadasana_on_begin")
        self.pool("float").append(None)

        self.pool("end").append("_hlopok_")
        self.pool("end").append("poehali")
