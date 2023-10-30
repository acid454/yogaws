#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  02_surya_namaskar.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseWorkout
from properties import IntProperty
from asanas import Asanas
from surya_namaskar import SuryaNamaskar


class DefaultWorkout(BaseWorkout):
    def __init__(self):
        BaseWorkout.__init__(self,
                             name = "surya_namaskar",
                             caption = "Сурья Намаскар",
                             description = "Сурья Намаскар и несколько основных асан")
    
        self.wrap_asana(Asanas.tadasana.Tadasana())
        self.sets.append(SuryaNamaskar())
        self.wrap_asana(Asanas.shavasana.Shavasana())

def do_load_workouts():
    return [DefaultWorkout]