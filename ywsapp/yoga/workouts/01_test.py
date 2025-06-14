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
    

        self.wrap_asana(Asanas.planka.PlankaWithRotationsEx())
        self.wrap_asana(Asanas.uttanasana.Uttanasana_ruki_v_zamke(tm_main = 10, tm_zamok = 10))
        self.wrap_asana(Asanas.plug.Plug())
        self.wrap_asana(Asanas.marichiasana.Marichiasana())
        self.wrap_asana(Asanas.shavasana.Shavasana())
        self.wrap_asana(Asanas.planka.Planka(tm_main = 900))
        #self.wrap_asana(Asanas.tadasana.Tadasana())
        #self.wrap_asana(Asanas.baddha_konasana.BaddhaKonasana(with_knees = True))


def do_load_workouts():
    return [DefaultWorkout]