#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  15 hermes10min.py
#  
#  Copyright 2024 Dmitry Repnikov <acid454@x220>
#  

from dataclasses import dataclass
from base import BaseWorkout
from asanas import Asanas
from hermes import HermesGymnastics


@dataclass
class DefaultWorkout(BaseWorkout):
    name: str = "hermes10min"
    caption: str = "Гимнастика Гермеса Трисмегиста 10 минут"
    description: str = ""
    group: str = "Гермес Трисмегист"

    def __post_init__(self):
        self.wrap_asana(Asanas.tadasana.Tadasana())
        self.wrap_asana(Asanas.vitjashenie_vverh.VitjashenieVverh(tm_main = 20))
        self.wrap_asana(Asanas.vitjashenie_vpered.VitjashenieVpered(tm_main = 10))
        self.wrap_asana(Asanas.uttanasana.UttanasanaWithCompensation(tm_main = 40, tm_compensation = 20))
        self.wrap_asana(Asanas.planka.Planka(tm_main = 60))
        self.wrap_asana(Asanas.sobaka_mordoi_vverh.SobakaMordoiVverh(tm_main = 30))
        self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 30, tm_prepare = 5))
        self.wrap_asana(Asanas.short_poses.Nogi_k_Rukam())

        self.sets.append(HermesGymnastics())
        
        self.wrap_asana(Asanas.shavasana.Shavasana())



def do_load_workouts():
    return [DefaultWorkout]