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
from ktimer import KTimer, KTimerX3


class DefaultWorkout(BaseWorkout):
    def __init__(self):
        BaseWorkout.__init__(self,
                             name = "test_workout",
                             caption = "Тестовая тренировка",
                             description = "Для тестирования асан")
    
        self.wrap_asana(Asanas.short_poses.LoshimsiaNaSpinu())
        #self.sets.append(KTimer(subcaption=" (нормальный)", cnt=22))
        #self.sets.append(KTimer(subcaption=" (замедленный)", tm_action=5, cnt=13))
        #self.sets.append(KTimer(subcaption=" (быстрый)", tm_action=1, tm_relax=1, cnt=10))
        
        #self.sets.append(KTimerX3())
        #self.wrap_asana(Asanas.sarvangasana.Sarvangasana())
        self.wrap_asana(Asanas.shavasana.Shavasana())

def do_load_workouts():
    return [DefaultWorkout]