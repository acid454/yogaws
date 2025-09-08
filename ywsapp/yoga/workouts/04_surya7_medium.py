#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  04_surya7_medium.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from dataclasses import dataclass
from base import BaseWorkout
from asanas import Asanas
from surya_namaskar import SuryaNamaskar


@dataclass
class DefaultWorkout(BaseWorkout):
    name: str = "surya7_medium"
    caption: str = "7 сурий средняя"
    description: str = "Разогреться и расслабиться"
    group: str = "Сурья Намаскар"
    
    def __post_init__(self):
        self.wrap_asana(Asanas.tadasana.Tadasana())
        self.sets.append(SuryaNamaskar(cnt = 3))
        self.sets.append(SuryaNamaskar(timings = "fast", cnt = 4))

        self.wrap_asana(Asanas.kapalabhati.Kapalabhati(tm_main = 70))
        self.wrap_asana(Asanas.uddijana_bandha.UddijanaBandha())

        self.wrap_asana(Asanas.gorka.GorkaWithLegs(tm_main = 55, tm_prepare = 5))
        self.wrap_asana(Asanas.parivritta.ParivrittaLeft())
        self.wrap_asana(Asanas.parivritta.ParivrittaRight())
        self.wrap_asana(Asanas.gorka.GorkaBase(metronome_rest = True, tm_main = 10))
        #self.wrap_asana(Asanas.padottanasana.PadottanasanaLeft())
        #self.wrap_asana(Asanas.padottanasana.PadottanasanaRight())
        self.wrap_asana(Asanas.prasarita_padottanasana.PrasaritaPadottanasana(tm_main = 110))
        self.wrap_asana(Asanas.malasana.Malasana(tm_main = 80))
        self.wrap_asana(Asanas.ardhachandrasana.ArdhachandrasanaLeft())
        self.wrap_asana(Asanas.ardhachandrasana.ArdhachandrasanaRight())

        self.wrap_asana(Asanas.short_poses.Seli())
        self.wrap_asana(Asanas.baddha_konasana.BaddhaKonasana())
        self.wrap_asana(Asanas.most.Most())
        self.wrap_asana(Asanas.plug.Plug(tm_main = 110))
        self.wrap_asana(Asanas.dzathara_parivartanasana.Dzathara_Parivartanasana(tm_main = 90))
        

        self.wrap_asana(Asanas.kobra.Kobra(tm_main = 60))
        self.wrap_asana(Asanas.plug.Plug(tm_main = 110))
        self.wrap_asana(Asanas.stol.Stol())
        self.wrap_asana(Asanas.malasana.Malasana(with_complication = False))
        self.wrap_asana(Asanas.dhanurasana.Dhanurasana())
        self.wrap_asana(Asanas.ushtrasana.Ushtrasana())

        # Взято из meditative1
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
        self.wrap_asana(Asanas.uddijana_bandha.UddijanaBandha(cycles = 5))
        self.wrap_asana(Asanas.pashimotanasana.Pashimotanasana(tm_main = 200))
        self.wrap_asana(Asanas.short_poses.LoshimsiaNaSpinu())
        self.wrap_asana(Asanas.plug.Plug(tm_main = 80))

        self.wrap_asana(Asanas.shavasana.Shavasana())

def do_load_workouts():
    return [DefaultWorkout]