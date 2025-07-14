#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  06_home_extended.py
#  
#  Copyright 2023 Repnikov Dmitry <acid454@yoga7>
#  

from dataclasses import dataclass
from base import BaseWorkout
from asanas import Asanas
from sobaki import Sobaki


@dataclass
class DefaultWorkout(BaseWorkout):
    name: str = "home_extended"
    caption: str = "Расширенная домашняя тренировка"
    description: str = "Непродолжительный комплекс для любого начального уровня подготовки. Прекращение физической деградации."

    def __post_init__(self):
        self.wrap_asana(Asanas.tadasana.Tadasana())
        self.wrap_asana(Asanas.vitjashenie_vverh.VitjashenieVverh())
        self.wrap_asana(Asanas.uttanasana.Uttanasana(tm_main = 45))

        self.wrap_asana(Asanas.short_poses.Seli())
        self.wrap_asana(Asanas.shirokii_razvorot_nazad.ShirokiiRazvorotNazad())
        self.wrap_asana(Asanas.markatasana.MarkatasanaWithLegs(cycles_count = 3, cycles_twist = 5))
        self.wrap_asana(Asanas.stol.Stol())
        self.wrap_asana(Asanas.baddha_konasana.BaddhaKonasana(with_knees = True))

        self.wrap_asana(Asanas.short_poses.PodnimaemsiaVvreh())
        self.wrap_asana(Asanas.vitjashenie_vverh.VitjashenieVverh(tm_main = 15))
        self.wrap_asana(Asanas.vitjashenie_vpered.VitjashenieVpered())
        self.wrap_asana(Asanas.virabhadrasana3.Virabhadrasana3Left(tm_main = 20))
        self.wrap_asana(Asanas.virabhadrasana3.Virabhadrasana3Right(tm_main = 20))

        self.wrap_asana(Asanas.planka.Planka(tm_main = 90))
        self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 55, tm_prepare = 5))

        self.wrap_asana(Asanas.virabhadrasana.VirabhadrasanaLeft(tm_main = 40))
        self.wrap_asana(Asanas.padottanasana.PadottanasanaLeft())
        #self.wrap_asana(Asanas.parivritta.ParivrittaLeft(tm_main = 40))
        
        self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 20))
        self.wrap_asana(Asanas.virabhadrasana.VirabhadrasanaRight(tm_main = 40))
        self.wrap_asana(Asanas.padottanasana.PadottanasanaRight())
        #self.wrap_asana(Asanas.parivritta.ParivrittaRight(tm_main = 40))

        self.wrap_asana(Asanas.short_poses.OpustilisNaKoleni())
        self.wrap_asana(Asanas.bakasana.Bakasana())
        self.wrap_asana(Asanas.dhanurasana.Dhanurasana())

        self.sets.append(Sobaki(timings = 'slow', first_gorka_tm = 30))
        self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 40))

        self.wrap_asana(Asanas.short_poses.Seli())
        
        #self.wrap_asana(Asanas.kukkutasana.Kukkutasana())
        self.wrap_asana(Asanas.marichiasana.Marichiasana())
        self.wrap_asana(Asanas.dshanu_shirshasana.DshanuShirshasana())
        self.wrap_asana(Asanas.most.Most())
        self.wrap_asana(Asanas.navasana.Navasana())
        self.wrap_asana(Asanas.plug.Plug())
        #self.wrap_asana(Asanas.stol.Stol())
        
        #self.wrap_asana(Asanas.ushtrasana.Ushtrasana())
        #self.wrap_asana(Asanas.matjasana.Matjasana())

        self.wrap_asana(Asanas.perekati_na_spine.Perekatu_na_spine())
        self.wrap_asana(Asanas.nakrasana.Nakrasana())

        self.wrap_asana(Asanas.sarvangasana.Sarvangasana())
        self.wrap_asana(Asanas.shavasana.Shavasana())

def do_load_workouts():
    return [DefaultWorkout]