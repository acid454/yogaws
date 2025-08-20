#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  short_poses.py
#   Короткие переходы типа сели, опустились на колени и тп
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeRest, MetronomeWork
from snd_pools import SND_OPUSTILIS_NA_KOLENI, SND_USHLI_NA_CHETVERENKI, SND_SELI


class OpustilisNaKoleni(BaseAsana):
    IMAGES = ["opustilis_na_koleni1", "opustilis_na_koleni2"]
    def __init__(self, **kwargs):
        super().__init__(name="opustilis_na_koleni", caption="Опустились на колени")
        self.properties.append(IntProperty(caption="время перехода", short="tm_main", default=5))
        self.update_props(kwargs)

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeRest(),
            images=OpustilisNaKoleni.IMAGES
        ))
        self.pool("name").append(SND_OPUSTILIS_NA_KOLENI + SND_USHLI_NA_CHETVERENKI)

class UshliNaChetverenki(BaseAsana):
    def __init__(self, **kwargs):
        super().__init__(name="ushli_na_chetverenki", caption="Переход на четвереньки")
        self.properties.append(IntProperty(caption="время перехода", short="tm_main", default=5))
        self.update_props(kwargs)

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeRest(),
            images=OpustilisNaKoleni.IMAGES
        ))
        self.pool("name").append(SND_USHLI_NA_CHETVERENKI)

class Seli(BaseAsana):
    IMAGES = [f"seli{n}" for n in range(1,4)]
    def __init__(self, **kwargs):
        super().__init__(name="seli", caption="Садимся")
        self.properties.append(IntProperty(caption="время перехода", short="tm_main", default=5))
        self.update_props(kwargs)

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeRest(),
            images=Seli.IMAGES
        ))
        self.pool("name").append(SND_SELI)

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
        
        self.pool("name").append("upr_podnimaemsia_vverh1")
        self.pool("name").append("upr_podnimaemsia_vverh2")
        self.pool("name").append("i_skrugliaja_spinu_vverh1")
        self.pool("name").append("i_skrugliaja_spinu_vverh2")
        self.pool("name").append("i_skrugliaja_spinu_vverh3")
        self.pool("name").append("i_skrugliaja_spinu_vverh4")
        self.pool("name").append("podnimaemsia1")
        self.pool("name").append("podnimaemsia2")

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
        
        self.pool("name").append("i_loshimsia_na_spinu")
        self.pool("name").append("ukladivaemsia_v_poloshenie_lezha_na_spine")

class Nogi_k_Rukam(BaseAsana):
    def __init__(self, **kwargs):
        BaseAsana.__init__(self, name="nogi_k_rukam", caption="Подходим ногами к рукам")
        self.properties.append(IntProperty(caption="время выполнения", short="tm_main", default=4))
        self.update_props(kwargs)

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=["nogi_k_rukam1"]))
        
        self.pool("name").append("i_podoshli_nogami_k_rukam")

class Prizhok_k_Rukam(BaseAsana):
    def __init__(self, **kwargs):
        BaseAsana.__init__(self, name="prizhok_k_rukam", caption="Прыжок к ладоням рук")
        self.properties.append(IntProperty(caption="время выполнения", short="tm_main", default=2))

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=["prizhok_k_rukam"]))
        
        self.pool("name").append("upr_prizhok_k_rukam1")
        self.pool("name").append("upr_prizhok_k_rukam2")
