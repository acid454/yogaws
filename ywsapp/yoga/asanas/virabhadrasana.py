#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  virabhadrasana.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

import random
from base import BaseTask
from go_down_base import AsanaGoDown
from parshvaconasana_base import BaseParshvaconasana
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import *


# Class for main virabhadrasana (with preparation)
class VirabhadrasanaBase(BaseParshvaconasana, AsanaGoDown):
    def __init__(self, _side, _caption, _go_down):
        super().__init__(name="virabhadrasana_%s"%(_side), caption=_caption, side = _side, prepare_tm_for_swap_hands = 4)
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=9))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=40))
        if _go_down:
            self.properties.append(IntProperty(caption="фиксация лежа", short="tm_down", default=45))
            self.properties.append(IntProperty(caption="выход", short="tm_exit", default=4))

        self.tasks.append(BaseTask(
            caption=self.caption + "\nподготовка",
            property=self.tm_prepare,
            metronome=MetronomeRest()
        ))

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork()
        ))

        # virabhadrasana_snds goes here - all this goes to main fixation task
        self.pool("continue").append("enter_virabhadrasana1")
        self.pool("continue").append("enter_virabhadrasana2")
        self.pool("continue").append("enter_virabhadrasana3")
        self.pool("continue").append("enter_virabhadrasana4")
        self.pool("continue").append("descr_virabhadrasana_obrashaem_vnimanie_na_stupniu_i_koleno")
        self.pool("continue").append("descr_virabhadrasana_telo_odna_linija")
        self.pool("float").append("descr_virabhadrasana_vipriamlaem_zadnuu_nogu")
        self.pool("continue" if random.randint(0, 1) else "float").append("descr_virabhadrasana3")
        self.pool("float").append("descr_virabhadrasana4")
        self.pool("float").append("descr_virabhadrasana5")
        self.pool("float").append("common_tianemsia_intensovno_vverh")
        self.pool("float").append("common_ne_zabuvaem_raspredeliat'_ravnovesie")
        self.pool("float").append("descr_virabhadrasana6")
        self.pool("continue").append("descr_virabhadrasana7")
        self.pool("float").append("descr_virabhadrasana8")
        self.pool("continue").append("descr_virabhadrasana10")
        self.pool("float").append("descr_virabhadrasana11")
        self.pool("continue").append("descr_virabhadrasana12")
        self.pool("float").append("descr_virabhadrasana13")
        self.pool("float").append("descr_virabhadrasana14")
        self.pool("float").append("descr_parivritta_parshvakonasana5", float_on_start = True)
        self.pool("float").append("common_glubokoe_proshivanie_tela")

        #!!!!!!! TODO: short sounds
        if self.tm_main.value <= 10:
            self.pool("float").append("common_delaem_vse_ne_toropias'")
            self.pool("float").append("common_derzimsia_dushim")
            self.pool("float").append(FIKSIRUEM + STOIM)
        
        if _go_down:
            self.go_down_task(self.tm_down, self.tm_exit, self.float_sounds)
            self.tasks[-2].images = ["kapotasana_down_left"] if _side == 'left' else ["kapotasana_down_right"]
            self.task(self.tm_exit).images = self.task(self.tm_prepare).images
        else:
            self.pool("end").append(SND_RASSLABILIS + SND_EXHALE + SND_S_VIDOHOM_VNIZ)
    
    def float_sounds(self):
        self.pool("float").append("descr_virabhadrasana1")
        self.pool("float").append("descr_virabhadrasana9")
        self.pool("float").append("common_povtoriaushiesia_pozu")
        self.pool("float").append("common_vihodim_iz_asan_plavno")
        self.pool("float").append("common_akcentiruite_vidohi")
        self.pool("float").append("common_delaem_medlenno_pomogaja_duhaniem")
        self.pool("float").append("common_duhanie_estestvennoe_long")
        
    def build_snd_name(self, prev_asana):
        if issubclass(type(prev_asana), VirabhadrasanaBase):
            return
        self.tasks[0].pool("name").append("name_virabhadrasana1")
        self.tasks[0].pool("name").append("name_virabhadrasana2")
        self.tasks[0].pool("name").append("name_virabhadrasana3")
        self.tasks[0].pool("name").append("name_virabhadrasana4")
        self.tasks[0].pool("name").append("name_virabhadrasana5")

class VirabhadrasanaLeft(VirabhadrasanaBase):
    def __init__(self, **kwargs):
        _down = kwargs.get('go_down', False)
        super().__init__('left', "Вирабхадрасана (левая нога)", _go_down = _down)
        self.update_props(kwargs)

        self.update_all_tasks_images([f"virabhadrasana_left{x}" for x in range(1,5)])
        if _down:
            self.task(self.tm_down).images = [f"virabhadrasana_down_left{x}" for x in range(1,3)]

class VirabhadrasanaRight(VirabhadrasanaBase):
    def __init__(self, **kwargs):
        _down = kwargs.get('go_down', False)
        super().__init__('right', "Вирабхадрасана (правая нога)", _go_down = _down)
        self.update_props(kwargs)

        self.update_all_tasks_images([f"virabhadrasana_right{x}" for x in range(1,5)])
        if _down:
            self.task(self.tm_down).images = [f"virabhadrasana_down_right{x}" for x in range(1,3)]
