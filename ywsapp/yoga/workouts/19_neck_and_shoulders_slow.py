#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  19_neck_and_shoulders_slow.py
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
    name: str = "neck_and_shoulders_slow"
    caption: str = "Шея и плечи медленная"
    description: str = "Медленная тренировка для расслабления мышц шеи и плеч"
    
    def __post_init__(self):
        self.wrap_asana(Asanas.tadasana.Tadasana())
        self.sets.append(SuryaNamaskar(cnt = 1, timings = 'extra_slow'))
        self.wrap_asana(Asanas.uttanasana.UttanasanaWithCompensation(tm_main = 50, tm_compensation = 30))

        self.wrap_asana(Asanas.planka.Planka(tm_main = 70))
        self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 10, tm_prepare = 5))
        self.wrap_asana(Asanas.kobra.KobraWithRotations(tm_left = 20, tm_right = 20))
        self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 20))

        self.wrap_asana(Asanas.short_poses.Nogi_k_Rukam())
        self.wrap_asana(Asanas.uttanasana.UttanasanaWithCompensation(tm_main = 30, tm_compensation = 20))

        self.wrap_asana(Asanas.ushtrasana.Ushtrasana())
        self.wrap_asana(Asanas.pashimotanasana.Pashimotanasana())
        self.wrap_asana(Asanas.marichiasana.Marichiasana())
        self.wrap_asana(Asanas.plug.Plug())
        self.wrap_asana(Asanas.matjasana.Matjasana())

        self.wrap_asana(Asanas.shavasana.Shavasana())

def do_load_workouts():
    return [DefaultWorkout]