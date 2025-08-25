#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  23 morning_five1.py
#  
#  Copyright 2025 Dmitry Repnikov <acid454@yoga7>
#  

from dataclasses import dataclass
from base import BaseWorkout
from asanas import Asanas


@dataclass
class DefaultWorkout(BaseWorkout):
    name: str = "morning_five1"
    caption: str = "5 утренних асан"
    description: str = "Мягкая разминка по утрам"
    group: str = "Утренние и вечерние"
    
    def __post_init__(self):
        self.wrap_asana(Asanas.tadasana.Tadasana())
        self.wrap_asana(Asanas.vitjashenie_vverh.VitjashenieVverh())
        self.wrap_asana(Asanas.uttanasana.UttanasanaWithCompensation(tm_main = 50, tm_compensation = 30))

        # 4 asanas * 90 sec * 4 cycles
        for i in range(3):
             self.wrap_asana(Asanas.virabhadrasana.VirabhadrasanaLeft(tm_main = 25))
             self.wrap_asana(Asanas.kapotasana.KapotasanaLeft(tm_main = 45))
             self.wrap_asana(Asanas.gorka.GorkaBase(tm_main = 7, metronome_rest = True))
             self.wrap_asana(Asanas.virabhadrasana.VirabhadrasanaRight(tm_main = 25))
             self.wrap_asana(Asanas.kapotasana.KapotasanaRight(tm_main = 45))

             self.wrap_asana(Asanas.marichiasana.Marichiasana(tm_main = 40))
             if i == 1:
                 self.wrap_asana(Asanas.kapalabhati.Kapalabhati(tm_main = 70))
             self.wrap_asana(Asanas.plug.Plug(tm_main = 60))
        self.wrap_asana(Asanas.shavasana.Shavasana())


def do_load_workouts():
    return [DefaultWorkout]