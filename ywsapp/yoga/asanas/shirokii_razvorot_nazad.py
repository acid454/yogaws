#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  shirokii_razvorot_nazad.py
#  
#  Copyright 2025 Dmitry Repnikov <acid454@yoga7>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import *
from short_poses import Seli


class ShirokiiRazvorotNazad(BaseAsana):
    def __init__(self, **kwargs):
        super().__init__(self, name="shirokii_razvorot_nazad", caption="Широкий разворот назад")
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=5))
        self.properties.append(IntProperty(caption="циклов", short="cycles", default=3))
        self.properties.append(IntProperty(caption="смена рук", short="tm_swap", default=5))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=14))
        self.update_props(kwargs)

        
        self.tasks.append(BaseTask(
            caption=self.caption + "\nподготовка",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=["shirokii_razvorot_nazad_left"]
        ))
        self.pool("start").append("enter_shirokii_razvorot_vlevo")

        for i in range(self.cycles.value):
            self.tasks.append(BaseTask(
                caption=self.caption + "\nвлево",
                property=self.tm_main,
                metronome=MetronomeWork(),
                images=["shirokii_razvorot_nazad_left"]
            ))
            
            if i == 0:
                self.pool("name").append("name_shirokii_razvorot_nazad")
                self.pool("continue").append(SND_SIDE_LEFT, mandatory = True)
            self.float_sounds()
            
            self.swap_hands()
            #self.pool("end").append(SND_SIDE_RIGHT)

            self.tasks.append(BaseTask(
                caption=self.caption + "\nвправо",
                property=self.tm_main,
                metronome=MetronomeWork(),
                images=["shirokii_razvorot_nazad_right"]
            ))
            self.float_sounds()
            
            self.swap_hands()
            self.pool("name").append("vernuli_pravuju_ruku")
            #self.pool("end").append(SND_SIDE_LEFT)
        self.pool("continue").clear()
        self.pool("end").clear()
        self.pool("end").append(SND_COMPLETION_OTHERS + SND_ZAKONCHILI_DALSHE)

    def float_sounds(self):
        self.pool("float").append(None)
        self.pool("float").append(FIKSIRUEM, float_on_start = True)
        self.pool("float").append("ruka_priamaja", float_on_start = True)
        self.pool("float").append("shirokii_razvorot_descr_tianem_daleko")
        self.pool("float").append("common_delaem_vse_ne_toropias'")
        self.pool("float").append("common_derzimsia_dushim")
        self.pool("float").append("common_duhanie_rovnoe_estestvennoe")
        self.pool("float").append("common_dushim_derzim_t'anemsia")
        self.pool("float").append("common_mjagkoe_bezobidnoe_uprashnenie_raskrepostit'_pojasnicu")
        self.pool("float").append("common_potianut'_pojasnichnue_mishzi_zameret'")
        self.pool("float").append("common_sbrasivaete_napriajenie_s_litca_s_shivota")
        self.pool("float").append("common_sledim_za_geometriei_kak_zadumanno")
        self.pool("float").append("common_tianemsia_2x")
        self.pool("float").append("common_ubedilis'_chto_nam_horosho")
        self.pool("float").append("common_vashna_geometria_i_tochnost")
        self.pool("float").append("common1")
        self.pool("float").append("common3")
        self.pool("float").append("common4")
        self.pool("float").append("common7")

    def swap_hands(self):
        self.tasks.append(BaseTask(
            caption=self.caption + "\nсмена рук",
            property=self.tm_swap,
            metronome=MetronomeRest(),
            images=Seli.IMAGES
        ))
        
        self.pool("name").append(SND_VERNULIS)
        self.pool("name").append("vernuli_ruku")
        self.pool("name").append("i_razvorachivaemsia_vpered")
        self.pool("name").append("razvernulis")
        self.pool("continue").append(SND_NA_DRUGUJU_STORONU, mandatory = True)
