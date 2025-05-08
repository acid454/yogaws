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
    

        self.wrap_asana(Asanas.virabhadrasana.VirabhadrasanaLeft(tm_main = 40))
        self.wrap_asana(Asanas.virabhadrasana.VirabhadrasanaRight(tm_main = 40))
        self.wrap_asana(Asanas.vitjashenie_vverh.VitjashenieVverh(tm_main = 20000))


        self.sets.append(KTimerX3())


def do_load_workouts():
    return [DefaultWorkout]