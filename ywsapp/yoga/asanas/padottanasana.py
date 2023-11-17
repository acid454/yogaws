#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  padottanasana.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseTask
from parshvaconasana_base import BaseParshvaconasana
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import *


# Class for main padottanasana (with preparation)
class PadottanasanaBase(BaseParshvaconasana):
    def __init__(self, _side, _caption):
        super().__init__(name="padottanasana_%s"%(_side), caption=_caption, side=_side)
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=9))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=45))

        self.tasks.append(BaseTask(
            caption=self.caption + "\nподготовка",
            property=self.tm_prepare,
            metronome=MetronomeRest()
        ))
        self.pool("continue").append("vipriamlijem_perednuu_nogu")
        self.pool("end").append("i_tjanemsia_k_nei")
        self.pool("end").append("i_potianulis'_vniz")
        self.pool("end").append("opustilis'_2")
        self.pool("end").append("opustilis'_3")
        self.pool("end").append("upr_vitiagivanie_vniz1")
        self.pool("end").append("upr_vitiagivanie_vniz2")
        self.pool("end").append("upr_vitiagivanie_vniz4")
        for i in SND_S_VIDOHOM_VNIZ:
            self.pool("end").append(i) 
        
        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork()
        ))

        # all this goes to main fixation task
        self.pool("start").append("leg_priamaja_noga_ushli_k_nei")
        self.pool("start").append("vitjanulis'1")
        self.pool("start").append("vitjanulis'2")
        self.pool("start").append("i_mu_zamerli")
        self.pool("start").append("i_dershimsia")
        self.pool("start").append("i_stoim1")
        self.pool("start").append("i_stoim2")
        self.pool("start").append("i_stoim3")
        self.pool("float").append("descr_padattonasana")
        self.pool("float").append("leg_rastiagivaja_mishzi_zadnei_chasti_nogi")
        self.pool("float").append("common_delaem_vse_ne_toropias'")
        self.pool("float").append("common_telo_prosedajet")
        self.pool("float").append("common7")
        self.pool("float").append("common_derzimsia_dushim")
        self.pool("float").append("posvisajem_potianemsia")
        self.pool("float").append("common_tianemsia_2x")
        self.pool("float").append("common_i_postojat'_podushat'")
        self.pool("float").append("descr_prasarita_potjanulis_k_noge_common")
        self.pool("end").append("vernulis'1")
        self.pool("end").append("vernulis'2")
        for i in SND_ZAKONCHILI_DALSHE:
            self.pool("end").append(i) 

    def build_snd_name(self):
        self.tasks[0].pool("name").append("name_padottanasana1")
        self.tasks[0].pool("name").append("name_padottanasana2")
        self.tasks[0].pool("name").append("name_padottanasana3")


class PadottanasanaLeft(PadottanasanaBase):
    def __init__(self, **kwargs):
        super().__init__('left', "Падоттанасана\n(левая нога)")
        self.update_props(kwargs)
        self.update_all_tasks_images([f"padottanasana_left{x}" for x in range(1,3)])
        self.tasks[0].pool("continue").append("leg_left_vipriamlajem")


class PadottanasanaRight(PadottanasanaBase):
    def __init__(self, **kwargs):
        super().__init__('right', "Падоттанасана\n(правая нога)")
        self.update_props(kwargs)
        self.update_all_tasks_images([f"padottanasana_right{x}" for x in range(1,3)])
