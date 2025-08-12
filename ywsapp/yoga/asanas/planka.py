#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  planka.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import *
from asanas.uttanasana import UttanasanaBase, Uttanasana


class Planka(BaseAsana):
    def __init__(self, **kwargs):
        super().__init__(name="planka", caption="Планка")
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=4))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=40))
        self.update_props(kwargs)


        self.tasks.append(BaseTask(
            caption=self.caption + " (подготовка)",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=["planka1", "planka2"]
        ))
        self.pool("start").append(SND_OPUSTILIS)
        self.pool("name").append("name_planka1")
        self.pool("name").append("name_planka2")
        self.pool("name").append("name_planka3")
        self.main_task_planka(self.tm_main)

    def main_task_planka(self, prop):
        self.tasks.append(BaseTask(
            caption=self.caption,
            property=prop,
            metronome=MetronomeWork(),
            images=["planka1", "planka2"]
        ))
        self.pool("start").append("descr_planka1")
        self.pool("start").append("descr_planka2")
        self.pool("start").append("descr_planka3")
        self.pool("start").append("descr_planka4")
        self.pool("continue").append(FIKSIRUEM + STOIM)
        self.pool("continue").append("stoim_derzhim")
        self.float_sounds()
        self.pool("end").append(SND_ZAKONCHILI_DALSHE)

    def float_sounds(self):
        self.pool("float").append("common3")
        self.pool("float").append("common4")
        self.pool("float").append("common6")
        self.pool("float").append("common7")
        self.pool("float").append("common8")
        self.pool("float").append("common9")
        self.pool("float").append("common10")
        self.pool("float").append("common12")
        self.pool("float").append("common_duhanie_rovnoe_estestvennoe")
        self.pool("float").append("common_sledim_za_geometriei_kak_zadumanno")
        self.pool("float").append("common_prirost_navikov")
        self.pool("float").append("common_samokontrol'_primenit'_k_sebe")

    def build(self, workout, _set):
        prev_asana = workout.prev_item(self)
        if isinstance(prev_asana, UttanasanaBase):
            self.task(self.tm_prepare).pool("start").clear()
            self.task(self.tm_prepare).pool("start").append("i_s_vidohom_na_ladoni_ruk")
            self.task(self.tm_prepare).pool("start").append("ladoni_ruk_pered_soboi1")
            self.task(self.tm_prepare).pool("start").append("ladoni_ruk_pered_soboi2")
            self.task(self.tm_prepare).pool("start").append("malasana_ladoni_v_pol")


class PlankaWithRotationsEx(Planka):
    def __init__(self, with_sagging = False, **kwargs):
        super().__init__(**kwargs)
        self.properties.append(IntProperty(caption="переход на руку", short="tm_switch", default=7))
        self.properties.append(IntProperty(caption="фиксация на боку", short="tm_side", default=35))
        if with_sagging:
            self.properties.append(IntProperty(caption="провисание", short="tm_sagging", default=35))
        self.properties.append(IntProperty(caption="повторная фиксация", short="tm_second", default=20))
        self.update_props(kwargs)
        self.pool("end").clear()

        self.tasks.append(BaseTask(
            caption=self.caption +  " на левой руке\n(подготовка)",
            property=self.tm_switch,
            metronome=MetronomeRest(),
            images=["planka_left_hand"]
        ))
        self.pool("name").append("upr_razvorachivaemsia_na_levuju_ruku")
        self.pool("continue").append("vitalkivaemsia_vverh")
        self.pool("continue").append("gorka_with_leg_potianuli_udershivaja_konstruciu")
        self.pool("end").append("hand_right_vpered")
        self.construct_hand_pulls()

        self.tasks.append(BaseTask(
            caption=self.caption +  " на левой руке",
            property=self.tm_side,
            metronome=MetronomeWork(),
            images=["planka_left_hand"]
        ))
        self.float_sounds()
        self.planka_na_boku_snd_end()

        if with_sagging:
            self.tasks.append(BaseTask(
                caption=self.caption +  " на левой руке\n(провисание)",
                property=self.tm_sagging,
                metronome=MetronomeWork(),
                images=["planka_left_hand_provisanie"]
            ))
            self.pool("name").append(SND_SAGGING)
            self.pool("continue").append("enter_planka_provisli_na_levoi_ruke")
            self.pool("float").append("descr_planka_provisli_na_levoi_ruke")
            self.float_sounds()
        self.pool("end").append(SND_VERNULIS)
        self.pool("end").append("vernuli_pravuju_ruku")
    
            
        self.tasks.append(BaseTask(
            caption=self.caption +  " на правой руке\n(подготовка)",
            property=self.tm_switch,
            metronome=MetronomeRest(),
            images=["planka_right_hand"]
        ))
        self.pool("name").append("i_meniaem")
        self.pool("name").append("pereshli_na_prvuju_ruku")
        self.pool("name").append(SND_NA_DRUGUJU_STORONU)
        self.pool("continue").append("gorka_with_leg_potianuli_udershivaja_konstruciu")
        self.construct_hand_pulls()


        self.tasks.append(BaseTask(
            caption=self.caption +  " на правой руке",
            property=self.tm_side,
            metronome=MetronomeWork(),
            images=["planka_right_hand"]
        ))
        self.planka_na_boku_snd_end()


        if with_sagging:
            self.tasks.append(BaseTask(
                caption=self.caption +  " на правой руке\n(провисание)",
                property=self.tm_sagging,
                metronome=MetronomeWork(),
                images=["planka_left_hand_provisanie"]
            ))
            self.pool("name").append(SND_SAGGING)
            self.pool("continue").append("enter_planka_provisli_na_levoi_ruke")
            self.pool("float").append("descr_planka_provisli_na_levoi_ruke")
            self.float_sounds()
        self.pool("end").append(SND_VERNULIS)
        self.main_task_planka(self.tm_second)


    def construct_hand_pulls(self):
        self.pool("end").append(SND_POTIANULI_RUKU_VPERED)
        self.pool("end").append("provernuli_ruku")
        self.pool("end").append("ruku_vpered_a_sami_v_potolok", overlapsed = True)

    def planka_na_boku_snd_end(self):
        self.pool("end").append("opustili_ruku")
        self.pool("end").append("i_s_vidohom_opuskaem_ruku_vniz")
        self.pool("end").append("i_s_vidohom_opustili_ruku")
        self.pool("end").append("provernuli_ruku_opustili_vniz")
        self.pool("end").append("exit_provernuv_ruku_opuskaem_ee_vniz")


class PlankaWithLegs(Planka):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.properties.append(IntProperty(caption="фиксация ноги", short="tm_leg", default=20))
        self.properties.append(IntProperty(caption="повторная фиксация", short="tm_second", default=20))
        self.update_props(kwargs)
        self.pool("end").clear()


        self.tasks.append(BaseTask(
            caption=self.caption +  "\nлевая нога вверх",
            property=self.tm_leg,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images
        ))
        self.pool("name").append("leg_left_up1")
        self.float_sounds()
        self.pool("end").append(SND_MENIAJEM_NOGI)


        self.tasks.append(BaseTask(
            caption=self.caption +  "\nправая нога вверх",
            property=self.tm_leg,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images
        ))
        self.float_sounds()
        self.pool("end").append(SND_VERNULIS)
        self.main_task_planka(self.tm_second)
