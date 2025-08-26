#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  21 meditative.py
#  
#  Copyright 2025 Dmitry Repnikov <acid454@x220>
#  

from dataclasses import dataclass
from base import BaseWorkout
from asanas import Asanas
from surya_namaskar import SuryaNamaskar



@dataclass
class DefaultWorkout(BaseWorkout):
    name: str = "meditative_1"
    caption: str = "Медитативная медленная"
    description: str = "Медленная тренировка с небольшим количеством базовых асан"
   
    def __post_init__(self):
        self.wrap_asana(Asanas.tadasana.Tadasana())
        self.sets.append(SuryaNamaskar(timings = 'extra_slow', cnt = 1))

        self.wrap_asana(Asanas.planka.Planka(tm_main = 40))
        self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 10))
        self.wrap_asana(Asanas.kapotasana.KapotasanaLeft(tm_main = 50))
        self.wrap_asana(Asanas.kapotasana.KapotasanaRight(tm_main = 50))

        self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 10, metronome_rest = True))
        self.wrap_asana(Asanas.short_poses.Nogi_k_Rukam())
        self.wrap_asana(Asanas.uttanasana.Uttanasana(tm_main = 90))

        self.wrap_asana(Asanas.kobra.Kobra(tm_main = 60))
        self.wrap_asana(Asanas.short_poses.UshliNaChetverenki())
        self.wrap_asana(Asanas.malasana.Malasana(with_complication = False))
        self.wrap_asana(Asanas.short_poses.Seli())
        self.wrap_asana(Asanas.baddha_konasana.BaddhaKonasana())
        self.wrap_asana(Asanas.marichiasana.Marichiasana())
        self.wrap_asana(Asanas.kapalabhati.Kapalabhati(tm_main = 70))
        self.wrap_asana(Asanas.uddijana_bandha.UddijanaBandha())
        self.wrap_asana(Asanas.pashimotanasana.Pashimotanasana(tm_main = 200))

        self.wrap_asana(Asanas.short_poses.LoshimsiaNaSpinu())
        self.wrap_asana(Asanas.most.Most())
        self.wrap_asana(Asanas.plug.Plug(tm_main = 110))
        self.wrap_asana(Asanas.dzathara_parivartanasana.Dzathara_Parivartanasana(tm_main = 90))

        # Переворачиваемся на живот здесь
        self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 10, metronome_rest = True))
        self.wrap_asana(Asanas.kobra.KobraWithRotations(tm_main = 60))
        self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 10, metronome_rest = True))
        self.wrap_asana(Asanas.short_poses.Nogi_k_Rukam())
        self.wrap_asana(Asanas.uttanasana.Uttanasana(tm_main = 90))

        self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 10, metronome_rest = True))
        self.wrap_asana(Asanas.kapotasana.KapotasanaLeft(go_down = True, tm_main = 50, tm_down = 50))
        self.wrap_asana(Asanas.kapotasana.KapotasanaRight(go_down = True, tm_main = 50, tm_down = 50))
        self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 50))
        
        self.wrap_asana(Asanas.short_poses.Nogi_k_Rukam())
        self.wrap_asana(Asanas.short_poses.Seli())
        self.wrap_asana(Asanas.marichiasana.Marichiasana())
        self.wrap_asana(Asanas.kapalabhati.Kapalabhati(tm_main = 70))
        self.wrap_asana(Asanas.uddijana_bandha.UddijanaBandha())
        self.wrap_asana(Asanas.pashimotanasana.Pashimotanasana(tm_main = 200))
        self.wrap_asana(Asanas.short_poses.LoshimsiaNaSpinu())
        self.wrap_asana(Asanas.plug.Plug(tm_main = 80))


        self.wrap_asana(Asanas.shavasana.Shavasana())



def do_load_workouts():
    return [DefaultWorkout]