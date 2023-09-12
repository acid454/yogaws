#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  01 test.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from dataclasses import dataclass, field
from base import BaseWorkout, BaseSet
from properties import IntProperty
from tadasana import Tadasana
from planka import Planka
from gorka import GorkaNormal


@dataclass
class DefaultWorkout(BaseWorkout):
    name: str = "default_workout"
    caption: str = "Тестовая тренировка"
    description: str = "Описание тестовой тренировки"
    properties: list = field(default_factory=lambda: [
        IntProperty(caption="test int prop1")])
    
    sets: list = field(default_factory=lambda: [
        BaseSet(visible=False, asanas=[Tadasana()]),
        BaseSet(visible=False, asanas=[Planka()]),
        BaseSet(visible=False, asanas=[GorkaNormal()])])
    

def do_load_workouts():
    return [DefaultWorkout]