#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dshanu_shirshasana.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import *
from integer_constants import VOICE_SIDE_ONLY_ACTING


class DshanuShirshasana(BaseAsana):
    def __init__(self, **kwargs):
        super().__init__(name="dshanu_shirshasana", caption="Джану Ширшасана")
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=10))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=85))
        self.properties.append(IntProperty(caption="смена ног", short="tm_swap", default=15))
        self.properties.append(IntProperty(caption="выход", short="tm_exit", default=4))
        self.update_props(kwargs)

        self.tasks.append(BaseTask(
            caption=self.caption + "\nпправая нога, подготовка",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=["dshanu_shirshasana_right1", "dshanu_shirshasana_right2", "dshanu_shirshasana_right3", "dshanu_shirshasana_right4"]
        ))
        for snd in SND_LEG_RIGHT_FORWARD:
            self.pool("start").append(snd)
        
        self.pool("name").append("name_dshanu_shirshasana1")
        self.pool("name").append("name_dshanu_shirshasana2")
        self.pool("name").append("name_dshanu_shirshasana3")
        self.pool("name").append("name_dshanu_shirshasana_next")

        for snd in SND_LEG_RIGHT_FORWARD:
            self.pool("continue").append(snd, only_actings = VOICE_SIDE_ONLY_ACTING)

        self.pool("end").append("enter_dshanu_shirshasana_right1")
        self.pool("end").append("enter_dshanu_shirshasana_right2")
        

        self.tasks.append(BaseTask(
            caption=self.caption + "\nправая нога",
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images
        ))
        self.dshanu_shirshasana_float_sounds()
        self.pool("end").append("so_vdohom_vverh1")
        self.pool("end").append("so_vdohom_vverh2")
        self.pool("end").append("podnimaemsia1")
        self.pool("end").append("podnimaemsia2")
        self.pool("end").append("otlichno")


        self.tasks.append(BaseTask(
            caption=self.caption + "\nлевая нога, подготовка",
            property=self.tm_swap,
            metronome=MetronomeRest(),
            images=["dshanu_shirshasana_left1", "dshanu_shirshasana_left2", "dshanu_shirshasana_left3", "dshanu_shirshasana_left4"]
        ))
        self.pool("start").append("i_meniaem", mandatory = True)
        for snd in SND_MENIAJEM_NOGI + SND_NA_DRUGUJU_STORONU:
            self.pool("start").append(snd, mandatory = True)
        self.pool("continue").append("enter_dshanu_shirshasana_left1")
        self.pool("continue").append("enter_dshanu_shirshasana_left2")


        self.tasks.append(BaseTask(
            caption=self.caption + "\nлевая нога",
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images
        ))
        self.dshanu_shirshasana_float_sounds()
        self.pool("end").append("otpuskaem_levuju_nogu")
        self.pool("end").append("podnimaemsia1")
        self.pool("end").append("podnimaemsia2")
        for snd in SND_ZAKONCHILI_DALSHE:
            self.pool("end").append(snd)

    def dshanu_shirshasana_float_sounds(self):
        self.pool("continue").append("descr_dshanu_shirshasana1")
        self.pool("continue").append("descr_dshanu_shirshasana2")
        self.pool("continue").append("descr_dshanu_shirshasana3")
        self.pool("continue").append("descr_dshanu_shirshasana4")
        self.pool("float").append("descr_dshanu_shirshasana_navisanie_nad_nogoi")
        self.pool("float").append("descr_dshanu_shirshasana_ja_mogu_sloshitsia")
        self.pool("float").append("descr_dshanu_shirshasana_sledim_za_perekosom_v_plechah")
        self.pool("float").append("common_podrasslabitsia")
        self.pool("float").append("common_telo_prosedajet")
        self.pool("float").append("common3")
        self.pool("float").append("common8")
        self.pool("float").append("common9")
        self.pool("float").append("common10")
        self.pool("float").append("common11")
        self.pool("float").append("common12")
        self.pool("float").append("common_delaite_to_chto_poluchaetsia")
        self.pool("float").append("common_duhanie_estestvennoe_long")
        self.pool("float").append("common_ne_pererastjagivaem_mushci")
        self.pool("float").append("common_rasslabit'_lico_plechi")
        self.pool("float").append("common_akcentiruite_vidohi")
        self.pool("float").append("common_esli_chto_to_ne_poluchaetsia")
