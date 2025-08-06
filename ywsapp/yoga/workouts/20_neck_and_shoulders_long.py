#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  20_neck_and_shoulders_long.py
#  
#  Copyright 2025 Dmitry Repnikov <acid454@yoga7>
#  

from dataclasses import dataclass
from base import BaseWorkout
from asanas import Asanas
from surya_namaskar import SuryaNamaskar
from ktimer import KTimerX3


@dataclass
class DefaultWorkout(BaseWorkout):
    name: str = "neck_and_shoulders_long"
    caption: str = "Шея и плечи #2 увеличенная"
    description: str = "Медленная тренировка для расслабления мышц шеи и плеч, увеличенная версия"
    
    def __post_init__(self):
        self.wrap_asana(Asanas.tadasana.Tadasana())
        self.sets.append(SuryaNamaskar(cnt = 1, timings = 'extra_slow'))
        self.wrap_asana(Asanas.uttanasana.Uttanasana_ruki_v_zamke(tm_main = 50, tm_zamok = 30))

        #self.wrap_asana(Asanas.planka.PlankaWithRotationsEx())
        self.wrap_asana(Asanas.planka.Planka(tm_main = 60))
        self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 10, tm_prepare = 5))
        self.wrap_asana(Asanas.kobra.KobraWithRotations(tm_left = 20, tm_right = 20))
        self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 20))

        self.wrap_asana(Asanas.short_poses.Nogi_k_Rukam())
        self.wrap_asana(Asanas.uttanasana.Uttanasana_ruki_v_zamke(tm_main = 50, tm_zamok = 30))
        self.wrap_asana(Asanas.short_poses.Seli())
        self.wrap_asana(Asanas.stol.Stol())

        self.wrap_asana(Asanas.ushtrasana.Ushtrasana(tm_main = 50))
        self.wrap_asana(Asanas.short_poses.PodnimaemsiaVvreh())

        self.wrap_asana(Asanas.vitjashenie_vverh.VitjashenieVverh(tm_main = 30))
        self.wrap_asana(Asanas.uttanasana.Uttanasana_ruki_v_zamke(tm_main = 70, tm_zamok = 30))

        self.wrap_asana(Asanas.short_poses.Seli())
        self.wrap_asana(Asanas.malasana.Malasana())
        self.wrap_asana(Asanas.kobra.Kobra(tm_main = 50))
        self.wrap_asana(Asanas.pashimotanasana.Pashimotanasana())
        self.wrap_asana(Asanas.marichiasana.Marichiasana())
        self.wrap_asana(Asanas.plug.Plug())
        self.wrap_asana(Asanas.perekati_na_spine.Perekatu_na_spine())
        self.wrap_asana(Asanas.matjasana.Matjasana())
        self.wrap_asana(Asanas.pashimotanasana.Pashimotanasana())

        self.wrap_asana(Asanas.shavasana.Shavasana())

def do_load_workouts():
    return [DefaultWorkout]