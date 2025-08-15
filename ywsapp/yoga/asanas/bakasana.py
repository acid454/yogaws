#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bakasana.py
#  
#  Copyright 2023 Repnikov Dmitry <acid454@yoga7>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import *


class Bakasana(BaseAsana):
    def __init__(self, side = 'middle', **kwargs):
        if side == 'left':
            _caption = 'Паршва Бакасана\n(левая сторона)'
        elif side == 'right':
            _caption = 'Паршва Бакасана\n(правая сторона)'
        else:
            _caption = 'Бакасана'
        super().__init__(name="bakasana", caption=_caption)
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=13))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=57))
        self.properties.append(IntProperty(caption="выход", short="tm_exit", default=3))
        self.update_props(kwargs)
        
        self.tasks.append(BaseTask(
            caption=self.caption + "\n(подготовка)",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=[f"bakasana{x}" for x in range(1,2)]
        ))
        self.pool("name").append("name_bakasana1")
        self.pool("name").append("name_bakasana2")
        self.pool("name").append("name_bakasana3")
        if side == 'middle':
            self.pool("continue").append("enter_bakasana1", overlapse = True)
            self.pool("continue").append("enter_bakasana2")
        elif side == 'left':
            self.pool("continue").append("left_side1", mandatory = True)
            self.pool("continue").append("left_side2", mandatory = True)
        else:
            self.pool("continue").append("upr_skrutka_vpravo", mandatory = True)


        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images
        ))
        self.pool("continue").append("common_i_postojat'_podushat'", float_on_start = True)
        self.pool("continue").append("descr_ardhachandrasana_common1")
        self.pool("continue").append("descr_ardhachandrasana_zameret'")
        self.pool("float").append("common3")
        self.pool("float").append("common4_dushim_dershimsia")
        self.pool("float").append("common6")
        self.pool("float").append("common7")
        self.pool("float").append("common10")
        self.pool("float").append("common12")
        self.pool("float").append("common_sledim_za_geometriei_kak_zadumanno")
        self.pool("float").append("common_esli_chto_to_ne_poluchaetsia")
        self.pool("float").append("common_ne_zabuvaem_raspredeliat'_ravnovesie")
        self.pool("end").append(SND_COMPLETION_OTHERS + SND_EXHALE + SND_RASSLABILIS)

        self.tasks.append(BaseTask(
            caption=self.caption + "\n(выход)",
            property=self.tm_exit,
            metronome=MetronomeRest(),
            images=self.tasks[-1].images
        ))
        self.pool("end").append(SND_ZAKONCHILI_DALSHE)

    def build(self, workout, _set):
        print(f"Bakasana build, exit time: {self.task(self.tm_exit).property.value}")
        super().build(workout, _set)
        prev_asana = workout.prev_item(self)
        if issubclass(type(prev_asana), Bakasana):
            t = self.task(self.tm_prepare)
            t.pool("start").clear()
            t.pool("start").append(SND_NA_DRUGUJU_STORONU)
            return
    