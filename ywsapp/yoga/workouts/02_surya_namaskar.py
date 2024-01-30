#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  02_surya_namaskar.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseWorkout
from asanas import Asanas
from surya_namaskar import SuryaNamaskar


class DefaultWorkout(BaseWorkout):
    def __init__(self):
        BaseWorkout.__init__(self,
                             name = "surya_namaskar",
                             caption = "Сурья Намаскар 20 минут",
                             description = "Сурья Намаскар и несколько основных асан")
    
        self.wrap_asana(Asanas.tadasana.Tadasana())
        self.sets.append(SuryaNamaskar(cnt = 3))

        self.wrap_asana(Asanas.planka.Planka(tm_main = 90))

        self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 10, tm_prepare = 5))
        self.wrap_asana(Asanas.parivritta.ParivrittaLeft())
        self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 10))
        self.wrap_asana(Asanas.parivritta.ParivrittaRight())
        self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 10))
        #self.wrap_asana(Asanas.padottanasana.PadottanasanaLeft())
        #self.wrap_asana(Asanas.padottanasana.PadottanasanaRight())
        self.wrap_asana(Asanas.prasarita_padottanasana.PrasaritaPadottanasana(with_hands = False))

        #self.wrap_asana(Asanas.nogi_k_rukam.Nogi_k_Rukam())
        self.wrap_asana(Asanas.ardhachandrasana.ArdhachandrasanaLeft())
        self.wrap_asana(Asanas.ardhachandrasana.ArdhachandrasanaRight())

        self.wrap_asana(Asanas.bakasana.Bakasana())
        self.wrap_asana(Asanas.baddha_konasana.BaddhaKonasana(with_knees = False))
        
        #self.wrap_asana(Asanas.marichiasana.Marichiasana())
        self.wrap_asana(Asanas.most.Most())

        self.wrap_asana(Asanas.plug.Plug())
        self.wrap_asana(Asanas.sarvangasana.Sarvangasana())

        self.wrap_asana(Asanas.shavasana.Shavasana())

def do_load_workouts():
    return [DefaultWorkout]