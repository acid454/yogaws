#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  20_neck_and_shoulders_long.py
#  
#  Copyright 2025 Dmitry Repnikov <acid454@yoga7>
#  

from dataclasses import dataclass
from base import BaseWorkout
from asanas import Asanas
from surya_namaskar import SuryaNamaskar


@dataclass
class DefaultWorkout(BaseWorkout):
    name: str = "neck_and_shoulders_long"
    caption: str = "Шея и плечи #2 увеличенная"
    description: str = "Медленная тренировка для расслабления мышц шеи и плеч, увеличенная версия"
    
    def __post_init__(self):
        self.wrap_asana(Asanas.tadasana.Tadasana())
        self.sets.append(SuryaNamaskar(cnt = 1, timings = 'extra_slow'))
        self.wrap_asana(Asanas.uttanasana.Uttanasana_ruki_v_zamke(tm_main = 50, tm_zamok = 30))

        #self.wrap_asana(Asanas.planka.PlankaWithRotationsEx())
        #self.wrap_asana(Asanas.planka.Planka(tm_main = 60))
        self.wrap_asana(Asanas.planka.PlankaWithLegs(tm_main = 60))
        self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 10, tm_prepare = 5, metronome_rest = True))
        self.wrap_asana(Asanas.kobra.KobraWithRotations(tm_main = 60, tm_left = 20, tm_right = 20))
        self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 20, metronome_rest = True))

        self.wrap_asana(Asanas.short_poses.Nogi_k_Rukam())
        self.wrap_asana(Asanas.uttanasana.Uttanasana_ruki_v_zamke(tm_main = 50, tm_zamok = 30))
        self.wrap_asana(Asanas.short_poses.Seli())

        self.wrap_asana(Asanas.markatasana.MarkatasanaWithLegs())
        self.wrap_asana(Asanas.marichiasana.Marichiasana())
        self.wrap_asana(Asanas.stol.Stol())
        self.wrap_asana(Asanas.plug.Plug(tm_main = 60))
        self.wrap_asana(Asanas.malasana.Malasana(with_complication = False))
        self.wrap_asana(Asanas.matjasana.Matjasana())
        self.wrap_asana(Asanas.ushtrasana.Ushtrasana(tm_main = 50))
        self.wrap_asana(Asanas.short_poses.PodnimaemsiaVvreh())

        self.wrap_asana(Asanas.vitjashenie_vverh.VitjashenieVverh(tm_main = 30))
        self.wrap_asana(Asanas.uttanasana.Uttanasana_ruki_v_zamke(tm_main = 70, tm_zamok = 30))

        self.wrap_asana(Asanas.short_poses.Seli())
        self.wrap_asana(Asanas.kobra.Kobra(tm_main = 50))
        self.wrap_asana(Asanas.pashimotanasana.Pashimotanasana(tm_main = 200))
        self.wrap_asana(Asanas.marichiasana.Marichiasana(tm_main = 110))
        self.wrap_asana(Asanas.plug.Plug(tm_main = 50))
        self.wrap_asana(Asanas.perekati_na_spine.Perekatu_na_spine())
        self.wrap_asana(Asanas.plug.Plug(tm_main = 70))
        self.wrap_asana(Asanas.matjasana.Matjasana())

        self.wrap_asana(Asanas.pashimotanasana.Pashimotanasana())
        self.wrap_asana(Asanas.stol.Stol())
        self.wrap_asana(Asanas.most.Most())
        self.wrap_asana(Asanas.dzathara_parivartanasana.Dzathara_Parivartanasana())
        self.wrap_asana(Asanas.kapalabhati.Kapalabhati(tm_main = 70))
        self.wrap_asana(Asanas.uddijana_bandha.UddijanaBandha())

        self.wrap_asana(Asanas.shavasana.Shavasana())

def do_load_workouts():
    return [DefaultWorkout]