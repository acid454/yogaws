#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  11_home_extended2.py
#  
#  Copyright 2023 Repnikov Dmitry <acid454@yoga7>
#  

from dataclasses import dataclass
from base import BaseWorkout
from asanas import Asanas
from ktimer import KTimerX3


@dataclass
class DefaultWorkout(BaseWorkout):
    name: str = "home_extended2"
    caption: str = "Расширенная домашняя тренировка #2"
    description: str = "Комплекс для начального уровня подготовки. Прекращение физической деградации."

    def __post_init__(self):
        self.wrap_asana(Asanas.tadasana.Tadasana())
        self.wrap_asana(Asanas.vitjashenie_vverh.VitjashenieVverh(tm_main = 20))
        self.wrap_asana(Asanas.vitjashenie_vpered.VitjashenieVpered(tm_main = 13))
        self.wrap_asana(Asanas.uttanasana.UttanasanaWithCompensation(tm_main = 40, tm_compensation = 30))

        self.wrap_asana(Asanas.planka.PlankaWithRotationsEx(tm_main = 70))
        self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 55, tm_prepare = 5))

        self.wrap_asana(Asanas.virabhadrasana.VirabhadrasanaLeft(go_down = True, tm_main = 40))
        self.wrap_asana(Asanas.parivritta.ParivrittaLeft(tm_main = 40))
        self.wrap_asana(Asanas.virabhadrasana.VirabhadrasanaRight(go_down = True, tm_main = 40))
        self.wrap_asana(Asanas.parivritta.ParivrittaRight(tm_main = 40))

        self.wrap_asana(Asanas.prasarita_padottanasana.PrasaritaPadottanasana(with_hands = False, tm_main = 110))

        self.wrap_asana(Asanas.short_poses.OpustilisNaKoleni())
        self.wrap_asana(Asanas.bakasana.Bakasana())
        self.wrap_asana(Asanas.dhanurasana.Dhanurasana())
        self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 10, metronome_rest = True))
        self.wrap_asana(Asanas.malasana.Malasana(with_complication = False))

        self.wrap_asana(Asanas.short_poses.Seli())
        self.wrap_asana(Asanas.baddha_konasana.BaddhaKonasana(with_knees = False))
        self.wrap_asana(Asanas.marichiasana.Marichiasana())
        self.wrap_asana(Asanas.dshanu_shirshasana.DshanuShirshasana())
        self.wrap_asana(Asanas.most.Most())

        self.wrap_asana(Asanas.navasana.Navasana())
        self.wrap_asana(Asanas.ushtrasana.Ushtrasana())        
        self.wrap_asana(Asanas.plug.Plug())
        #self.wrap_asana(Asanas.matjasana.Matjasana())
        self.wrap_asana(Asanas.stol.Stol())

        self.wrap_asana(Asanas.malasana.Malasana(with_complication = False))
        self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 10, metronome_rest = True))
        self.wrap_asana(Asanas.kapotasana.KapotasanaLeft(go_down = True, tm_main = 50, tm_down = 50))
        self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 10, metronome_rest = True))
        self.wrap_asana(Asanas.kapotasana.KapotasanaRight(go_down = True, tm_main = 50, tm_down = 50))
        self.wrap_asana(Asanas.gorka.GorkaWithLegs(tm_main = 40))
        
        self.wrap_asana(Asanas.short_poses.Nogi_k_Rukam())
        self.wrap_asana(Asanas.short_poses.Seli())
        self.wrap_asana(Asanas.marichiasana.Marichiasana())
        self.wrap_asana(Asanas.pashimotanasana.Pashimotanasana(tm_main = 150))
        self.wrap_asana(Asanas.short_poses.LoshimsiaNaSpinu())
        self.wrap_asana(Asanas.plug.Plug(tm_main = 80))


        self.wrap_asana(Asanas.nakrasana.Nakrasana())
        self.sets.append(KTimerX3())
        #self.wrap_asana(Asanas.sarvangasana.Sarvangasana())
        self.wrap_asana(Asanas.shavasana.Shavasana())

def do_load_workouts():
    return [DefaultWorkout]