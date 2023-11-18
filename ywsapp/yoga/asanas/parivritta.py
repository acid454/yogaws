#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  parivritta.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseTask
from parshvaconasana_base import BaseParshvaconasana
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import *

# Class for main parivritta (with preparation)
class ParivrittaBase(BaseParshvaconasana):
    def __init__(self, _side, _caption):
        super().__init__(name="parivritta_%s"%(_side), caption=_caption, side=_side)
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=12))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=30))

        self.tasks.append(BaseTask(
            caption=self.caption + "подготовка",
            property=self.tm_prepare,
            metronome=MetronomeRest()
        ))
        self.pool("end").append("krug_rukoi_i_potianuli_ee_vpered")
        self.pool("end").append("krug_rukoi_provorot")
        self.pool("end").append("i_potianuli_ruku_vpered1")
        self.pool("end").append("i_potianuli_ruku_vpered2")
        self.pool("end").append("i_potianuli_ruku_vpered3")
        self.pool("end").append("i_potjanut'_ruku_vpered")
        self.pool("end").append("ruku_vpered_a_sami_v_potolok")

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork()
        ))

        # all this goes to main fixation task
        self.pool("start").append("makushka_golovi_tianet_vpered")
        self.pool("start").append("upr_potjanulis_vpered1")
        self.pool("start").append("upr_potjanulis_vpered2")
        self.pool("start").append("upr_potjanulis_vpered3")
        self.pool("start").append("upr_potjanulis_vpered5")
        self.pool("start").append("upr_potjanulis_vpered7")
        self.pool("start").append("vitjanulis'1")
        self.pool("start").append("vitjanulis'2")
        self.pool("start").append("fiksiruem")
        self.pool("start").append("i_mu_zamerli")
        self.pool("start").append("i_dershimsia")
        self.pool("start").append("i_stoim1")
        self.pool("float").append("descr_parivritta_parshvakonasana2")
        self.pool("float").append("descr_parivritta_parshvakonasana3")
        self.pool("float").append("descr_parivritta_parshvakonasana4")
        self.pool("float").append("descr_utthita_vzgliad_v_potolok")
        self.pool("float").append("common1")
        self.pool("float").append("common3")
        self.pool("float").append("common4")
        self.pool("float").append("descr_parivritta_parshvakonasana1")
        self.pool("float").append("descr_parivritta_parshvakonasana5")
        self.pool("float").append("common10")
        self.pool("float").append("common6")
        self.pool("float").append("common12")
        self.pool("float").append("descr_utthita_stupnia_ruka")
        self.pool("float").append("common7")
        self.pool("float").append("common_derzimsia_dushim")
        self.pool("float").append("common_i_postojat'_podushat'")
        self.pool("end").append("i_s_vidohom_opuskaem_ruku_vniz")
        self.pool("end").append("i_s_vidohom_opustili_ruku")
        self.pool("end").append("provernuli_ruku_opustili_vniz")
        self.pool("end").append("exit_provernuv_ruku_opuskaem_ee_vniz")
        for i in SND_S_VIDOHOM_VNIZ:
            self.pool("end").append(i) 
    
    def build(self, workout, _set):
        super().build(workout, _set)
        prev_asana = workout.prev_item(self)
        if type(prev_asana) is BaseParshvaconasana:
            if prev_asana.side == self.side:
                # We are in utthita/parivritta, and leg is same - only swap hands
                self.tm_prepare.default = 8
        # Others - default 16

    def build_snd_name(self):
        self.tasks[0].pool("name").append("name_parivritta_pashvakonasana1")
        self.tasks[0].pool("name").append("name_parivritta_pashvakonasana2")


class ParivrittaLeft(ParivrittaBase):
    def __init__(self, **kwargs):
        super().__init__('left', "Паривритта Паршваконасана\n(левая нога)")
        self.update_props(kwargs)
        self.update_all_tasks_images([f"parivritta_parshvakonasana_left{x}" for x in range(1,5)])
    
    def build_snd_name(self):
        super().build_snd_name()
        self.tasks[0].pool("continue").append("short_enter_parivritta_parshvakonasana_left1")
        self.tasks[0].pool("continue").append("short_enter_parivritta_parshvakonasana_left2")
        self.tasks[0].pool("continue").append("enter_parivritta_parshvakonasana_left")


class ParivrittaRight(ParivrittaBase):
    def __init__(self, **kwargs):
        super().__init__('right', "Паривритта Паршваконасана\n(правая нога)")
        self.update_props(kwargs)
        self.update_all_tasks_images([f"parivritta_parshvakonasana_right{x}" for x in range(1,5)])
    
    def build_snd_name(self):
        super().build_snd_name()
        self.tasks[0].pool("continue").append("short_enter_parivritta_parshvakonasana_right1")
        self.tasks[0].pool("continue").append("short_enter_parivritta_parshvakonasana_right2")
        self.tasks[0].pool("continue").append("short_enter_parivritta_parshvakonasana_right3")
