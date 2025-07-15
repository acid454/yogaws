#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  markatasana.py
#  
#  Copyright 2025 Repnikov Dmitry <acid454@yoga7>
#  

import random
from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import *


class Markatasana(BaseAsana):
    def __init__(self, **kwargs):
        super().__init__(name="markatasana", caption="Маркатасана")
        self.properties.append(IntProperty(caption="подготовка", short="tm_enter", default=11))
        self.properties.append(IntProperty(caption="циклов", short="cycles_count", default=5))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=7))
        self.update_props(kwargs)
        
        self.tasks.append(BaseTask(
            caption=self.caption + " (подготовка)",
            property=self.tm_enter,
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
                self.pool("continue").append("descr_markatasana_left")
            self.pool("end").append(SND_MENIAJEM_NOGI)
            self.pool("end").append("i potom rovno na oborot")
            
            self.tasks.append(BaseTask(
                caption=self.caption + "\nвправо",
                property=self.tm_main,
                metronome=MetronomeWork(),
                images=[f"markatasana_right{j}" for j in range(1,3)]
            ))
            self.pool("end").append(SND_MENIAJEM_NOGI)
            self.pool("end").append("i potom rovno na oborot")
            

        # Ignore enter and first cycle tasks
        for t in self.tasks[2:]:
            self.setup_float(t)
        self.setup_end_pool()

    def setup_float(self, t):
        t.pool("float").append(None)
        t.pool("float").append("common_delaem_vse_ne_toropias'")
        t.pool("float").append("common_potianut'_pojasnichnue_mishzi_zameret'")
        t.pool("float").append("descr_markatasana_koleni_stremiatsia_opustitsia_na_pol")
        t.pool("float").append("common_mjagkoe_bezobidnoe_uprashnenie_raskrepostit'_pojasnicu")

    def setup_end_pool(self):
        self.pool("end").clear()
        self.pool("end").append(SND_ZAKONCHILI_DALSHE + SND_COMPLETION_OTHERS)


class MarkatasanaWithLegs(Markatasana):
    def __init__(self, **kwargs):
        super().__init__()
        self.cycles_count.caption = "циклов коленей"
        self.properties.append(IntProperty(caption="ноги перед собой", short="tm_legs", default=5))
        self.properties.append(IntProperty(caption="циклов скруток", short="cycles_twist", default=3))
        self.properties.append(IntProperty(caption="смена ног", short="tm_swap", default=3))
        self.update_props(kwargs)

        self.pool("end").clear()


        self.tasks.append(BaseTask(
            caption=self.caption + " (подготовка)",
            property=self.tm_legs,
            metronome=MetronomeRest(),
            images=["markatasana_leg_right_up"]
        ))
        self.pool("start").append(NOGI_PERED_SOBOI)
        self.pool("continue").append("enter_markatasana_stavim_nogi")
        self.pool("end").append("i_potianulis'_vlevo")

        stopi_do_kovrika_rand = random.randint(1, self.cycles_twist.value - 1) + random.randint(0,1)/2
        for i in range(self.cycles_count.value):
            self.tasks.append(BaseTask(
                caption=self.caption + "\nвлево",
                property=self.tm_main,
                metronome=MetronomeWork(),
                images=["markatasana_leg_right_left"]
            ))
            
            if i == stopi_do_kovrika_rand:
                self.pool("float").append("markatasana_stopi_do_kovrika")
            else:
                self.setup_float(self.tasks[-1])
            self.task_swap_legs()

            self.tasks.append(BaseTask(
                caption=self.caption + "\nвправо",
                property=self.tm_main,
                metronome=MetronomeWork(),
                images=["markatasana_leg_left_right"]
            ))
            if i + 0.5 == stopi_do_kovrika_rand:
                self.pool("float").append("markatasana_stopi_do_kovrika")
            else:
                self.setup_float(self.tasks[-1])
            self.task_swap_legs()
        
        del self.tasks[-1]
        self.setup_end_pool()
        

    def task_swap_legs(self):
        self.tasks.append(BaseTask(
            caption=self.caption + "\nсмена ног",
            property=self.tm_swap,
            metronome=MetronomeRest(),
            images=["markatasana_leg_left_up"]
        ))
        self.pool("start").append(SND_MENIAJEM_NOGI)
            


