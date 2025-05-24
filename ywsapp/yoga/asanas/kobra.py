#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kobra.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeRest, MetronomeWork
from snd_pools import SND_ZAKONCHILI_DALSHE, SND_NA_DRUGUJU_STORONU


class Kobra(BaseAsana):
    def __init__(self, **kwargs):
        super().__init__(name="kobra", caption="Кобра")
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=5))
        self.properties.append(IntProperty(caption="фиксация", short="tm_main", default=25))
        self.update_props(kwargs)

        self.tasks.append(BaseTask(
            caption=self.caption + " (подготовка)",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=["kobra01", "kobra02", "kobra03"]
        ))
        self.pool("name").append("enter_kobra_provisli")

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[0].images))
        
        self.pool("float").append("rasslablenie_v_kobre")
        self.pool("float").append("ubedilis'_chto_nam_horosho")
        self.pool("float").append("common3")
        self.pool("float").append("common5_v_vitalkivanii")
        self.pool("float").append("common7")
        self.pool("float").append("common10")
        self.pool("float").append("common_delaem_medlenno_pomogaja_duhaniem")

        for i in SND_ZAKONCHILI_DALSHE:
            self.pool("end").append(i)

class KobraWithRotations(Kobra):
    def __init__(self, **kwargs):
        super().__init__(name="kobra_with_rotations", caption="Кобра")
        self.properties.append(IntProperty(caption="поворот влево", short="tm_left", default=15))
        self.properties.append(IntProperty(caption="поворот вправо", short="tm_right", default=15))
        self.properties.append(IntProperty(caption="вторая фиксация", short="tm_second", default=15))
        self.update_props(kwargs)

        self.pool("end").clear()

        self.tasks.append(BaseTask(
            caption=self.caption + "\n(разворот влево)",
            property=self.tm_left,
            metronome=MetronomeWork(),
            images=self.tasks[0].images))
        self.pool("name").append("upr_razvorot_vlevo")
        self.pool("name").append("upr_potjanulis_v_levuju_storonu")
        self.pool("float").append("starajas'_uvidet'_zadnuu_nogu")

        self.tasks.append(BaseTask(
            caption=self.caption + "\n(разворот вправо)",
            property=self.tm_right,
            metronome=MetronomeWork(),
            images=self.tasks[0].images))
        self.pool("name").append("upr_razvorot_vpravo")
        for snd in SND_NA_DRUGUJU_STORONU:
            self.pool("name").append(snd)

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_second,
            metronome=MetronomeWork(),
            images=self.tasks[0].images))
        self.pool("name").append("i_razvorachivaemsia_vpered")
        self.pool("name").append("razvernulis")
        self.pool("name").append("i_provisli")
        for i in SND_ZAKONCHILI_DALSHE:
            self.pool("end").append(i)
