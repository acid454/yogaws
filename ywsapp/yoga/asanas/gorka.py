#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gorka.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from base import AsanaLegForward
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest, MetronomeRestComplete
from snd_pools import SND_RASSLABILIS, SND_EXHALE, SND_ZAKONCHILI_DALSHE


class GorkaBase(BaseAsana):
    def __init__(self, transition_type=None, metronome_rest=False, **kwargs):
        BaseAsana.__init__(self, name="gorka", caption="Горка")
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=40))
        self.update_props(kwargs)

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork() if not metronome_rest else MetronomeRestComplete(),
            images=[f"gorka{x}" for x in range(1,5)]
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
        else:
            self.pool("name").append("name_sobaka_mordoi_vniz")
        
        self.gorka_name_snd()

        self.pool("float").append("common_delaem_vse_ne_toropias'")
        self.pool("float").append("common1")
        self.pool("float").append("descr_padattonasana", float_on_start = True)
        self.pool("float").append("descr_potjanulis_vpered1", float_on_start = True)
        self.pool("float").append("descr_gorka2", float_on_start = True)
        if metronome_rest:
            return

        self.pool("float").append("common_i_postojat'_podushat'")
        self.pool("float").append("common_derzimsia_dushim")
        self.pool("float").append("common_vashna_geometria_i_tochnost")
        self.pool("float").append("stoim_derzhim")
        self.pool("float").append("descr_gorka1")
        self.pool("float").append("descr_gorka3")
        self.pool("float").append("descr_gorka4", float_on_start = True)
        self.pool("float").append("descr_gorka5", float_on_start = True)
        self.pool("float").append("descr_gorka6")
        self.pool("float").append("descr_gorka7")
        self.pool("float").append("common5_v_vitalkivanii")
        self.pool("float").append("common4")
        self.pool("float").append("common3")
        self.pool("float").append("common7")
        self.pool("float").append("common12")
        self.pool("float").append("common_esli_chto_to_ne_poluchaetsia")
        self.pool("float").append("common_duhanie_rovnoe_estestvennoe")
        self.pool("float").append("common_sledim_za_geometriei_kak_zadumanno")
        self.pool("float").append("common_povtoriaushiesia_pozu")
        self.pool("float").append("marichiasana_common_sledim_za_pozvonochnikom")
    
    def gorka_name_snd(self):
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
        

class GorkaNormal(GorkaBase):
    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.properties.insert(0, IntProperty(caption="подготовка", short="tm_prepare", default=4))
        self.update_props(kwargs)

        name_pool = self.tasks[0].pool("name")
        self.tasks.insert(0, BaseTask(
            caption=self.caption + " (подготовка)",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=self.tasks[0].images
        ))

        self.tasks[0].pool("name").migrate(name_pool)
        for i in SND_RASSLABILIS + SND_EXHALE + SND_ZAKONCHILI_DALSHE:
            self.pool("end").append(i)
    
    def build(self, workout, _set):
        super().build(workout, _set)
        
        next_asana = workout.next_item(self)
        if issubclass(type(next_asana), AsanaLegForward):
            self.pool("end").clear()
