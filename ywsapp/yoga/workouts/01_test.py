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
    

        self.wrap_asana(Asanas.short_poses.Seli())
        self.wrap_asana(Asanas.malasana.Malasana())
        self.wrap_asana(Asanas.shirokii_razvorot_nazad.ShirokiiRazvorotNazad())
        self.wrap_asana(Asanas.vitjashenie_vpered.VitjashenieVpered())
        self.wrap_asana(Asanas.virabhadrasana3.Virabhadrasana3Left(tm_main = 20))
        self.wrap_asana(Asanas.virabhadrasana3.Virabhadrasana3Right(tm_main = 20))

        self.wrap_asana(Asanas.markatasana.MarkatasanaWithLegs())
        self.wrap_asana(Asanas.gorka.GorkaNormal())
        #self.wrap_asana(Asanas.tadasana.Tadasana())
        #self.wrap_asana(Asanas.baddha_konasana.BaddhaKonasana(with_knees = True))


def do_load_workouts():
    return [DefaultWorkout]