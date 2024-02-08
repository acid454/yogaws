#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  04_surya7_medium.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from dataclasses import dataclass
from base import BaseWorkout
from asanas import Asanas
from surya_namaskar import SuryaNamaskar


@dataclass
class DefaultWorkout(BaseWorkout):
    name: str = "surya7_medium"
    caption: str = "7 сурий средняя"
    description: str = "Разогреться и расслабиться"
    group: str = "Сурья Намаскар"
    
    def __post_init__(self):
        self.wrap_asana(Asanas.tadasana.Tadasana())
        self.sets.append(SuryaNamaskar(slow_timings = True, cnt = 3))
        self.sets.append(SuryaNamaskar(slow_timings = False, cnt = 4))

        self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 10, tm_prepare = 5))
        self.wrap_asana(Asanas.parivritta.ParivrittaLeft())
        self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 10))
        self.wrap_asana(Asanas.parivritta.ParivrittaRight())
        self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 10))
        #self.wrap_asana(Asanas.padottanasana.PadottanasanaLeft())
        #self.wrap_asana(Asanas.padottanasana.PadottanasanaRight())
        self.wrap_asana(Asanas.prasarita_padottanasana.PrasaritaPadottanasana(with_hands = False))

        self.wrap_asana(Asanas.nogi_k_rukam.Nogi_k_Rukam())
        self.wrap_asana(Asanas.ardhachandrasana.ArdhachandrasanaLeft())
        self.wrap_asana(Asanas.ardhachandrasana.ArdhachandrasanaRight())

        self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 45, tm_prepare = 5))
        self.wrap_asana(Asanas.sobaka_mordoi_vverh.SobakaMordoiVverh(tm_main = 45))
        self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 10))

        self.wrap_asana(Asanas.nogi_k_rukam.Nogi_k_Rukam())
        self.wrap_asana(Asanas.bakasana.Bakasana())

       # self.wrap_asana(Asanas.kapotasana.KapotasanaLeft())
       # self.wrap_asana(Asanas.kapotasana.KapotasanaRight())
        self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 10))
        self.wrap_asana(Asanas.ushtrasana.Ushtrasana())

        self.wrap_asana(Asanas.pashimotanasana.Pashimotanasana())
        self.wrap_asana(Asanas.marichiasana.Marichiasana())
        
        self.wrap_asana(Asanas.plug.Plug())
        self.wrap_asana(Asanas.nakrasana.Nakrasana())

        self.wrap_asana(Asanas.sarvangasana.Sarvangasana())
        self.wrap_asana(Asanas.shavasana.Shavasana())

def do_load_workouts():
    return [DefaultWorkout]