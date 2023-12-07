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


class DefaultWorkout(BaseWorkout):
    def __init__(self):
        BaseWorkout.__init__(self,
                             name = "test_workout",
                             caption = "Тестовая тренировка",
                             description = "Для тестирования асан")
    
        self.wrap_asana(Asanas.tadasana.Tadasana())
        
        self.wrap_asana(Asanas.bakasana.Bakasana(side='left'))
        self.wrap_asana(Asanas.bakasana.Bakasana(side='right'))

        self.wrap_asana(Asanas.virabhadrasana3.Virabhadrasana3Left())
        self.wrap_asana(Asanas.virabhadrasana3.Virabhadrasana3Right())

        self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 10, tm_prepare = 5))
        self.wrap_asana(Asanas.kapotasana.KapotasanaLeft())
        self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 10))
        self.wrap_asana(Asanas.kapotasana.KapotasanaRight())
        self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 10))

        self.wrap_asana(Asanas.ardhachandrasana.ArdhachandrasanaLeft())
        self.wrap_asana(Asanas.ardhachandrasana.ArdhachandrasanaRight())

        self.wrap_asana(Asanas.shavasana.Shavasana())

def do_load_workouts():
    return [DefaultWorkout]