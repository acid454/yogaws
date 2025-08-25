#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  13 evening_20.py
#  
#  Copyright 2024 Dmitry Repnikov <acid454@x220>
#  

from dataclasses import dataclass
from base import BaseWorkout
from asanas import Asanas
from surya_namaskar import SuryaNamaskar
from sobaki import Sobaki


@dataclass
class DefaultWorkout(BaseWorkout):
    name: str = "evening_20"
    caption: str = "20 вечерних минут"
    description: str = "Быстрая тренировка с минимальным временем фиксации асан"
    group: str = "Утренние и вечерние"
    
    def __post_init__(self):
        self.wrap_asana(Asanas.tadasana.Tadasana(tm_main = 20))
        self.wrap_asana(Asanas.vitjashenie_vverh.VitjashenieVverh(tm_main = 20))
        self.wrap_asana(Asanas.uttanasana.Uttanasana(tm_main = 45))

        self.sets.append(SuryaNamaskar(timings = 'fast', cnt = 3))
        
        self.wrap_asana(Asanas.short_poses.Seli())
        self.wrap_asana(Asanas.shirokii_razvorot_nazad.ShirokiiRazvorotNazad())
        self.wrap_asana(Asanas.markatasana.Markatasana(cycles_count = 5, cycles_twist = 2))
        self.wrap_asana(Asanas.malasana.Malasana(tm_main = 10))

        self.sets.append(Sobaki(timings = 'fast', transitions = 'up', cycles_count = 4))
        self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 10, metronome_rest = True))
        self.wrap_asana(Asanas.kobra.KobraWithRotations())
        self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 10, metronome_rest = True))

        self.wrap_asana(Asanas.short_poses.Prizhok_k_Rukam())
        self.wrap_asana(Asanas.short_poses.Seli())
        self.wrap_asana(Asanas.marichiasana.Marichiasana(tm_main = 15))
        self.wrap_asana(Asanas.short_poses.LoshimsiaNaSpinu())
        self.wrap_asana(Asanas.plug.Plug(tm_main = 10))
        self.wrap_asana(Asanas.dzathara_parivartanasana.Dzathara_Parivartanasana(tm_main = 15))

        self.wrap_asana(Asanas.malasana.Malasana(with_complication = False, tm_main = 10))
        self.wrap_asana(Asanas.bakasana.Bakasana(tm_main = 20))
        self.wrap_asana(Asanas.planka.Planka(tm_main = 15))

        self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 10, metronome_rest = True))
        self.wrap_asana(Asanas.short_poses.Nogi_k_Rukam())
        self.wrap_asana(Asanas.ardhachandrasana.ArdhachandrasanaLeft())
        self.wrap_asana(Asanas.ardhachandrasana.ArdhachandrasanaRight())

        self.wrap_asana(Asanas.short_poses.Seli())
        self.wrap_asana(Asanas.baddha_konasana.BaddhaKonasana(with_knees = False, tm_main = 15))
        self.wrap_asana(Asanas.most.Most(tm_main = 20))
        self.wrap_asana(Asanas.plug.Plug(tm_main = 20))
        self.wrap_asana(Asanas.marichiasana.Marichiasana(tm_main = 15))

        self.wrap_asana(Asanas.stol.Stol(tm_main = 20))
        self.wrap_asana(Asanas.short_poses.PodnimaemsiaVvreh())
        self.wrap_asana(Asanas.utkatasana.Utkatasana())
        self.wrap_asana(Asanas.kapalabhati.Kapalabhati(tm_main = 70))

        # 
        # self.wrap_asana(Asanas.marichiasana.Marichiasana())

        # #self.wrap_asana(Asanas.ushtrasana.Ushtrasana())
        # #self.wrap_asana(Asanas.navasana.Navasana())
        
        # self.wrap_asana(Asanas.plug.Plug())
        # self.wrap_asana(Asanas.nakrasana.Nakrasana())

        #self.wrap_asana(Asanas.sarvangasana.Sarvangasana())
        self.wrap_asana(Asanas.shavasana.Shavasana())


def do_load_workouts():
    return [DefaultWorkout]