#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  markatasana.py
#  
#  Copyright 2025 Repnikov Dmitry <acid454@yoga7>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import SND_ZAKONCHILI_DALSHE, SND_COMPLETION_OTHERS, SND_MENIAJEM_NOGI


class Markatasana(BaseAsana):
    def __init__(self, **kwargs):
        super().__init__(name="markatasana", caption="Маркатасана")
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=9))
        self.properties.append(IntProperty(caption="циклов", short="cycles_count", default=7))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=15))
        self.update_props(kwargs)
        
        self.tasks.append(BaseTask(
            caption=self.caption + " (подготовка)",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=["markatasana base"]
        ))
        self.pool("name").append("name_markatasana_delaem_markatasanu")
        self.pool("continue").append("enter_markatasana")

        for i in range(self.cycles_count.value):
            self.tasks.append(BaseTask(
                caption=self.caption + "\nвлево",
                property=self.tm_main,
                metronome=MetronomeWork(),
                images=[f"markatasana_left{j}" for j in range(1,3)]
            ))

            if i == 0:
                self.pool("continue+").append("descr_markatasana_left")
            
            self.pool("end").append(SND_MENIAJEM_NOGI)
            self.pool("end").append("i potom rovno na oborot")
            
            self.tasks.append(BaseTask(
                caption=self.caption + "\nвправо",
                property=self.tm_main,
                metronome=MetronomeWork(),
                images=[f"markatasana_right{j}" for j in range(1,3)]
            ))

            if i < self.cycles_count.value - 1:
                self.pool("end").append(SND_MENIAJEM_NOGI)
                self.pool("end").append("i potom rovno na oborot")
            

        # Ignore enter and first cycle tasks
        for t in self.tasks[2:]:
            t.pool("float").append("common_delaem_vse_ne_toropias'")
            t.pool("float").append("common_potianut'_pojasnichnue_mishzi_zameret'")
            t.pool("float").append("descr_markatasana_koleni_stremiatsia_opustitsia_na_pol")
            t.pool("float").append("common_mjagkoe_bezobidnoe_uprashnenie_raskrepostit'_pojasnicu")

        self.pool("end").clear()
        self.pool("end").append(SND_ZAKONCHILI_DALSHE + SND_COMPLETION_OTHERS)
