#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sobaki.py
#  
#  Copyright 2023 Repnikov Dmitry <acid454@yoga7>
#  

from base import BaseSet
from properties import IntProperty
from asanas import Asanas


class Sobaki(BaseSet):
    TRANSITION_TIMINGS = [
        {'asana':Asanas.gorka.GorkaBase, 'slow':8, 'fast':7, 'extra_slow':13},
        {'asana':Asanas.sobaka_mordoi_vverh.SobakaMordoiVverh, 'slow':8, 'fast':7, 'extra_slow':13}
    ]
    def __init__(self, timings = 'slow', first_gorka_tm = None, **kwargs):
        super().__init__(caption="Переходы Горка - Собака мордой вверх", visible = True)
        self.properties.append(IntProperty(caption="количество циклов", short="cnt", default=6))
        self.update_props(kwargs)
        self.timings = timings
        self.first_gorka_tm = first_gorka_tm
    
    def build(self, workout):
        tarans_tp = None       # For first gorka asana
        first_asana = True
        for i in range(self.cnt.value):
            # Construct new one asana classes every time
            for itm in Sobaki.TRANSITION_TIMINGS:
                if first_asana and self.first_gorka_tm is not None:
                    tm = self.first_gorka_tm
                    first_asana = False
                else:
                    tm = itm[self.timings]
                self.asanas.append(itm['asana'](transition_type = tarans_tp, tm_main = tm))
            
            # We begin with up transition, if was None
            tarans_tp = 'down' if tarans_tp == 'up' else 'up'
        super().build(workout)

