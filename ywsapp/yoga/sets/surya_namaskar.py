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
    SURYA_TIMINGS = [
        {'asana':Asanas.vitjashenie_vverh.VitjashenieVverh, 'slow':9, 'fast':4, 'extra_slow':11},
        {'asana':Asanas.vitjashenie_vpered.VitjashenieVpered, 'slow':9, 'fast':5, 'extra_slow':11 },
        {'asana':Asanas.uttanasana.UttanasanaWithCompensation, 'slow':(9,6), 'fast':(4,4), 'extra_slow':(30,20)},
        {'asana':Asanas.niznii_upor.NizniiUpor, 'slow':6, 'fast':4, 'extra_slow':12},
        {'asana':Asanas.sobaka_mordoi_vverh.SobakaMordoiVverh, 'slow':11, 'fast':7, 'extra_slow':35},
        {'asana':Asanas.gorka.GorkaBase, 'slow':11, 'fast':7, 'extra_slow':16},
        {'asana':Asanas.virabhadrasana.VirabhadrasanaLeft, 'slow':16, 'fast':12, 'extra_slow':50},
        {'asana':Asanas.gorka.GorkaBase, 'slow':9, 'fast':4, 'extra_slow':16},
        {'asana':Asanas.virabhadrasana.VirabhadrasanaRight, 'slow':16, 'fast':12, 'extra_slow':50},
        {'asana':Asanas.gorka.GorkaBase, 'slow':11, 'fast':4, 'extra_slow':30},
        {'asana':Asanas.nogi_k_rukam.Prizhok_k_Rukam},
        {'asana':Asanas.uttanasana.Uttanasana, 'slow':9, 'fast':4, 'extra_slow':35},
        {'asana':Asanas.short_poses.PodnimaemsiaVvreh}
    ]
    def __init__(self, timings = 'slow', **kwargs):
        super().__init__(caption="Сурья Намаскар")
        self.properties.append(IntProperty(caption="количество циклов", short="cnt", default=9))
        self.update_props(kwargs)
        self.timings = timings
    
    def build(self, workout):
        for i in range(self.cnt.value):
            # Construct new one asana classes every time
            for itm in SuryaNamaskar.SURYA_TIMINGS:
                #print("SURYA construct %s"%(itm['asana']))
                if self.timings in itm.keys():
                    tm = itm[self.timings]
                    if type(tm) == int:
                        self.asanas.append(itm['asana'](tm_main = tm))
                    else:
                        self.asanas.append(itm['asana'](tm_main = tm[0], tm_compensation = tm[1]))
                else:
                    self.asanas.append(itm['asana']())
        
        # Remove PodnimaemsiaVvreh if next asana is Gorka, or Planka
        next_asana = workout.next_item(self.asanas[-1])
        if type(next_asana) in [Asanas.gorka.GorkaBase, Asanas.planka.Planka]:
            del self.asanas[-1]
        super().build(workout)

