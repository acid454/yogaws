#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  surya_namaskar.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseSet
from properties import IntProperty
from asanas import Asanas
#from gorka import GorkaBase
#from uttanasana import Uttanasana
#from sobaka_mordoi_vverh import SobakaMordoiVverh


class SuryaNamaskar(BaseSet):
    def __init__(self, slow_timings = True):
        super().__init__(caption="Сурья Намаскар")
        self.properties.append(IntProperty(caption="количество циклов", short="cnt", default=9))
        self.slow_timings = slow_timings
    
    def build(self, workout):
        for i in range(self.cnt.value):
            # Construct new one asana classes every time
            self.asanas += [
                Asanas.vitjashenie_vverh.VitjashenieVverh(tm_main = 9 if self.slow_timings else 4),
                Asanas.vitjashenie_vpered.VitjashenieVpered(tm_main = 9 if self.slow_timings else 5),
                Asanas.uttanasana.UttanasanaWithCompensation(
                    tm_main = 9 if self.slow_timings else 4,
                    tm_compensation = 6 if self.slow_timings else 4
                ),
                Asanas.niznii_upor.NizniiUpor(tm_main = 6 if self.slow_timings else 4),
                Asanas.sobaka_mordoi_vverh.SobakaMordoiVverh(tm_main = 11 if self.slow_timings else 7),
                Asanas.gorka.GorkaBase(tm_main = 11 if self.slow_timings else 7),
                Asanas.virabhadrasana.VirabhadrasanaLeft(tm_main = 16 if self.slow_timings else 12),
                Asanas.gorka.GorkaBase(tm_main = 9 if self.slow_timings else 4),
                Asanas.virabhadrasana.VirabhadrasanaRight(tm_main = 16 if self.slow_timings else 12),
                Asanas.gorka.GorkaBase(tm_main = 11 if self.slow_timings else 4),
                Asanas.nogi_k_rukam.Prizhok_k_Rukam(),
                Asanas.uttanasana.Uttanasana(tm_main = 9 if self.slow_timings else 4)
            ]
        super().build(workout)

