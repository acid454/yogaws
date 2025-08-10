#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  08 morning_power.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from dataclasses import dataclass
from base import BaseWorkout
from asanas import Asanas
from ktimer import KTimerX3

@dataclass
class DefaultWorkout(BaseWorkout):
    name: str = "morning_deep"
    caption: str = "Утренняя спокойно-силовая"
    description: str = "Медленная силовая утренняя тренровка"
    group: str = "Утренние и вечерние"
    
    def __post_init__(self):
        self.wrap_asana(Asanas.tadasana.Tadasana())
        self.wrap_asana(Asanas.vitjashenie_vverh.VitjashenieVverh(tm_main = 20))
        self.wrap_asana(Asanas.vitjashenie_vpered.VitjashenieVpered(tm_main = 10))
        self.wrap_asana(Asanas.uttanasana.UttanasanaWithCompensation(tm_main = 40, tm_compensation = 20))

        self.wrap_asana(Asanas.planka.PlankaWithRotationsEx(tm_main = 60))
        self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 30, tm_prepare = 5))
        self.wrap_asana(Asanas.virabhadrasana.VirabhadrasanaLeft(go_down = True, tm_main = 30))
        self.wrap_asana(Asanas.virabhadrasana.VirabhadrasanaRight(go_down = True, tm_main = 30))
        self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 10, metronome_rest = True))

        self.wrap_asana(Asanas.sobaka_mordoi_vverh.SobakaMordoiVverh(tm_main = 35))
        #self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 40))
        self.wrap_asana(Asanas.gorka.GorkaWithLegs(tm_main = 40))
        
        self.wrap_asana(Asanas.bakasana.Bakasana())
        self.wrap_asana(Asanas.malasana.Malasana(with_complication = False, tm_main = 80))
        self.wrap_asana(Asanas.navasana.Navasana())
        self.wrap_asana(Asanas.baddha_konasana.BaddhaKonasana(with_knees = False))
        self.wrap_asana(Asanas.stol.Stol())
        self.wrap_asana(Asanas.malasana.Malasana(tm_main = 50))
        self.wrap_asana(Asanas.uttanasana.Uttanasana(tm_main = 40))
        
        self.wrap_asana(Asanas.parivritta.ParivrittaLeft())
        self.wrap_asana(Asanas.parivritta.ParivrittaRight())
        self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 20, metronome_rest = True))

        self.wrap_asana(Asanas.short_poses.Nogi_k_Rukam())
        self.wrap_asana(Asanas.utkatasana.Utkatasana())

        
        self.sets.append(KTimerX3())
        self.wrap_asana(Asanas.plug.Plug())
        #self.wrap_asana(Asanas.sarvangasana.Sarvangasana())
        self.wrap_asana(Asanas.shavasana.Shavasana())

def do_load_workouts():
    return [DefaultWorkout]