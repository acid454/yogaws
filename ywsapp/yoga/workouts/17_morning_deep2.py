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
        self.wrap_asana(Asanas.uttanasana.UttanasanaWithCompensation(tm_main = 50, tm_compensation = 30))

        self.wrap_asana(Asanas.short_poses.Seli())
        self.wrap_asana(Asanas.markatasana.Markatasana())
        self.wrap_asana(Asanas.baddha_konasana.BaddhaKonasana(with_knees = True, tm_main = 160, tm_squared = 80))
        self.wrap_asana(Asanas.malasana.Malasana(with_complication = False, tm_main = 80))
        
        self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 50))
        #self.wrap_asana(Asanas.kobra.KobraWithRotations())
        self.wrap_asana(Asanas.kobra.Kobra(tm_main = 45))
        self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 10, metronome_rest = True))
        self.wrap_asana(Asanas.short_poses.OpustilisNaKoleni())
        self.wrap_asana(Asanas.ushtrasana.Ushtrasana(tm_main = 50))
        self.wrap_asana(Asanas.malasana.Malasana(with_complication = False))
        
        self.wrap_asana(Asanas.short_poses.PodnimaemsiaVvreh())
        self.wrap_asana(Asanas.vitjashenie_vverh.VitjashenieVverh(tm_main = 20))
        self.wrap_asana(Asanas.uttanasana.Uttanasana(tm_main = 90))
        self.wrap_asana(Asanas.virabhadrasana.VirabhadrasanaLeft(tm_main = 50))
        self.wrap_asana(Asanas.virabhadrasana.VirabhadrasanaRight(tm_main = 50))


        self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 10, metronome_rest = True))
        self.wrap_asana(Asanas.short_poses.Nogi_k_Rukam())
        #self.wrap_asana(Asanas.short_poses.LoshimsiaNaSpinu())
        self.wrap_asana(Asanas.short_poses.Seli())

        self.wrap_asana(Asanas.kapalabhati.Kapalabhati(tm_main = 70))
        self.wrap_asana(Asanas.uddijana_bandha.UddijanaBandha())

        #self.wrap_asana(Asanas.plug.Plug())
        self.wrap_asana(Asanas.pashimotanasana.Pashimotanasana(tm_main = 110))
        self.wrap_asana(Asanas.dzathara_parivartanasana.Dzathara_Parivartanasana(tm_main = 95))
        self.wrap_asana(Asanas.perekati_na_spine.Perekatu_na_spine())
        
        #self.wrap_asana(Asanas.kapotasana.KapotasanaLeft(tm_main = 45))
        #self.wrap_asana(Asanas.kapotasana.KapotasanaRight(tm_main = 45))
        #self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 20))
        #self.sets.append(Sobaki(timings = 'slow', first_gorka_tm = 30, cnt = 3))
        
        self.wrap_asana(Asanas.shavasana.Shavasana())

def do_load_workouts():
    return [DefaultWorkout]