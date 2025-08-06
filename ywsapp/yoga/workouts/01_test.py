#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  01 test.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseWorkout
from asanas import Asanas
from surya_namaskar import SuryaNamaskar
from hermes import HermesGymnastics
from ktimer import KTimerX3


class DefaultWorkout(BaseWorkout):
    def __init__(self):
        BaseWorkout.__init__(self,
                             name = "test_workout",
                             caption = "Тестовая тренировка",
                             description = "Для тестирования асан")
    

        #self.wrap_asana(Asanas.baddha_konasana.BaddhaKonasana(with_knees = False))
        self.wrap_asana(Asanas.kapotasana.KapotasanaLeft(go_down = True, tm_main = 50, tm_down = 50))
        self.wrap_asana(Asanas.kapotasana.KapotasanaRight(go_down = True, tm_main = 50, tm_down = 50))

        self.wrap_asana(Asanas.virabhadrasana.VirabhadrasanaLeft(go_down = True, tm_main = 40))
        self.wrap_asana(Asanas.virabhadrasana.VirabhadrasanaRight(go_down = True, tm_main = 40))

        self.wrap_asana(Asanas.short_poses.Seli())
        self.wrap_asana(Asanas.shavasana.Shavasana(tm_main = 5))


def do_load_workouts():
    return [DefaultWorkout]