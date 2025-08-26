#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  12_surya7_relax.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from dataclasses import dataclass
from base import BaseWorkout
from asanas import Asanas
from surya_namaskar import SuryaNamaskar


@dataclass
class DefaultWorkout(BaseWorkout):
    name: str = "surya7_relax",
    caption: str = "7 сурий и релакс"
    description: str = "Разогреться и расслабиться"
    group: str = "Сурья Намаскар"
    
    def __post_init__(self):
        self.wrap_asana(Asanas.tadasana.Tadasana())
        self.sets.append(SuryaNamaskar(timings = 'slow', cnt = 3))
        self.sets.append(SuryaNamaskar(timings = 'fast', cnt = 4))
        self.wrap_asana(Asanas.kapalabhati.Kapalabhati())
        self.wrap_asana(Asanas.uddijana_bandha.UddijanaBandha())

        #self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 10, tm_prepare = 5))
        #self.wrap_asana(Asanas.parivritta.ParivrittaLeft())
        #self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 10))
        #self.wrap_asana(Asanas.parivritta.ParivrittaRight())
        #self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 10))
        self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 10, tm_prepare = 5))
        self.wrap_asana(Asanas.padottanasana.PadottanasanaLeft())
        self.wrap_asana(Asanas.padottanasana.PadottanasanaRight())
        #self.wrap_asana(Asanas.prasarita_padottanasana.PrasaritaPadottanasana(with_hands = False))

        self.wrap_asana(Asanas.short_poses.Seli())
        self.wrap_asana(Asanas.baddha_konasana.BaddhaKonasana(with_knees = False, tm_main = 120))
        self.wrap_asana(Asanas.malasana.Malasana(tm_main = 70))
        self.wrap_asana(Asanas.kobra.KobraWithRotations())
        self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 10, metronome_rest = True))
        self.wrap_asana(Asanas.kapotasana.KapotasanaLeft(go_down = True, tm_main = 50, tm_down = 50))
        self.wrap_asana(Asanas.kapotasana.KapotasanaRight(go_down = True, tm_main = 50, tm_down = 50))
        self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 10, metronome_rest = True))
        self.wrap_asana(Asanas.short_poses.OpustilisNaKoleni())
        self.wrap_asana(Asanas.ushtrasana.Ushtrasana())

        self.wrap_asana(Asanas.pashimotanasana.Pashimotanasana(tm_main = 180))
        self.wrap_asana(Asanas.marichiasana.Marichiasana())

        self.wrap_asana(Asanas.kapalabhati.Kapalabhati())
        self.wrap_asana(Asanas.uddijana_bandha.UddijanaBandha())
        self.wrap_asana(Asanas.plug.Plug(tm_main = 110))
        self.wrap_asana(Asanas.shavasana.Shavasana())

def do_load_workouts():
    return [DefaultWorkout]