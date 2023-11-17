#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  04_surya7_medium.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseWorkout
from asanas import Asanas
from surya_namaskar import SuryaNamaskar


class DefaultWorkout(BaseWorkout):
    def __init__(self):
        BaseWorkout.__init__(self,
                             name = "surya7_medium",
                             caption = "7 сурий средняя",
                             description = "Разогреться и расслабиться")
    
        self.wrap_asana(Asanas.tadasana.Tadasana())
        self.sets.append(SuryaNamaskar(slow_timings = True, cnt = 3))
        self.sets.append(SuryaNamaskar(slow_timings = False, cnt = 4))

        self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 10, tm_prepare = 5))
        self.wrap_asana(Asanas.parivritta.ParivrittaLeft(tm_main = 30))
        self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 10, tm_prepare = 0))
        self.wrap_asana(Asanas.parivritta.ParivrittaRight(tm_main = 30))
        self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 10, tm_prepare = 0))
        self.wrap_asana(Asanas.padottanasana.PadottanasanaLeft())
        self.wrap_asana(Asanas.padottanasana.PadottanasanaRight())
        self.wrap_asana(Asanas.prasarita_padottanasana.PrasaritaPadottanasana(with_hands = False))

        self.wrap_asana(Asanas.nogi_k_rukam.Nogi_k_Rukam())
        self.wrap_asana(Asanas.ardhachandrasana.Ardhachandrasana())

        self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 45, tm_prepare = 5))
        self.wrap_asana(Asanas.sobaka_mordoi_vverh.SobakaMordoiVverh(tm_main = 45))
        self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 10, tm_prepare = 0))
        self.wrap_asana(Asanas.kapotasana.Kapotasana())
        self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 10, tm_prepare = 0))
        self.wrap_asana(Asanas.ushtrasana.Ushtrasana())

        self.wrap_asana(Asanas.pashimotanasana.Pashimotanasana())
        self.wrap_asana(Asanas.marichiasana.Marichiasana())
        
        self.wrap_asana(Asanas.plug.Plug())
        self.wrap_asana(Asanas.nakrasana.Nakrasana())

        self.wrap_asana(Asanas.sarvangasana.Sarvangasana())
        self.wrap_asana(Asanas.shavasana.Shavasana())

def do_load_workouts():
    return [DefaultWorkout]