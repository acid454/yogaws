#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kapotasana.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from go_down_base import AsanaGoDown
from properties import IntProperty
from metronomes import MetronomeRest, MetronomeWork
from snd_pools import *

class KapotasanaBase(BaseAsana, AsanaGoDown):
    def __init__(self, _side, _caption, _go_down):
        super().__init__(name="kapotasana_%s"%(_side), caption=_caption)
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=13))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=35))
        if _go_down:
            self.properties.append(IntProperty(caption="фиксация лежа", short="tm_down", default=35))
            self.properties.append(IntProperty(caption="выход", short="tm_exit", default=4))

        self.tasks.append(BaseTask(
            caption=self.caption + "\nподготовка",
            property=self.tm_prepare,
            metronome=MetronomeRest()
        ))
        self.pool("end").append("i_tjanemsia_vverh")
        self.pool("end").append("so_vdohom_vverh1")
        self.pool("end").append("vitalkivaemsia_vverh")
        self.pool("end").append("upr_vitajshenie_vverh1")
        self.pool("end").append("upr_vitajshenie_vverh2")
        self.pool("end").append("upr_vitajshenie_vverh3_na_vdohe")
        self.pool("end").append("vitjanulis'1")
        self.pool("end").append("vitjanulis'2")
        self.pool("end").append(FIKSIRUEM)

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork()
        ))
        self.pool("float").append("descr_kapotasana")
        self.pool("float").append("common3")
        self.pool("float").append("common4")
        self.pool("float").append("common5_v_vitalkivanii")
        self.pool("float").append("common8")
        self.pool("float").append("common_tianemsia_intensovno_vverh")
        self.pool("float").append("common_sledim_za_geometriei_kak_zadumanno")
        self.float_sounds()

        if _go_down:
            self.go_down_task(self.tm_down, self.tm_exit, self.float_sounds)
            #self.tasks[-2].images =  if _side == 'left' else ["kapotasana_down_right"]
            self.task(self.tm_exit).images = self.task(self.tm_prepare).images
        
    def float_sounds(self):
        self.pool("float").append("common7")
        self.pool("float").append("common9")
        self.pool("float").append("common10")
        self.pool("float").append("common12")
        self.pool("float").append("common_duhanie_rovnoe_estestvennoe")
        self.pool("float").append("common_ubedilis'_chto_nam_horosho")
        self.pool("float").append("marichiasana_common_sledim_za_pozvonochnikom")
        self.pool("float").append("common_vsie_budet_horosho")
        self.pool("float").append("common_sbrasivaete_napriajenie_s_litca_s_shivota")
        self.pool("float").append("common_vihodim_iz_asan_plavno")
        self.pool("float").append("common_akcentiruite_vidohi")
        self.pool("float").append("common_delaem_medlenno_pomogaja_duhaniem")
        self.pool("float").append("common_delaite_to_chto_poluchaetsia")
        self.pool("float").append("common_duhanie_estestvennoe_long")
        self.pool("float").append("common_isportit'_usediem")
    
    def build(self, workout, _set):
        super().build(workout, _set)
        prev_asana = workout.prev_item(self)
        if issubclass(type(prev_asana), KapotasanaBase):
            if self.side == prev_asana.side:
                return
            t = self.task(self.tm_prepare)
            t.pool("start").clear()
            t.pool("start").append("i_meniaem", mandatory = True)
            t.pool("start").append(SND_MENIAJEM_NOGI + SND_NA_DRUGUJU_STORONU, mandatory = True)
            return
        
        with self.task(self.tm_prepare) as t:
            t.pool("name").append("name_kapotasana1")
            t.pool("name").append("name_kapotasana2")
            t.pool("name").append("name_kapotasana3")

class KapotasanaLeft(KapotasanaBase):
    def __init__(self, **kwargs):
        _down = kwargs.get('go_down', False)
        super().__init__('left', "Капотасана\n(левая сторона)", _go_down = _down)
        self.update_props(kwargs)
        
        self.update_all_tasks_images([f"kapotasana_left{x}" for x in range(1,3)])
        self.task(self.tm_prepare).pool("continue").append(SND_SIDE_LEFT)
        if _down:
            self.task(self.tm_down).images = ["kapotasana_down_left"]

class KapotasanaRight(KapotasanaBase):
    def __init__(self, **kwargs):
        _down = kwargs.get('go_down', False)
        super().__init__('right', "Капотасана\n(правая сторона)", _go_down = _down)
        self.update_props(kwargs)

        self.update_all_tasks_images([f"kapotasana_right{x}" for x in range(1,3)])
        self.task(self.tm_prepare).pool("start").append(SND_LEG_RIGHT_FORWARD)
        if _down:
            self.task(self.tm_down).images = ["kapotasana_down_right"]

            
        