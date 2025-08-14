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
        self.properties.append(IntProperty(caption="фиксация", short="tm_main", default=30))
        self.update_props(kwargs)

        self.tasks.append(BaseTask(
            caption=self.caption + " (подготовка)",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=[f"kobra0{x}" for x in range(1,4)]
        ))
        self.pool("name").append("enter_kobra_provisli")
        self.pool("name").append("name_kobra")

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[0].images))
        self.snd_float()
        self.pool("end").append(SND_ZAKONCHILI_DALSHE)
        
    def snd_float(self):
        self.pool("float").append("descr_kobra_tianemsia_ne_za_schet_ruk", float_on_start = True)
        self.pool("float").append("common_tianemsia_intensovno_vverh")
        self.pool("float").append("rasslablenie_v_kobre")
        self.pool("float").append("common_ubedilis'_chto_nam_horosho")
        self.pool("float").append("common3")
        self.pool("float").append("common5_v_vitalkivanii")
        self.pool("float").append("common7")
        self.pool("float").append("common10")
        self.pool("float").append("common_delaem_medlenno_pomogaja_duhaniem")
        self.pool("float").append("common_duhanie_rovnoe_estestvennoe")
        self.pool("float").append("common_sledim_za_geometriei_kak_zadumanno")
        self.pool("float").append("common_vihodim_iz_asan_plavno")
        self.pool("float").append("common_uluchshenie_krovosnabshenia_pozvonochnika")
        self.pool("float").append("common_isportit'_usediem")
        self.pool("float").append("common_pozvonochnik_prinial_predloshennoe_poloshenie_v_progibe", float_on_start = True)
        self.pool("float").append("common_glubokoe_proshivanie_tela")
        

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
            images=["kobra_left"]))
        self.pool("name").append("upr_razvorot_vlevo")
        self.pool("name").append("upr_potjanulis_v_levuju_storonu")
        self.pool("float").append("starajas'_uvidet'_zadnuu_nogu")

        self.tasks.append(BaseTask(
            caption=self.caption + "\n(разворот вправо)",
            property=self.tm_right,
            metronome=MetronomeWork(),
            images=["kobra_right"]))
        self.pool("name").append("upr_razvorot_vpravo")
        self.pool("name").append("razvernulis'_vpravo")
        self.pool("name").append(SND_NA_DRUGUJU_STORONU)

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_second,
            metronome=MetronomeWork(),
            images=self.tasks[0].images))
        self.pool("name").append("i_razvorachivaemsia_vpered")
        self.pool("name").append("razvernulis")
        self.pool("name").append("i_provisli")
        self.pool("end").append(SND_ZAKONCHILI_DALSHE)
