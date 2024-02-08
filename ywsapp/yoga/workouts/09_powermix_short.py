#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  09 powermix short.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from dataclasses import dataclass
from base import BaseWorkout
from asanas import Asanas


@dataclass
class DefaultWorkout(BaseWorkout):
    name: str = "powermix_short"
    caption: str = "Утренняя спокойно-силовая v2"
    description: str = "Медленная силовая утренняя тренровка"
    group: str = "Утренние и вечерние"
    
    def __post_init__(self):
        self.wrap_asana(Asanas.tadasana.Tadasana())
        
        self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 10, tm_prepare = 5))
        self.wrap_asana(Asanas.virabhadrasana.VirabhadrasanaLeft(tm_main = 40))
        #self.wrap_asana(Asanas.padottanasana.PadottanasanaLeft())
        self.wrap_asana(Asanas.parivritta.ParivrittaLeft(tm_main = 40))
        self.wrap_asana(Asanas.virabhadrasana3.Virabhadrasana3Left())
        self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 20))
        self.wrap_asana(Asanas.virabhadrasana.VirabhadrasanaRight(tm_main = 40))
        #self.wrap_asana(Asanas.padottanasana.PadottanasanaRight())
        self.wrap_asana(Asanas.parivritta.ParivrittaRight(tm_main = 40))
        self.wrap_asana(Asanas.virabhadrasana3.Virabhadrasana3Right())

        self.wrap_asana(Asanas.bakasana.Bakasana())
        #self.wrap_asana(Asanas.bakasana.Bakasana(side='left'))
        #self.wrap_asana(Asanas.bakasana.Bakasana(side='right'))

        #self.wrap_asana(Asanas.virabhadrasana3.Virabhadrasana3Left())
        #self.wrap_asana(Asanas.virabhadrasana3.Virabhadrasana3Right())

        self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 10, tm_prepare = 5))
        self.wrap_asana(Asanas.kapotasana.KapotasanaLeft())
        self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 10))
        self.wrap_asana(Asanas.kapotasana.KapotasanaRight())
        self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 10))

        self.wrap_asana(Asanas.ardhachandrasana.ArdhachandrasanaLeft())
        self.wrap_asana(Asanas.ardhachandrasana.ArdhachandrasanaRight())

        self.wrap_asana(Asanas.baddha_konasana.BaddhaKonasana())
        self.wrap_asana(Asanas.ushtrasana.Ushtrasana())
        self.wrap_asana(Asanas.sarvangasana.Sarvangasana())

        self.wrap_asana(Asanas.shavasana.Shavasana())

def do_load_workouts():
    return [DefaultWorkout]