#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sukhasana.py
#  
#  Copyright 2025 Repnikov Dmitry <acid454@yoga7>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import *


class Sukhasana(BaseAsana):
    def __init__(self, **kwargs):
        super().__init__(name="sukhasana", caption="Сукхасана")
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=8))
        self.properties.append(IntProperty(caption="вытяжение вперёд", short="tm_main", default=20))
        self.properties.append(IntProperty(caption="циклов наклона", short="cycles_count", default=2))
        self.properties.append(IntProperty(caption="вытяжение вбок", short="tm_side", default=15))
        self.properties.append(IntProperty(caption="выход", short="tm_exit", default=5))
        self.update_props(kwargs)
        
        self.tasks.append(BaseTask(
            caption=self.caption + " (подготовка)",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=["sukhasana_prepare1"]
        ))
        self.pool("name").append("skrestili_nogi")
        self.pool("end").append(SND_POTIANULIS_VPERED)

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=["sukhasana_forward1"]
        ))
        self.snd_float()
        self.pool("end").append(SND_PODNIMAEMSIA)
        

        for i in range(self.cycles_count.value):
            self.tasks.append(BaseTask(
                caption=self.caption + "\nнаклон влево",
                property=self.tm_side,
                metronome=MetronomeWork(),
                images=["sukhasana_left1"]
            ))
            if i == 0:
                self.pool("name").append("potjanulis'_za_koleno_left")
            else:
                self.pool("name").append("upr_potjanulis_v_levuju_storonu")
                self.pool("name").append(SND_NA_DRUGUJU_STORONU)

            self.tasks.append(BaseTask(
                caption=self.caption + "\nнаклон вправо",
                property=self.tm_side,
                metronome=MetronomeWork(),
                images=["sukhasana_right1"]
            ))
            self.pool("name").append(SND_NA_DRUGUJU_STORONU)

        self.tasks.append(BaseTask(
            caption=self.caption + " (выход)",
            property=self.tm_exit,
            metronome=MetronomeRest(),
            images=["sukhasana_prepare1"]
        ))
        self.pool("name").append(SND_ZAKONCHILI_DALSHE)

    def snd_float(self):
        self.pool("float").append("common_podrasslabitsia")
        self.pool("float").append("common_ne_pererastjagivaem_mushci")
        self.pool("float").append("common_rasslabit'_lico_plechi")
        self.pool("float").append("common_delaem_plavno")
        self.pool("float").append("common_prirost_navikov")
        self.pool("float").append("common_telo_prosedajet")
        self.pool("float").append("common8")
        self.pool("float").append("common9")
        self.pool("float").append("common11")
        self.pool("float").append("common_delaite_to_chto_poluchaetsia")
        self.pool("float").append("common_duhanie_rovnoe_estestvennoe")
        self.pool("float").append("common_sbrasivaete_napriajenie_s_litca_s_shivota")
        self.pool("float").append("common_isportit'_usediem")
        self.pool("float").append("common_glubokoe_proshivanie_tela")
        self.pool("float").append("marichiasana_common_sledim_za_pozvonochnikom")
        self.pool("float").append("common_vsie_budet_horosho")
        