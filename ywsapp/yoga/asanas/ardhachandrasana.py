#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ardhachandrasana.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeRest, MetronomeWork
from snd_pools import *

class Ardhachandrasana(BaseAsana):
    def __init__(self, **kwargs):
        super().__init__(name="ardhachandrasana", caption="Ардха Чандрасана")
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=13))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=25))
        self.properties.append(IntProperty(caption="смена ног", short="tm_swap", default=13))
        self.properties.append(IntProperty(caption="выход", short="tm_exit", default=4))
        self.update_props(kwargs)

        self.tasks.append(BaseTask(
            caption=self.caption + "\nлевая нога, подготовка",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=[f"ardhachandrasana_left{x}" for x in range(1,4)]
        ))
        self.pool("name").append("name_ardhachandrasana1")
        self.pool("name").append("name_ardhachandrasana2")
        self.pool("name").append("name_ardhachandrasana3")
        self.pool("continue").append("leg_left_opornaja")
        self.pool("float").append("enter_ardhachandrasana_left1")

        self.tasks.append(BaseTask(
            caption=self.caption + "\nлевая нога",
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images
        ))
        self.ardhachandrasana_common_sounds()

        self.tasks.append(BaseTask(
            caption=self.caption + "\nправая нога, подготовка",
            property=self.tm_swap,
            metronome=MetronomeRest(),
            images=[f"ardhachandrasana_right{x}" for x in range(1,4)]
        ))
        self.pool("start").append("i_meniaem")
        for snd in SND_MENIAJEM_NOGI + SND_NA_DRUGUJU_STORONU:
            self.pool("start").append(snd)
        self.pool("continue").append("enter_ardhachandrasana_right1")
        self.pool("continue").append("enter_ardhachandrasana_right2")
        self.pool("continue").append("enter_ardhachandrasana_right3")

        self.tasks.append(BaseTask(
            caption=self.caption + "\nправая нога",
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images
        ))
        self.ardhachandrasana_common_sounds()
        
        self.tasks.append(BaseTask(
            caption=self.caption + "\nвыход",
            property=self.tm_exit,
            metronome=MetronomeRest(),
            images=self.tasks[-1].images
        ))
        for snd in SND_ZAKONCHILI_DALSHE:
            self.pool("end").append(snd)

    def ardhachandrasana_common_sounds(self):
        self.pool("float").append("descr_ardhachandrasana_zameret'")
        self.pool("float").append("common3")
        self.pool("float").append("common4")
        self.pool("float").append("descr_ardhachandrasana_common1")
        self.pool("float").append("common_esli_chto_to_ne_poluchaetsia")
        self.pool("float").append("common10")
        self.pool("float").append("common6")
        self.pool("float").append("descr_ardhachandrasana_common2")
        self.pool("float").append("common_i_postojat'_podushat'")
        self.pool("float").append("common_derzimsia_dushim")
        self.pool("float").append("common_vashna_geometria_i_tochnost")
        self.pool("float").append("common1")
        for i in SND_RASSLABILIS + SND_EXHALE + SND_S_VIDOHOM_VNIZ:
            self.pool("end").append(i)
        self.pool("end").append("i_s_vidohom_na_ladoni_ruk")
        self.pool("end").append("i_s_vidohom_opuskaem_ruku_vniz")
        self.pool("end").append("i_s_vidohom_opustili_ruku")
        self.pool("end").append("provernuli_ruku_opustili_vniz")
        self.pool("end").append("exit_provernuv_ruku_opuskaem_ee_vniz")
