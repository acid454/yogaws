#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  shavasana.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeRest
from snd_pools import SND_ZAKONCHILI_DALSHE


class Shavasana(BaseAsana):
    def __init__(self):
        BaseAsana.__init__(self, name="shavasana", caption="Шавасана")
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=90))
        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeRest(),
            images=["shavasana1", "shavasana2", "shavasana3", "shavasana4", "shavasana5"]
        ))
        self.pool("start").append("descr_shavasana1")
        self.pool("start").append("descr_shavasana2")
        self.pool("start").append("descr_shavasana3")
        self.pool("start").append("descr_shavasana4")
        self.pool("start").append("descr_shavasana5")
    
    def build(self, workout):
        BaseAsana.build(self, workout)

        # {% if not glob.get('last_before_shavasana') %}
        end_pool = workout.sets[-2].asanas[-1].tasks[-1].pool("end")
        end_pool.remove("i_dvishemsia_dalshe1")
        end_pool.remove("i_dvishemsia_dalshe2")
        end_pool.remove("i_dvishemsia_dalshe3")


