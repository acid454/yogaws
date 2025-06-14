#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  14 common1.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseWorkout
from asanas import Asanas
from surya_namaskar import SuryaNamaskar
from ktimer import KTimerX3


class DefaultWorkout(BaseWorkout):
    def __init__(self):
        BaseWorkout.__init__(self,
                             name = "common1",
                             caption = "Общая тренировка",
                             description = "Общая тренировка на растяжку, скрутки и силовую часть")
    
        self.wrap_asana(Asanas.tadasana.Tadasana())
        self.sets.append(SuryaNamaskar(timings = 'extra_slow', cnt = 1))

        self.wrap_asana(Asanas.planka.Planka(tm_main = 90))
        self.wrap_asana(Asanas.pashimotanasana.Pashimotanasana(tm_main = 210))
        self.wrap_asana(Asanas.padottanasana.PadottanasanaLeft())
        self.wrap_asana(Asanas.parivritta.ParivrittaLeft(tm_main = 50))
        self.wrap_asana(Asanas.short_poses.OpustilisNaKoleni())           # Na koleno
        self.wrap_asana(Asanas.padottanasana.PadottanasanaLeft())

        self.wrap_asana(Asanas.padottanasana.PadottanasanaRight())
        self.wrap_asana(Asanas.parivritta.ParivrittaRight(tm_main = 50))
        self.wrap_asana(Asanas.short_poses.OpustilisNaKoleni())           # Na koleno
        self.wrap_asana(Asanas.padottanasana.PadottanasanaRight())

        self.wrap_asana(Asanas.bakasana.Bakasana())
        self.wrap_asana(Asanas.baddha_konasana.BaddhaKonasana(tm_progib = 120))
        self.wrap_asana(Asanas.prasarita_padottanasana.PrasaritaPadottanasana(tm_main = 210, with_hands = False))   # Упавишта конасана
        self.sets[-1].asanas[-1].caption = "Упавишта конасана"
        self.wrap_asana(Asanas.plug.Plug())
        self.wrap_asana(Asanas.nakrasana.Nakrasana())

        self.sets.append(KTimerX3())

        self.wrap_asana(Asanas.sarvangasana.Sarvangasana())
        self.wrap_asana(Asanas.shavasana.Shavasana())



def do_load_workouts():
    return [DefaultWorkout]