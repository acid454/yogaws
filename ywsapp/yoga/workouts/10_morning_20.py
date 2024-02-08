#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  10 morning_20.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from dataclasses import dataclass
from base import BaseWorkout
from asanas import Asanas


@dataclass
class DefaultWorkout(BaseWorkout):
    name: str = "morning_20"
    caption: str = "20 утренних минут"
    description: str = "Мягкая разминка по утрам"
    group: str = "Утренние и вечерние"
    
    def __post_init__(self):
        self.wrap_asana(Asanas.tadasana.Tadasana())
        self.wrap_asana(Asanas.vitjashenie_vverh.VitjashenieVverh(tm_main = 20))
        self.wrap_asana(Asanas.uttanasana.Uttanasana(tm_main = 45))

        self.wrap_asana(Asanas.niznii_upor.NizniiUpor(tm_main = 20))
        self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 30, tm_prepare = 5))
        self.wrap_asana(Asanas.sobaka_mordoi_vverh.SobakaMordoiVverh(tm_main = 45))
        self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 25))

        self.wrap_asana(Asanas.virabhadrasana.VirabhadrasanaLeft(tm_main = 30))
        self.wrap_asana(Asanas.virabhadrasana.VirabhadrasanaRight(tm_main = 30))
        self.wrap_asana(Asanas.prasarita_padottanasana.PrasaritaPadottanasana(with_hands = False))
        self.wrap_asana(Asanas.parivritta.ParivrittaLeft(tm_main = 40))
        self.wrap_asana(Asanas.parivritta.ParivrittaRight(tm_main = 40))
        

        self.wrap_asana(Asanas.utkatasana.Utkatasana())
        #self.wrap_asana(Asanas.ardhachandrasana.ArdhachandrasanaLeft())
        #self.wrap_asana(Asanas.ardhachandrasana.ArdhachandrasanaRight())
        
        self.wrap_asana(Asanas.baddha_konasana.BaddhaKonasana())
        self.wrap_asana(Asanas.marichiasana.Marichiasana())

        #self.wrap_asana(Asanas.ushtrasana.Ushtrasana())
        #self.wrap_asana(Asanas.navasana.Navasana())
        
        self.wrap_asana(Asanas.perekati_na_spine.Perekatu_na_spine())
        self.wrap_asana(Asanas.nakrasana.Nakrasana())

        self.wrap_asana(Asanas.sarvangasana.Sarvangasana())
        self.wrap_asana(Asanas.shavasana.Shavasana())


def do_load_workouts():
    return [DefaultWorkout]