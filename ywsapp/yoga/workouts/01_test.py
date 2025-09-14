#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  01 test.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from dataclasses import dataclass
from base import BaseWorkout
from asanas import Asanas
from surya_namaskar import SuryaNamaskar
from hermes import HermesGymnastics
from ktimer import KTimerX3


@dataclass
class DefaultWorkout(BaseWorkout):
    name: str = "test_workout"
    caption: str = "Тестовая тренировка"
    description: str = "Для тестирования асан"
    
    def __post_init__(self):
        #self.wrap_asana(Asanas.baddha_konasana.BaddhaKonasana(with_knees = False))
        self.wrap_asana(Asanas.kapotasana.KapotasanaLeft(go_down = True, tm_main = 50, tm_down = 50))
        self.wrap_asana(Asanas.kapotasana.KapotasanaRight(go_down = True, tm_main = 50, tm_down = 50))


def do_load_workouts():
    return [DefaultWorkout]