#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tadasana.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeRest


class Tadasana(BaseAsana):
    def __init__(self, **kwargs):
        super().__init__(self, name="tadasana", caption="Тадасана")
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=45))
        self.update_props(kwargs)

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeRest(),
            images=["tadasana01", "tadasana02"]))
        
        self.pool("name").append("begin_nachinaete_s_poloshenija_stoja")
        self.pool("name").append("begin_vstaem_na_kovrik")
        self.pool("name").append("name_tadasana")
        self.pool("name").append("begin_tadasana")

        self.pool("float").append("begin_vstaem_rovno_ruki_vdol'_tulovisha")
        self.pool("float").append("descr_tadasana_on_begin")
        self.pool("float").append(None)

        self.pool("end").append("_hlopok_")
        self.pool("end").append("poehali1")
        self.pool("end").append("poehali2")
        self.pool("end").append("poehali3")
        self.pool("end").append("poehali_nu_chto1")
        self.pool("end").append("poehali_nu_chto2")
