#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  02_surya_namaskar.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseWorkout
from properties import IntProperty


class DefaultWorkout(BaseWorkout):
    def __init__(self):
        BaseWorkout.__init__(self,
                             name = "surya_namaskar",
                             caption = "Сурья Намаскар")
    
        self.properties.append(IntProperty(caption="количество циклов", short="cnt", default=9))
        
    def view(self):
        for _ in range(self.get_prop("cnt").value):
            self.asanas.append("test_asana")
        return super().view()

def do_load_workouts():
    return [DefaultWorkout]