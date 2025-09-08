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
from snd_pools import SND_ZAKONCHILI_DALSHE, SND_COMPLETION_OTHERS, FIKSIRUEM, NOGI_PERED_SOBOI, SND_MENIAJEM_NOGI


class MarkatasanaBase(BaseAsana):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def setup_float(self, t):
        t.pool("float").append(None)
        t.pool("float").append(FIKSIRUEM, float_on_start = True)
        t.pool("float").append("common_delaem_vse_ne_toropias'")
        t.pool("float").append("common_potianut'_pojasnichnue_mishzi_zameret'", float_on_start = True)
        t.pool("float").append("descr_markatasana_koleni_stremiatsia_opustitsia_na_pol", float_on_start = True)
        t.pool("float").append("common_mjagkoe_bezobidnoe_uprashnenie_raskrepostit'_pojasnicu")
        t.pool("float").append("common_delaem_vse_ne_toropias'")
        t.pool("float").append("common_tianemsia_2x")
        t.pool("float").append("common_ubedilis'_chto_nam_horosho")
        t.pool("float").append("common1")
        t.pool("float").append("common7")
        t.pool("float").append("common_uluchshenie_krovosnabshenia_pozvonochnika")
        t.pool("float").append("common_glubokoe_proshivanie_tela")

    def setup_end_pool(self):
        self.pool("end").clear()
        self.pool("end").append(SND_ZAKONCHILI_DALSHE + SND_COMPLETION_OTHERS)


class Markatasana(MarkatasanaBase):
    def __init__(self, **kwargs):
        super().__init__(name="markatasana", caption="Маркатасана")
        self.properties.append(IntProperty(caption="подготовка", short="tm_enter", default=13))
        self.properties.append(IntProperty(caption="циклов", short="cycles_count", default=4))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=9))
        self.update_props(kwargs)
        
        self.tasks.append(BaseTask(
            caption=self.caption + " (подготовка)",
            property=self.tm_enter,
            metronome=MetronomeRest(),
            images=["markatasana_base1", "markatasana_base2"]
        ))
        self.pool("name").append("name_markatasana_delaem_markatasanu")
        self.pool("name").append("name_markatasana_variant")
        self.pool("continue").append("enter_markatasana")

        for i in range(self.cycles_count.value):
            self.tasks.append(BaseTask(
                caption=self.caption + "\nвлево",
                property=self.tm_main,
                metronome=MetronomeWork(),
                images=[f"markatasana_left{j}" for j in range(1,4)]
            ))

            if i == 0:
                self.pool("start").append("descr_markatasana_left")
            else:
                self.pool("float").append("descr_markatasana_zatragivaet_tazobedrennue", float_on_start = True, overlapse = True)

            self.pool("end").append(SND_MENIAJEM_NOGI)
            self.pool("end").append("i potom rovno na oborot")
            
            self.tasks.append(BaseTask(
                caption=self.caption + "\nвправо",
                property=self.tm_main,
                metronome=MetronomeWork(),
                images=[f"markatasana_right{j}" for j in range(1,4)]
            ))
            self.pool("end").append(SND_MENIAJEM_NOGI)
            self.pool("end").append("i potom rovno na oborot")
            

        # Ignore enter and first cycle tasks
        for t in self.tasks[2:]:
            self.setup_float(t)
        self.pool("end").clear()
        self.pool("end").append(SND_ZAKONCHILI_DALSHE + SND_COMPLETION_OTHERS)


class MarkatasanaWithLegs(MarkatasanaBase):
    def __init__(self, **kwargs):
        super().__init__(name="markatasana_legs", caption="Маркатасана")
        self.properties.append(IntProperty(caption="подготовка", short="tm_enter", default=6))
        self.properties.append(IntProperty(caption="циклов", short="cycles_count", default=4))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=9))
        self.properties.append(IntProperty(caption="смена ног", short="tm_swap", default=2))
        self.update_props(kwargs)

        self.tasks.append(BaseTask(
            caption=self.caption + " (подготовка)",
            property=self.tm_enter,
            metronome=MetronomeRest(),
            images=["markatasana_leg_right_up"]
        ))
        self.pool("start").append(NOGI_PERED_SOBOI, mandatory = True)
        self.pool("continue").append("enter_markatasana_stavim_nogi", mandatory = True)
        self.pool("end").append("i_potianulis'_vlevo", mandatory = True)

        stopi_do_kovrika_rand = random.randint(1, self.cycles_count.value - 1) + random.randint(0,1)/2
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
        self.pool("end").clear()
        self.pool("end").append(SND_ZAKONCHILI_DALSHE + SND_COMPLETION_OTHERS)
        

    def task_swap_legs(self):
        self.tasks.append(BaseTask(
            caption=self.caption + "\nсмена ног",
            property=self.tm_swap,
            metronome=MetronomeRest(),
            images=["markatasana_leg_left_up"]
        ))
        self.pool("start").append(SND_MENIAJEM_NOGI)
            


