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
    

        self.wrap_asana(Asanas.sukhasana.Sukhasana())
        self.wrap_asana(Asanas.markatasana.MarkatasanaWithLegs())
        self.wrap_asana(Asanas.kapalabhati.Kapalabhati())
        self.wrap_asana(Asanas.uddijana_bandha.UddijanaBandha())
        
        self.wrap_asana(Asanas.shavasana.Shavasana())


def do_load_workouts():
    return [DefaultWorkout]