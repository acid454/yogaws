#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  perekatu_na_spine.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork
from snd_pools import SND_ZAKONCHILI_DALSHE


class Perekatu_na_spine(BaseAsana):
    def __init__(self, **kwargs):
        BaseAsana.__init__(self, name="perekatu_na_spine", caption="Перекаты на спине")
        self.properties.append(IntProperty(caption="время выполнения", short="tm_main", default=40))
        self.update_props(kwargs)

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=["perekatu_na_spine1"]))
        
        self.pool("name").append("upr_kataemsia_po_spine1")
        self.pool("name").append("upr_kataemsia_po_spine2")
        self.pool("float").append("descr_kataemsia_po_spine1")
        self.pool("float").append("descr_kataemsia_po_spine2")
        self.pool("float").append("descr_kataemsia_po_spine3")
        self.pool("float").append("descr_kataemsia_po_spine4")
        self.pool("end").append(SND_ZAKONCHILI_DALSHE)
