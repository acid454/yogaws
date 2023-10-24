#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  base.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

import os, jsons
from dataclasses import dataclass, field
from speech_manager import SpeechManager


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
    
    def build(self, workout, _set):
        while any(list(map(lambda x: x.build(workout, _set), self.tasks))):
            pass
        return False

    # Удобно брать пул последней таски
    def pool(self, name):
        return self.tasks[-1].pool(name)


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

@dataclass
class SoundPool:
    name: str = None
    files: list = field(default_factory=lambda: [])
    seq: int = 0

    def append(self, x):
        self.files.append(x)
    
    def remove(self, x):
        try:
            self.files.remove(x)
        except:
            pass

@dataclass
class MetronomeSounds:
    tick: str = "tick_rest"
    bell: str = "task_complete_norm"

@dataclass
class BaseTask:
    caption: str = "Без названия"
    property: BaseProperty = None       # instead of value
    metronome: MetronomeSounds = field(default_factory=lambda: MetronomeSounds())
    images: list = field(default_factory=lambda: [])
    snd_pools: list = field(default_factory=lambda: [])
    sounds: dict = field(default_factory=lambda: {})

    def pool(self, name):
        for p in self.snd_pools:
            if p.name == name:
                return p
        self.snd_pools.append(SoundPool(name=name))
        return self.snd_pools[-1]

    def build(self, workout, _set):
        #print("Build method for task '%s' - empty"%(self.caption))
        return False

@dataclass
class BaseSet(PropertiesContainer):
    caption: str = None
    visible: bool = True
    asanas: list = field(default_factory=lambda: [])

    def build(self, workout):
        while any(list(map(lambda x: x.build(workout, self), self.asanas))):
            pass
        return False

@dataclass
class BaseWorkout(PropertiesContainer):
    name: str = "noname"
    caption: str = "Без названия"
    description: str = "Без описания"
    id: str = None
    #properties: list = field(default_factory=lambda: [])
    sets: list = field(default_factory=lambda: [])

    # Добавляем сет, не отображаемый в интерфейсе, с одной асаной
    def wrap_asana(self, asana):
        self.sets.append(BaseSet(visible=False, asanas=[asana]))

    # Возвращаем предыдущий таск или асану (в зависимости от того, что передано через this)
    #  (возможно, в предыдущей асане или даже сете)
    def prev_item(self, this):
        prev_asana = None
        prev_task = None

        for s in self.sets:
            for a in s.asanas:
                if a == this:
                    return prev_asana
                prev_asana = a
                for t in a.tasks:
                    if t == this:
                        return prev_task
                    prev_task = t

    def build(self, _id):
        self.id = _id
        while any(list(map(lambda x: x.build(self), self.sets))):
            pass
        return jsons.dump(self)

@dataclass
class AsanaLegForward(BaseAsana):
    side: str = None