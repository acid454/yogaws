#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kapotasana.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeRest, MetronomeWork
from snd_pools import *

class KapotasanaBase(BaseAsana):
    def __init__(self, _side):
        self.side = _side
        side_text = 'левая' if _side == 'left' else 'правая'
        super().__init__(name="kapotasana", caption="Капотасана\n(%s сторона)"%(side_text))
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=13))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=35))

        self.tasks.append(BaseTask(
            caption=self.caption + "\nподготовка",
            property=self.tm_prepare,
            metronome=MetronomeRest()
        ))
        self.pool("end").append("vitjanulis'1")
        self.pool("end").append("vitjanulis'2")
        self.pool("end").append(FIKSIRUEM)

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images            # We made a ref to prev task's images
        ))
        self.pool("float").append("descr_kapotasana")
        self.pool("float").append("common9")
        self.pool("float").append("common12")
        self.pool("float").append("common1")
        self.pool("float").append("common3")
        self.pool("float").append("common4")
        self.pool("float").append("common5_v_vitalkivanii")
        self.pool("float").append("common7")
        self.pool("float").append("common8")
        self.pool("float").append("common10")
        self.pool("float").append("common_duhanie_rovnoe_estestvennoe")
        self.pool("float").append("common_sledim_za_geometriei_kak_zadumanno")
        self.pool("float").append("common_ubedilis'_chto_nam_horosho")
        self.pool("float").append("marichiasana_common_sledim_za_pozvonochnikom")
        self.pool("float").append("common_vsie_budet_horosho")
        self.pool("float").append("common_sbrasivaete_napriajenie_s_litca_s_shivota")
    
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
        super().__init__(_side = 'left')
        self.update_props(kwargs)

        with self.task(self.tm_prepare) as t:
            t.images += ["kapotasana_left1"]
            t.pool("continue").append(SND_SIDE_LEFT)

class KapotasanaRight(KapotasanaBase):
    def __init__(self, **kwargs):
        super().__init__(_side = 'right')
        self.update_props(kwargs)

        with self.task(self.tm_prepare) as t:
            t.images += ["kapotasana_right1"]
            t.pool("start").append(SND_LEG_RIGHT_FORWARD)

            
        