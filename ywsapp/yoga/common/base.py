#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  base.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

import os, jsons
from dataclasses import dataclass, field

BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@dataclass
class PropertiesContainer:
    properties: list = field(default_factory=lambda: [])
    
    # Use property's short name as attribute of workout
    def __getattr__(self, name):
        for _p in self.properties:
            if _p.short == name:
                return _p
        return None


@dataclass
class BaseAsana(PropertiesContainer):
    name: str = None
    caption: str = None
    tasks: list = field(default_factory=lambda: [])
    #properties: list = field(default_factory=lambda: [])

@dataclass
class BaseProperty:
    type: str = None
    caption: str = "Без названия"
    short: str = None
    default = None
    _value = None

    #
    # Используем property, если value is None - возвращаем default
    @property
    def value(self):
        return self.default if self._value is None else self._value
    
    @value.setter
    def value(self, v):
        self._value = v

#@dataclass
#class SoundsContainer:

@dataclass
class MetronomeSounds:
    tick: int = 0
    bell: int = 0

@dataclass
class BaseTask:
    caption: str = "Без названия"
    property: BaseProperty = None       # instead of value
    metronome: MetronomeSounds = field(default_factory=lambda: MetronomeSounds())
    images: list = field(default_factory=lambda: [])
    sounds: list = field(default_factory=lambda: [])    #ToDo: will be reworked

@dataclass
class BaseSet(PropertiesContainer):
    caption: str = None
    asanas: list = field(default_factory=lambda: [])

@dataclass
class BaseWorkout(PropertiesContainer):
    name: str = "noname"
    caption: str = "Без названия"
    description: str = "Без описания"
    #properties: list = field(default_factory=lambda: [])
    asanas: list = field(default_factory=lambda: [])

    def view(self):
        return jsons.dump(self)
	