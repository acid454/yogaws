#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gorka.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import SND_RASSLABILIS, SND_EXHALE, SND_ZAKONCHILI_DALSHE

class GorkaBase(BaseAsana):
    def __init__(self, transition_type=None, **kwargs):
        BaseAsana.__init__(self, name="gorka", caption="Горка")
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=40))
        self.update_props(kwargs)
        
        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=["gorka1", "gorka2", "gorka3", "gorka4"]
        ))
        if transition_type == "up":
            self.pool("start").append("upr_podnimaemsia_vverh1")
            self.pool("start").append("upr_podnimaemsia_vverh2")
            self.pool("start").append("so_vdohom_vverh1")
            self.pool("start").append("so_vdohom_vverh2")
        elif transition_type == "down":
            self.pool("start").append("delaem_nirok")
            self.pool("start").append("otzhimaetes'")
            self.pool("start").append("cherez_niz")
        
        self.pool("name").append("gorka1")
        self.pool("name").append("gorka2")
        self.pool("name").append("gorka3")
        self.pool("name").append("gorka4")
        self.pool("name").append("gorka5")
        self.pool("name").append("gorka6")
        self.pool("name").append("gorka7")
        self.pool("name").append("gorka8")
        self.pool("name").append("name_gorka1")
        self.pool("name").append("gorka_perehodim")
        self.pool("name").append("gorka_ushli")

        self.pool("float").append("common_i_postojat'_podushat'")
        self.pool("float").append("common_delaem_vse_ne_toropias'")
        self.pool("float").append("common_derzimsia_dushim")
        self.pool("float").append("common_vashna_geometria_i_tochnost")
        self.pool("float").append("stoim_derzhim")
        self.pool("float").append("common1")
        self.pool("float").append("descr_gorka1")
        self.pool("float").append("descr_gorka2")
        self.pool("float").append("descr_gorka3")
        self.pool("float").append("descr_gorka6")
        self.pool("float").append("descr_gorka7")
        self.pool("float").append("common5_v_vitalkivanii")
        self.pool("float").append("common4")
        self.pool("float").append("common3")
        self.pool("float").append("common7")
        self.pool("float").append("common12")
        self.pool("float").append("common_esli_chto_to_ne_poluchaetsia")

        for i in SND_RASSLABILIS + SND_EXHALE + SND_ZAKONCHILI_DALSHE:
            self.pool("end").append(i) 
        

class GorkaNormal(GorkaBase):
    def __init__(self):
        GorkaBase.__init__(self)
        self.properties.insert(0, IntProperty(caption="подготовка", short="tm_prepare", default=4))
        self.tasks.append(BaseTask(
            caption=self.caption + " (подготовка)",
            property=self.tm_prepare,
            metronome=MetronomeRest()
        ))

        self.pool("start").append("descr_gorka4")
        self.pool("start").append("descr_gorka5")
        #<snd pool="{{pool}}" file="descr_gorka3"/>
        #<snd pool="{{pool}}" file="descr_gorka2"/>
        