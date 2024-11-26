#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  16 surya and hermes.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from dataclasses import dataclass
from base import BaseWorkout
from asanas import Asanas
from surya_namaskar import SuryaNamaskar
from hermes import HermesGymnastics


@dataclass
class DefaultWorkout(BaseWorkout):
    name: str = "surya_and_hermes"
    caption: str = "Сурья Намаскар и гимнастика Гермеса Трисмегиста"
    description: str = "Разминочные упражнения из цикла приветствия Солнцу и Гимнастика Гермеса Трисмегиста"
    group: str = "Гермес Трисмегист"
    
    def __post_init__(self):
        self.wrap_asana(Asanas.tadasana.Tadasana())
        self.sets.append(SuryaNamaskar(cnt = 3))
        self.sets.append(HermesGymnastics())

        self.wrap_asana(Asanas.vitjashenie_vverh.VitjashenieVverh(tm_main = 20))
        self.wrap_asana(Asanas.uttanasana.UttanasanaWithCompensation(tm_main = 40, tm_compensation = 20))
        self.wrap_asana(Asanas.sobaka_mordoi_vverh.SobakaMordoiVverh(tm_main = 30))
        self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 30, tm_prepare = 5))
        
        self.wrap_asana(Asanas.shavasana.Shavasana())



def do_load_workouts():
    return [DefaultWorkout]