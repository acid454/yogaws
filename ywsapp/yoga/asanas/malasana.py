#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dhanurasana.py
#  
#  Copyright 2025 Repnikov Dmitry <acid454@yoga7>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import SND_EXHALE, SND_COMPLETION_OTHERS, SND_ZAKONCHILI_DALSHE


class Malasana(BaseAsana):
    def __init__(self, with_complication = True, **kwargs):
        super().__init__(name="malasana", caption="Маласана")
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=10))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=50))
        if with_complication:
            self.properties.append(IntProperty(caption="вытяжение вниз", short="tm_floor", default=30))
        self.properties.append(IntProperty(caption="выход", short="tm_exit", default=5))
        self.update_props(kwargs)
        
        self.tasks.append(BaseTask(
            caption=self.caption + " (подготовка)",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=["malasana1"]
        ))
        self.pool("name").append("name_malasana_i_variant")
        self.pool("continue").append("enter_malasana")
        self.pool("end").append("i_tjanemsia_vverh")
        self.pool("end").append("vitalkivaemsia_vverh")
        self.pool("end").append("upr_vitajshenie_vverh1")
        self.pool("end").append("upr_vitajshenie_vverh2")
        self.pool("end").append("upr_vitajshenie_vverh3_na_vdohe")

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images
        ))
        self.pool("continue").append("descr_malasana")
        self.float_sounds()
        self.pool("end").append(SND_EXHALE)

        if with_complication:
            self.tasks.append(BaseTask(
                caption=self.caption + " \n(ладони в пол)",
                property=self.tm_prepare,
                metronome=MetronomeRest(),
                images=["malasana_v_pol"]
            ))
            self.pool("name").append("malasana_ladoni_v_pol")
            self.pool("continue").append("malasana_beriem_sebia_za_piatki")
            self.pool("end").append("i_tianemsia_lbom_v_pol")

            self.tasks.append(BaseTask(
                caption=self.caption,
                property=self.tm_floor,
                metronome=MetronomeWork(),
                images=self.tasks[-1].images
            ))
            self.float_sounds()
            self.pool("end").append(SND_EXHALE)

        self.tasks.append(BaseTask(
            caption=self.caption + " (выход)",
            property=self.tm_exit,
            metronome=MetronomeRest(),
            images=["malasana_exit"]
        ))
        self.pool("end").append(SND_COMPLETION_OTHERS + SND_ZAKONCHILI_DALSHE)

    def float_sounds(self):
        self.pool("float").append("common_dlya_spinu_i_pozvonochnika")
        self.pool("float").append("common_prirost_navikov")
        self.pool("float").append("common_samokontrol'_primenit'_k_sebe")
        self.pool("float").append("common12")
        self.pool("float").append("common3")
        self.pool("float").append("common_duhanie_rovnoe_estestvennoe")
        self.pool("float").append("common_sledim_za_geometriei_kak_zadumanno")
        self.pool("float").append("common_vsie_budet_horosho")
        self.pool("float").append("common_vihodim_iz_asan_plavno")
        self.pool("float").append("common_isportit'_usediem")
