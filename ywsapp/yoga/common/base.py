#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  base.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

import datetime
from dataclasses import dataclass, field
from integer_constants import MetronomeTicks


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
class VisibleElement:
    id: str = None
    caption: str = None
    preview_img: str = None

@dataclass
class BaseAsana(PropertiesContainer, VisibleElement):
    name: str = None
    tasks: list = field(default_factory=lambda: [])
    
    def build(self, workout, _set):
        self.id = "%s.%03d"%(self.__class__.__name__, _set.asanas.index(self))
        for t_idx in range(len(self.tasks)):
            self.tasks[t_idx].id = "%s.%s.%03d"%(self.id, self.tasks[t_idx].__class__.__name__, t_idx)
        
        for task in self.tasks:
            task.build(workout, _set)

        for prp in self.properties:
            prp.gen_id(workout.name, _set.id, self.id )
        
        return False

    # Удобно брать пул последней задачи
    def pool(self, name):
        return self.tasks[-1].pool(name)

    def update_all_tasks_images(self, imgs):
        for t in self.tasks:
            t.images = imgs
    
    def task(self, property):
        for t in self.tasks:
            if t.property is property:
                return t
    
    # Используется, если после этого перехода идёт таймерное упражнение типа циклов дыхания (которые без названия)
    def set_name_sound(self, name):
        self.pool("name").clear()
        self.pool("name").append(name)
    
    # Используется для перехода на активность
    def set_bell(self, bell):
        self.tasks[-1].metronome.bell = bell
    
    def set_images(self, images):
        self.tasks[-1].images = images

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

    # Append None, string (sound name), or list with names
    def append(self, x, **kwargs):
        if x is None:
            self.can_be_empty = True
            return

        lst = x if isinstance(x, list) else [x]
        for i in lst:
            itm = {}
            for k in kwargs:
                itm[k] = kwargs[k]
            itm['file'] = i
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
    id: str = None
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
        if (workout.user is None) or (workout.user.metronome == MetronomeTicks.FULL):
            return

        from metronomes import MetronomeKapalabhati
        if isinstance(self.metronome, MetronomeKapalabhati):
            return
        
        self.metronome.tick = "none"
        if workout.user.metronome == MetronomeTicks.NONE:
            self.metronome.bell = "none"
            
        return
    
    def __enter__(self):
        return self
    
    def __exit__(self, type, value, traceback):
        pass

@dataclass
class BaseSet(PropertiesContainer, VisibleElement):
    visible: bool = True        # Видно ли название самого сета (вместо входящих в него асан)
    asanas: list = field(default_factory=lambda: [])

    def update_props(self, kwargs):
        PropertiesContainer.update_props(self, kwargs)
        if 'subcaption' in kwargs.keys():
            self.caption += kwargs['subcaption']

    def build(self, workout, *args):
        self.id = "set%03d"%(workout.sets.index(self))
        if self.preview_img is None:
            self.preview_img = self.asanas[0].tasks[0].images[0]
        if self.asanas[0].preview_img is None:
            self.asanas[0].preview_img = self.asanas[0].tasks[0].images[0]
        
        for a in self.asanas:
            a.build(workout, self)
        return False

@dataclass
class BaseWorkout(PropertiesContainer):
    name: str = "noname"
    caption: str = "Без названия"
    description: str = "Без описания"
    id: str = None
    #properties: list = field(default_factory=lambda: [])
    sets: list = field(default_factory=lambda: [])
    group: str = None
    timetable: list = None
    schedule: list = None
    sound_id: str = None

    # Добавляем сет, не отображаемый в интерфейсе, с одной асаной
    def wrap_asana(self, asana):
        self.sets.append(BaseSet(visible=False, asanas=[asana]))

    # Возвращаем предыдущий таск или асану (в зависимости от того, что передано через this)
    #  (возможно, в предыдущей асане или даже сете)
    def prev_item(self, this):
        prev_set = None
        prev_asana = None
        prev_task = None

        for s in self.sets:
            if s == this:
                return prev_set
            prev_set = s
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

    def build(self, _user, _id):
        self.id = _id
        self.user = _user
        
        # Watch for deletions, and also appends
        while not all(list(map(lambda x: getattr(x, 'build_complete', False), self.sets))):
            for s in self.sets:
                if getattr(s, 'build_complete', False):
                    continue
                
                len_before = len(self.sets)
                s.build(self)
                s.build_complete = True
                if len(self.sets) != len_before:
                    break
        for s in self.sets:
            del s.build_complete

        
        del self.user
        
        # Calc total workout time, and times for each asanas
        self.total_time_int = 0
        self.timetable = {}
        for s in self.sets:
            for a in s.asanas:
                for t in a.tasks:
                    self.timetable[self.total_time_int] = t
                    self.total_time_int += t.property.value
        
        # Pre-Calc task timing list for web engine
        self.schedule = []
        for i in range(self.total_time_int):
            self.schedule.append( max( list(filter( lambda x: x <= i, self.timetable.keys() )) ) )


        self.total_time_str = str(datetime.timedelta(seconds=self.total_time_int))
        if self.total_time_str.startswith("0:"):
            self.total_time_str = self.total_time_str[2:]
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
    SIDE_LEFT = "left"
    SIDE_RIGHT = "right"

    def is_prev_asana_same_leg(self, workout):
        prev_asana = workout.prev_item(self)
        if issubclass(type(prev_asana), AsanaLegForward):
            return prev_asana.side == self.side
        return False
