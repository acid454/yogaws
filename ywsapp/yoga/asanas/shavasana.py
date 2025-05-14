#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  shavasana.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeShavasana
from integer_constants import ShavasanaActing


class Shavasana(BaseAsana):
    def __init__(self):
        BaseAsana.__init__(self, name="shavasana", caption="Шавасана")
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=90))
        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeShavasana(),
            images=[f"shavasana{x}" for x in range(1,6)]
        ))
    
    def build(self, workout, _set):
        super().build(workout, _set)

        end_pool = workout.prev_item(self).pool("end")
        end_pool.remove("i_dvishemsia_dalshe1")
        end_pool.remove("i_dvishemsia_dalshe2")
        end_pool.remove("i_dvishemsia_dalshe3")

        if workout.user is None or workout.user.shavasana_acting != ShavasanaActing.NEVER_ACTING:
            snd_mandatory = True if workout.user is None else (workout.user.shavasana_acting == ShavasanaActing.ALWAYS_ACTING)
            self.pool("name").append("descr_shavasana1", mandatory = snd_mandatory)
            self.pool("name").append("descr_shavasana2", mandatory = snd_mandatory)
            self.pool("name").append("descr_shavasana3", mandatory = snd_mandatory)
            self.pool("name").append("descr_shavasana4", mandatory = snd_mandatory)
            self.pool("name").append("descr_shavasana5", mandatory = snd_mandatory)
        