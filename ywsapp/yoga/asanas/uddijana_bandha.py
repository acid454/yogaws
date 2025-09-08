#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  uddijana_bandha.py
#  
#  Copyright 2025 Repnikov Dmitry <acid454@yoga7>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import *
from asanas.kapalabhati import Kapalabhati


class UddijanaBandha(BaseAsana):
    def __init__(self, **kwargs):
        super().__init__(name="uddijana_bandha", caption="Уддияна Бандха")
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=16))
        self.properties.append(IntProperty(caption="циклов", short="cycles", default=3))
        self.properties.append(IntProperty(caption="выдох", short="tm_exhale", default=10))
        self.properties.append(IntProperty(caption="фиксация", short="tm_main", default=30))
        self.properties.append(IntProperty(caption="отдых", short="tm_exit", default=17))
        self.update_props(kwargs)
        
        self.tasks.append(BaseTask(
            caption=self.caption + "\n(подготовка)",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=["uddijana_bandha_seli1", "uddijana_bandha_seli2"]
        ))
        self.pool("name").append("name_uddijana_bandha1")
        self.pool("name").append("name_uddijana_bandha2")
        #self.pool("end").append(f"inhale{x}" for x in range(1,8))


        for _ in range(self.cycles.value):
            self.tasks.append(BaseTask(
                caption=self.caption + "\n(выдох)",
                property=self.tm_exhale,
                metronome=MetronomeRest(),
                images=["uddijana_bandha_exhale1"]
            ))
            self.pool("name").append(SND_S_VIDOHOM_VNIZ)
            self.pool("end").append(SND_PODNIMAEMSIA)


            self.tasks.append(BaseTask(
                caption=self.caption + "\n(фиксация)",
                property=self.tm_main,
                metronome=MetronomeWork(),
                images=["uddijana_bandha1"]
            ))
            self.pool("name").append(FIKSIRUEM)
            self.pool("end").append(SND_COMPLETION_OTHERS)

            self.tasks.append(BaseTask(
                caption=self.caption + "\n(отдых)",
                property=self.tm_exit,
                metronome=MetronomeRest(),
                images=self.task(self.tm_prepare).images
            ))
            self.pool("name").append("dushim1")
            self.pool("name").append(SND_RASSLABILIS)
        self.tasks[-1].pool("end").append(SND_ZAKONCHILI_DALSHE)

    def build(self, workout, _set):
        super().build(workout, _set)
        prev_asana = workout.prev_item(self)
        if isinstance(prev_asana, Kapalabhati):
            self.tm_prepare.default = 3
