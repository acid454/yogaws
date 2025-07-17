#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  marichiasana.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import *
from integer_constants import VOICE_SIDE_ONLY_ACTING


class Marichiasana(BaseAsana):
    def __init__(self, **kwargs):
        super().__init__(name="marichiasana", caption="Маричиасана")
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=16))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=60))
        self.properties.append(IntProperty(caption="выход", short="tm_exit", default=4))
        self.update_props(kwargs)

        self.tasks.append(BaseTask(
            caption=self.caption + "\nправый бок, подготовка",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=["marichiasana_right1", "ardhamatsyendrasana_right1", "ardhamatsyendrasana_right2", "marichiasana_right2"]
        ))
        self.pool("name").append("name_marichiasana1")
        self.pool("name").append("name_marichiasana2")
        self.pool("name").append("name_marichiasana3")
        self.pool("name").append("name_ardhamatsyendrasana")
        self.pool("name").append("name_ardhamatsyendrasana_i_delaem")
        self.pool("continue").append("enter_marichiasana_right1")
        self.pool("continue").append("enter_marichiasana_right2")
        self.pool("continue").append("enter_marichiasana_right3")
        self.pool("continue").append("enter_ardhamatsyendrasana_right1")
        self.pool("continue").append("enter_ardhamatsyendrasana_right2")
        self.pool("continue").append(SND_SIDE_RIGHT, only_actings = VOICE_SIDE_ONLY_ACTING)


        self.tasks.append(BaseTask(
            caption=self.caption + "\nправый бок",
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images
        ))
        self.marichiasana_float_sounds()
        self.marichiasana_exit_sounds("end")


        self.tasks.append(BaseTask(
            caption=self.caption + "\nлевый бок, подготовка",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=["marichiasana_left1", "marichiasana_left2", "ardhamatsyendrasana_left1", "ardhamatsyendrasana_left2"]
        ))
        self.pool("start").append(SND_MENIAJEM_NOGI + SND_NA_DRUGUJU_STORONU, mandatory = True)
        self.pool("continue").append("enter_marichiasana_left")


        self.tasks.append(BaseTask(
            caption=self.caption + "\nлевый бок",
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images
        ))
        self.pool("start").append("i_delaete_skrutku")
        self.pool("start").append("descr_ardhamatsyendrasana_left")
        self.marichiasana_float_sounds()


        self.tasks.append(BaseTask(
            caption=self.caption + "\nвыход",
            property=self.tm_exit,
            metronome=MetronomeRest(),
            images=self.tasks[-1].images
        ))
        self.marichiasana_exit_sounds("start")
        self.pool("end").append(SND_COMPLETION_OTHERS + SND_ZAKONCHILI_DALSHE)

    def marichiasana_exit_sounds(self, pool):
        self.pool(pool).append("raspletaemsia")
        self.pool(pool).append("i_raspletaemsia1")
        self.pool(pool).append("i_raspletaemsia2")
        self.pool(pool).append("i_raspletaemsia3")
        self.pool(pool).append("i_raspletaemsia4")
        self.pool(pool).append("i_akkuratno_raspletaemsia")
        self.pool(pool).append("razvernulis")
        self.pool(pool).append("i_razvorachivaemsia_vpered")

    def marichiasana_float_sounds(self):
        self.pool("float").append("descr_marichiasana1")
        self.pool("float").append("descr_marichiasana2")
        self.pool("float").append("descr_marichiasana3")
        self.pool("float").append("descr_ardhamatsyendrasana")
        self.pool("float").append("common_podrasslabitsia")
        self.pool("float").append("common_duhanie_estestvennoe_long")
        self.pool("float").append("common_samokontrol'_primenit'_k_sebe")
        self.pool("float").append("common_delaite_to_chto_poluchaetsia")
        self.pool("float").append("common_delaem_medlenno_pomogaja_duhaniem")
        self.pool("float").append("common_duhanie_rovnoe_estestvennoe")
        self.pool("float").append("common_sledim_za_geometriei_kak_zadumanno")
        self.pool("float").append("common_povtoriaushiesia_pozu")
        self.pool("float").append("marichiasana_common_sledim_za_pozvonochnikom")
        self.pool("float").append("common_vsie_budet_horosho")
        self.pool("float").append("common_sbrasivaete_napriajenie_s_litca_s_shivota")
