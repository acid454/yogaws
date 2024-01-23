#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  base.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

import datetime
from dataclasses import dataclass, field

@dataclass
class PropertiesContainer:
    properties: list = field(default_factory=lambda: [])
    
    # Use property's short name as attribute of workout
    def __getattr__(self, name):
        for _p in self.properties:
            if _p.short == name:
                return _p
        return None
    
    # Меняем default-значения properties, перечисленных в keys kwargs
    def update_props(self, kwargs):
        for k in kwargs:
            p = self.__getattr__(k)
            if p is not None:
                p.default = kwargs[k]
    
    # Возвращаем экземпляр property по id (для загрузки/сохранения значений)
    def get_prop_by_id(self, _id):
        for p in self.properties:
            if p.id == _id:
                return p
        return None

@dataclass
class BaseAsana(PropertiesContainer):
    name: str = None
    caption: str = None
    tasks: list = field(default_factory=lambda: [])
    id: str = None
    
    def build(self, workout, _set):
        while any(list(map(lambda x: x.build(workout, _set), self.tasks))):
            pass
        
        self.id = "%s.%03d"%(self.__class__.__name__, _set.asanas.index(self))
        for prp in self.properties:
            prp.gen_id(workout.name, _set.id, self.id )
        return False

    # Удобно брать пул последней таски
    def pool(self, name):
        return self.tasks[-1].pool(name)

    def update_all_tasks_images(self, imgs):
        for t in self.tasks:
            t.images = imgs
    
    def task(self, property):
        for t in self.tasks:
            if t.property is property:
                return t


@dataclass
class BaseProperty:
    type: str = None
    caption: str = "Без названия"
    short: str = None
    default = None
    _value = None
    id: str = None  # ID для хранения в БД. Генерируется build-методом асаны или таски.

    #
    # Используем property, если value is None - возвращаем default
    @property
    def value(self):
        return self.default if self._value is None else self._value
    
    @value.setter
    def value(self, v):
        self._value = v

    def gen_id(self, workout, _set, asana):
        self.id = "{workout_id}.{set_id}.{asana_id}.{short}".format(
            workout_id = workout,
            set_id = _set,
            asana_id = asana,
            short = self.short
        )

@dataclass
class SoundPool:
    name: str = None
    items: list = field(default_factory=lambda: [])
    seq: int = 0
    can_be_empty: bool = False

    def append(self, x, **kwargs):
        if x is None:
            self.can_be_empty = True
            return
        itm = kwargs
        itm['file'] = x
        self.items.append(itm)
    
    def remove(self, x):
        for i in self.items:
            try:
                if i['file'] == x:
                    self.items.remove(i)
            except:
                pass
    
    def clear(self):
        self.items.clear()
    
    def migrate(self, src):
        self.items = src.items
        src.items = []

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
        return False
    
    def __enter__(self):
        return self
    
    def __exit__(self, type, value, traceback):
        pass

@dataclass
class BaseSet(PropertiesContainer):
    caption: str = None
    visible: bool = True
    asanas: list = field(default_factory=lambda: [])
    id: str = None

    def build(self, workout):
        self.id = "set%03d"%(workout.sets.index(self))
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

    # Аналогично возвращаем следующий таск или асану
    def next_item(self, this):
        ret_nxt_asana = False
        ret_nxt_task = False

        for s in self.sets:
            for a in s.asanas:
                if a is this:
                    ret_nxt_asana = True
                elif ret_nxt_asana:
                    return a
                for t in a.tasks:
                    if t is this:
                        ret_nxt_task = True
                    elif ret_nxt_task:
                        return t

    # Возвращаем property по id
    def find_property_by_id(self, prop_id):
        for s in self.sets:
            for a in s.asanas:
                p = a.get_prop_by_id(prop_id)
                if p is not None:
                    return p
        return None

    def build(self, _id):
        self.id = _id
        while any(list(map(lambda x: x.build(self), self.sets))):
            pass
        
        total_time = 0
        for s in self.sets:
            for a in s.asanas:
                for t in a.tasks:
                    total_time += t.property.value
        self.total_time = str(datetime.timedelta(seconds=total_time))
        if self.total_time.startswith("0:"):
            self.total_time = self.total_time[2:]
        return self
    
    # Находим и применяем значение property
    def apply_prop(self, prop_id, prop_value):
        prop = self.find_property_by_id(prop_id)
        if prop is None:
            return
        prop.value = prop_value


@dataclass
class AsanaLegForward(BaseAsana):
    side: str = None

@dataclass
class AsanaLegsStayUp(BaseAsana):
    pass