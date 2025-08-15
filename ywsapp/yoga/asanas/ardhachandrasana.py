#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ardhachandrasana.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeRest, MetronomeWork
from snd_pools import *

class ArdhachandrasanaBase(BaseAsana):
    def __init__(self, _side):
        self.side = _side
        side_text = 'левая' if _side == 'left' else 'правая'
        super().__init__(name="ardhachandrasana", caption="Ардха Чандрасана\n(%s сторона)"%(side_text))
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=13))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=25))
        #self.properties.append(IntProperty(caption="выход", short="tm_exit", default=4))

        self.tasks.append(BaseTask(
            caption=self.caption + "\nподготовка",
            property=self.tm_prepare,
            metronome=MetronomeRest()
        ))

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images        # This is reference to prev task's images
        ))
        self.pool("float").append("descr_ardhachandrasana_zameret'")
        self.pool("float").append("common3")
        self.pool("float").append("common4_dushim_dershimsia")
        self.pool("float").append("descr_ardhachandrasana_common1")
        self.pool("float").append("common_esli_chto_to_ne_poluchaetsia")
        self.pool("float").append("common10")
        self.pool("float").append("common6")
        self.pool("float").append("descr_ardhachandrasana_common2")
        self.pool("float").append("common_i_postojat'_podushat'", float_on_start = True)
        self.pool("float").append("common_derzimsia_dushim")
        self.pool("float").append("common_vashna_geometria_i_tochnost")
        self.pool("float").append("common1")
        self.pool("float").append("common_duhanie_rovnoe_estestvennoe")
        self.pool("float").append("common_sledim_za_geometriei_kak_zadumanno")
        self.pool("float").append("common_tianemsia_intensovno_vverh")
        self.pool("float").append("common_ne_zabuvaem_raspredeliat'_ravnovesie")
        self.pool("end").append(SND_RASSLABILIS + SND_EXHALE + SND_S_VIDOHOM_VNIZ)
        self.pool("end").append("i_s_vidohom_na_ladoni_ruk")
        self.pool("end").append("i_s_vidohom_opuskaem_ruku_vniz")
        self.pool("end").append("i_s_vidohom_opustili_ruku")
        self.pool("end").append("provernuli_ruku_opustili_vniz")
        self.pool("end").append("i_provernuv_ruku_vozvrashaemsia")
        self.pool("end").append("exit_provernuv_ruku_opuskaem_ee_vniz")

    def build(self, workout, _set):
        super().build(workout, _set)
        prev_asana = workout.prev_item(self)
        if issubclass(type(prev_asana), ArdhachandrasanaBase):
            if self.side == prev_asana.side:
                return
            t = self.task(self.tm_prepare)
            t.pool("start").clear()
            t.pool("start").append(SND_MENIAJEM_NOGI + SND_NA_DRUGUJU_STORONU, mandatory = True)
            return
        
        with self.task(self.tm_prepare) as t:
            t.pool("name").append("name_ardhachandrasana1")
            t.pool("name").append("name_ardhachandrasana2")
            t.pool("name").append("name_ardhachandrasana3")

class ArdhachandrasanaLeft(ArdhachandrasanaBase):
    def __init__(self, **kwargs):
        super().__init__(_side = 'left')
        self.update_props(kwargs)

        with self.task(self.tm_prepare) as t:
            t.images += [f"ardhachandrasana_left{x}" for x in range(1,4)]
            t.pool('continue').append("leg_left_opornaja")
            t.pool('float').append('enter_ardhachandrasana_left1', float_on_start = True)

class ArdhachandrasanaRight(ArdhachandrasanaBase):
    def __init__(self, **kwargs):
        super().__init__(_side='right')
        self.update_props(kwargs)

        with self.task(self.tm_prepare) as t:
            t.images += [f"ardhachandrasana_right{x}" for x in range(1,4)]
            # ToDo: need 'leg right opornaja' sound
            #t.pool('continue').append("leg_left_opornaja")
            self.tasks[0].pool("continue").append(SND_LEG_RIGHT_FORWARD)
            t.pool('float').append('enter_ardhachandrasana_right1', float_on_start = True)
            t.pool('float').append('enter_ardhachandrasana_right2', float_on_start = True)
            t.pool('float').append('enter_ardhachandrasana_right3', float_on_start = True)
