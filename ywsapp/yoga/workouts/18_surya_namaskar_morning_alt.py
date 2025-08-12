#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  02_surya_namaskar.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from dataclasses import dataclass
from base import BaseWorkout
from asanas import Asanas
from surya_namaskar import SuryaNamaskar
from ktimer import KTimerX3


@dataclass
class DefaultWorkout(BaseWorkout):
    name: str = "surya_namaskar_morning_alt"
    caption: str = "Сурья Намаскар утренняя медленная"
    description: str = "Сурья Намаскар и несколько основных асан"
    group: str = "Сурья Намаскар"
    
    def __post_init__(self):
        self.wrap_asana(Asanas.tadasana.Tadasana())
        self.sets.append(SuryaNamaskar(cnt = 1, timings = 'extra_slow'))
        self.sets.append(SuryaNamaskar(cnt = 2))

        #self.wrap_asana(Asanas.planka.Planka(tm_main = 90))
        self.wrap_asana(Asanas.planka.PlankaWithLegs(tm_main = 70))

        self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 10, tm_prepare = 5))
        self.wrap_asana(Asanas.kapotasana.KapotasanaLeft())
        self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 10, metronome_rest = True))
        self.wrap_asana(Asanas.kapotasana.KapotasanaRight())
        self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 20, metronome_rest = True))
        self.wrap_asana(Asanas.padottanasana.PadottanasanaLeft())
        self.wrap_asana(Asanas.padottanasana.PadottanasanaRight())

        self.wrap_asana(Asanas.short_poses.Seli())
        self.wrap_asana(Asanas.marichiasana.Marichiasana())
        self.wrap_asana(Asanas.ushtrasana.Ushtrasana())


        self.wrap_asana(Asanas.ardhachandrasana.ArdhachandrasanaLeft())
        self.wrap_asana(Asanas.ardhachandrasana.ArdhachandrasanaRight())
        self.wrap_asana(Asanas.baddha_konasana.BaddhaKonasana(with_knees = False))
        

        self.wrap_asana(Asanas.plug.Plug())

        self.sets.append(KTimerX3())
        self.wrap_asana(Asanas.matjasana.Matjasana())

        #self.wrap_asana(Asanas.sarvangasana.Sarvangasana())
        self.wrap_asana(Asanas.shavasana.Shavasana())

def do_load_workouts():
    return [DefaultWorkout]