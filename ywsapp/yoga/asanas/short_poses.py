#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  short_poses.py
#   Короткие переходы типа сели, опустились на колени и тп
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask, SoundPool
from properties import IntProperty
from metronomes import MetronomeRest
from snd_pools import SND_OPUSTILIS_NA_KOLENI, SND_SELI


class OpustilisNaKoleni(BaseAsana):
    def __init__(self, **kwargs):
        super().__init__(name="opustilis_na_koleni", caption="Опустились на колени")
        self.properties.append(IntProperty(caption="время перехода", short="tm_main", default=5))
        self.update_props(kwargs)

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeRest(),
            images=["opustilis_na_koleni1", "opustilis_na_koleni2"]
        ))
        
        for i in SND_OPUSTILIS_NA_KOLENI:
            self.pool("start").append(i)


class Seli(BaseAsana):
    def __init__(self, **kwargs):
        super().__init__(name="seli", caption="Садимся")
        self.properties.append(IntProperty(caption="время перехода", short="tm_main", default=5))
        self.update_props(kwargs)

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeRest(),
            images=["seli1", "seli2", "seli3"]
        ))
        
        for i in SND_SELI:
            self.pool("start").append(i)

class PodnimaemsiaVvreh(BaseAsana):
    def __init__(self, **kwargs):
        super().__init__(name="podnimaemsia_vvreh", caption="Поднимаемся вверх")
        self.properties.append(IntProperty(caption="время перехода", short="tm_main", default=6))
        self.update_props(kwargs)

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeRest(),
            images=["tadasana01", "tadasana02"]
        ))
        
        self.pool("start").append("upr_podnimaemsia_vverh1")
        self.pool("start").append("upr_podnimaemsia_vverh2")
        self.pool("start").append("i_skrugliaja_spinu_vverh1")
        self.pool("start").append("i_skrugliaja_spinu_vverh2")
        self.pool("start").append("podnimaemsia1")
        self.pool("start").append("podnimaemsia2")

class LoshimsiaNaSpinu(BaseAsana):
    def __init__(self, **kwargs):
        super().__init__(name="loshimsia_na_spinu", caption="Ложимся на спину")
        self.properties.append(IntProperty(caption="время перехода", short="tm_main", default=4))
        self.update_props(kwargs)

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeRest(),
            images=[f"shavasana{x}" for x in range(1,6)]
        ))
        
        self.pool("start").append("i_loshimsia_na_spinu")
        self.pool("start").append("ukladivaemsia_v_poloshenie_lezha_na_spine")
