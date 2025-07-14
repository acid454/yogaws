#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  17 morning_deep2.py
#  
#  Copyright 2025 Dmitry Repnikov <acid454@x220>
#  

from dataclasses import dataclass
from base import BaseWorkout
from asanas import Asanas
from sobaki import Sobaki


@dataclass
class DefaultWorkout(BaseWorkout):
    name: str = "morning_deep"
    caption: str = "Утренняя медленная #2"
    description: str = "Медленная утренняя тренровка из базовых асан"
    group: str = "Утренние и вечерние"
    
    def __post_init__(self):
        self.wrap_asana(Asanas.tadasana.Tadasana())
        self.wrap_asana(Asanas.vitjashenie_vverh.VitjashenieVverh())
        self.wrap_asana(Asanas.uttanasana.UttanasanaWithCompensation(tm_main = 40, tm_compensation = 20))

        self.wrap_asana(Asanas.short_poses.Seli())
        self.wrap_asana(Asanas.shirokii_razvorot_nazad.ShirokiiRazvorotNazad())
        self.wrap_asana(Asanas.markatasana.MarkatasanaWithLegs(cycles_count = 3, cycles_twist = 5))
        self.wrap_asana(Asanas.baddha_konasana.BaddhaKonasana(with_knees = True))
        self.wrap_asana(Asanas.malasana.Malasana())
        self.wrap_asana(Asanas.ushtrasana.Ushtrasana())

        self.wrap_asana(Asanas.planka.Planka(tm_main = 60))
        self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 30, tm_prepare = 5))
        self.wrap_asana(Asanas.virabhadrasana.VirabhadrasanaLeft(tm_main = 40))
        self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 20))
        self.wrap_asana(Asanas.virabhadrasana.VirabhadrasanaRight(tm_main = 40))
        self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 50))
        
        #self.wrap_asana(Asanas.kapotasana.KapotasanaLeft(tm_main = 45))
        #self.wrap_asana(Asanas.kapotasana.KapotasanaRight(tm_main = 45))
        #self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 20))
        #self.sets.append(Sobaki(timings = 'slow', first_gorka_tm = 30, cnt = 3))
        self.wrap_asana(Asanas.kobra.KobraWithRotations())

        self.wrap_asana(Asanas.short_poses.Seli())
        self.wrap_asana(Asanas.pashimotanasana.Pashimotanasana())
        self.wrap_asana(Asanas.marichiasana.Marichiasana())
        self.wrap_asana(Asanas.perekati_na_spine.Perekatu_na_spine())
        self.wrap_asana(Asanas.plug.Plug())
        self.wrap_asana(Asanas.shavasana.Shavasana())

def do_load_workouts():
    return [DefaultWorkout]