#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  plug.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask, AsanaLegsStayUp
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import SND_ZAKONCHILI_DALSHE


class Plug(BaseAsana):
    def __init__(self, **kwargs):
        super().__init__(name="plug", caption="Халасана")
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=11))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=80))
        self.properties.append(IntProperty(caption="выход", short="tm_exit", default=6))
        self.update_props(kwargs)
        
        self.tasks.append(BaseTask(
            caption=self.caption + " (подготовка)",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=[f"plug{x}" for x in range(1,8)]
        ))
        self.pool("name").append("name_plug1")
        self.pool("name").append("name_plug2")
        self.pool("name").append("name_plug3")
        self.pool("name").append("name_plug4")
        self.pool("name").append("name_plug5")
        self.pool("name").append("name_plug_i_u_nas")
        self.pool("name").append("name_plug_i_uhodim")
        self.pool("continue").append("enter_plug1")
        self.pool("continue").append("enter_plug2")
        self.pool("continue").append("enter_plug3")
        self.pool("continue").append("enter_plug4")
        self.pool("continue").append("enter_plug5")

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images
        ))
        self.pool("start").append("descr_plug3")
        self.pool("start").append("descr_plug4")
        self.pool("start").append("common_delaem_vse_ne_toropias'")
        self.pool("float").append("descr_plug1")
        self.pool("float").append("descr_plug2")
        self.pool("float").append("descr_plug6")
        self.pool("float").append("common3")
        self.pool("float").append("common4")
        self.pool("float").append("common8")
        self.pool("float").append("common9")
        self.pool("float").append("common10")
        self.pool("float").append("common11")
        self.pool("float").append("common12")
        self.pool("float").append("common_ne_pererastjagivaem_mushci")
        self.pool("float").append("common_akcentiruite_vidohi")
        self.pool("float").append("common_delaite_to_chto_poluchaetsia")
        self.pool("float").append("common_delaem_medlenno_pomogaja_duhaniem")
        self.pool("float").append("common_duhanie_rovnoe_estestvennoe")
        self.pool("float").append("common_sledim_za_geometriei_kak_zadumanno")
        self.pool("float").append("marichiasana_common_sledim_za_pozvonochnikom")
        self.pool("float").append("common_vsie_budet_horosho")
        self.pool("float").append("common_vihodim_iz_asan_plavno")
        self.pool("float").append("common_uluchshenie_krovosnabshenia_pozvonochnika")
        
    def build(self, workout, _set):
        next_asana = workout.next_item(self)
        if type(next_asana) is AsanaLegsStayUp:
            self.tasks.append(BaseTask(
                caption=self.caption + " (выход, ноги подняты)",
                property=self.tm_exit,
                metronome=MetronomeRest(),
                images=["nogi_vverh_ruki_v_storoni"]
            ))
            self.pool("continue").append("vernuli_nogi_vverh")
            self.pool("continue").append("podniali_nogi")
            self.pool("continue").append("upr_podnimaemsia_vverh1")
            self.pool("continue").append("upr_podnimaemsia_vverh2")
        else:
            self.tasks.append(BaseTask(
                caption=self.caption + " (выход)",
                property=self.tm_exit,
                metronome=MetronomeRest(),
                images=self.tasks[-1].images
            ))
            self.pool("start").append("i_akkuratno_raskatali_spinu_obratno")
            self.pool("start").append("plug_i_poluperekatom_vozvrashaemsia_sidia")
        self.pool("start").append("raskatilis'")
        self.pool("start").append("poluperekatom_vozvrashaemsia")
        super().build(workout, _set)
