#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  22_chest_long.py
#  
#  Copyright 2025 Dmitry Repnikov <acid454@x220>
#  

from dataclasses import dataclass
from base import BaseWorkout
from asanas import Asanas
from surya_namaskar import SuryaNamaskar



@dataclass
class DefaultWorkout(BaseWorkout):
    name: str = "chest_long"
    caption: str = "Общая на грудную клетку"
    description: str = "Медленная тренировка с небольшим количеством базовых асан"
   
    def __post_init__(self):
        self.wrap_asana(Asanas.tadasana.Tadasana())
        self.wrap_asana(Asanas.vitjashenie_vverh.VitjashenieVverh(tm_main = 20))
        self.wrap_asana(Asanas.vitjashenie_vpered.VitjashenieVpered(tm_main = 13))
        self.wrap_asana(Asanas.uttanasana.UttanasanaWithCompensation(tm_main = 40, tm_compensation = 30))

        self.wrap_asana(Asanas.planka.PlankaWithRotationsEx(tm_main = 70))
        self.wrap_asana(Asanas.malasana.Malasana(with_complication = False))
        self.wrap_asana(Asanas.ushtrasana.Ushtrasana())
        self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 55, tm_prepare = 5))

        self.wrap_asana(Asanas.virabhadrasana.VirabhadrasanaLeft(go_down = True, tm_main = 40))
        self.wrap_asana(Asanas.parivritta.ParivrittaLeft(tm_main = 40))
        self.wrap_asana(Asanas.virabhadrasana.VirabhadrasanaRight(go_down = True, tm_main = 40))
        self.wrap_asana(Asanas.parivritta.ParivrittaRight(tm_main = 40))

        self.wrap_asana(Asanas.short_poses.OpustilisNaKoleni())
        self.wrap_asana(Asanas.bakasana.Bakasana())
        self.wrap_asana(Asanas.short_poses.LoshimsiaNaSpinu())
        self.wrap_asana(Asanas.dhanurasana.Dhanurasana())
        self.wrap_asana(Asanas.stol.Stol())
        self.wrap_asana(Asanas.malasana.Malasana(with_complication = False))


        self.wrap_asana(Asanas.gorka.GorkaNormal(tm_main = 10))
        self.wrap_asana(Asanas.kapotasana.KapotasanaLeft(go_down = True, tm_main = 50, tm_down = 65))
        self.wrap_asana(Asanas.kapotasana.KapotasanaRight(go_down = True, tm_main = 50, tm_down = 65))
        self.wrap_asana(Asanas.ushtrasana.Ushtrasana(tm_main = 70))

        self.wrap_asana(Asanas.short_poses.PodnimaemsiaVvreh())
        self.wrap_asana(Asanas.uttanasana.Uttanasana_ruki_v_zamke(tm_main = 30, tm_zamok = 60))

        self.wrap_asana(Asanas.kobra.Kobra(tm_main = 60))
        self.wrap_asana(Asanas.plug.Plug(tm_main = 110))
        self.wrap_asana(Asanas.stol.Stol())
        self.wrap_asana(Asanas.malasana.Malasana(with_complication = False))
        self.wrap_asana(Asanas.dhanurasana.Dhanurasana())
        self.wrap_asana(Asanas.ushtrasana.Ushtrasana())

        self.wrap_asana(Asanas.short_poses.Seli())
        self.wrap_asana(Asanas.baddha_konasana.BaddhaKonasana())
        self.wrap_asana(Asanas.marichiasana.Marichiasana())
        self.wrap_asana(Asanas.pashimotanasana.Pashimotanasana(tm_main = 200))

        self.wrap_asana(Asanas.short_poses.LoshimsiaNaSpinu())
        self.wrap_asana(Asanas.dzathara_parivartanasana.Dzathara_Parivartanasana(tm_main = 90))
        self.wrap_asana(Asanas.plug.Plug(tm_main = 80))
        self.wrap_asana(Asanas.shavasana.Shavasana())



def do_load_workouts():
    return [DefaultWorkout]