#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  07_surya3_slow.py
#  
#  Copyright 2023 Repnikov Dmitry <acid454@yoga7>
#  

from dataclasses import dataclass
from base import BaseWorkout
from asanas import Asanas
from surya_namaskar import SuryaNamaskar
from ktimer import KTimerX3

@dataclass
class DefaultWorkout(BaseWorkout):
    name: str = "surya3_slow"
    caption: str = "Сурьи медленная"
    description: str = "Увеличенные интервалы Сурья Намаскар"
    group: str = "Сурья Намаскар"
    
    def __post_init__(self):
        self.wrap_asana(Asanas.tadasana.Tadasana())
        self.sets.append(SuryaNamaskar(timings='extra_slow', cnt = 3))
        
        #self.wrap_asana(Asanas.planka.Planka(tm_main = 90))
        self.wrap_asana(Asanas.bakasana.Bakasana())
        self.wrap_asana(Asanas.prasarita_padottanasana.PrasaritaPadottanasana(with_hands = False))
        self.wrap_asana(Asanas.niznii_upor.NizniiUpor())
        self.wrap_asana(Asanas.kobra.KobraWithRotations())
        self.wrap_asana(Asanas.dhanurasana.Dhanurasana())

        self.wrap_asana(Asanas.short_poses.Seli())
        self.wrap_asana(Asanas.baddha_konasana.BaddhaKonasana(tm_progib = 120, with_knees = False))
        #self.wrap_asana(Asanas.perekati_na_spine.Perekatu_na_spine())
        self.wrap_asana(Asanas.marichiasana.Marichiasana())
        self.wrap_asana(Asanas.pashimotanasana.Pashimotanasana())
        #self.wrap_asana(Asanas.dshanu_shirshasana.DshanuShirshasana())
        self.wrap_asana(Asanas.most.Most())
        #self.wrap_asana(Asanas.ushtrasana.Ushtrasana())
        self.wrap_asana(Asanas.malasana.Malasana(tm_main = 80))
        
        self.wrap_asana(Asanas.plug.Plug(tm_main = 110))
        self.wrap_asana(Asanas.dzathara_parivartanasana.Dzathara_Parivartanasana(tm_main = 80))

        #self.wrap_asana(Asanas.navasana.Navasana())
        #self.wrap_asana(Asanas.bakasana.Bakasana(side = 'left'))
        #self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 20))
        #self.wrap_asana(Asanas.bakasana.Bakasana(side = 'right'))
        #self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 20))
                
             
        #self.wrap_asana(Asanas.nakrasana.Nakrasana())

        self.sets.append(KTimerX3())

        #self.wrap_asana(Asanas.sarvangasana.Sarvangasana(tm_main = 80))
        self.wrap_asana(Asanas.shavasana.Shavasana())
        

def do_load_workouts():
    return [DefaultWorkout]