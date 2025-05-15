#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  nakrasana.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import *
from integer_constants import VOICE_SIDE_ONLY_ACTING


class Nakrasana(BaseAsana):
    def __init__(self, **kwargs):
        super().__init__(name="nakrasana", caption="Ардха Париврита Накрасана")
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=13))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=90))
        self.properties.append(IntProperty(caption="переход", short="tm_swap", default=15))
        self.properties.append(IntProperty(caption="выход", short="tm_exit", default=6))
        self.update_props(kwargs)

        self.tasks.append(BaseTask(
            caption=self.caption + "\nлевый бок, подготовка",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=[f"nakrasana_left{x}" for x in range(1,4)]
        ))
        self.pool("name").append("upr_skrutka_leza1")
        self.pool("name").append("upr_skrutka_leza2")
        self.pool("name").append("upr_skrutki_leza")
        self.pool("name").append("upr_skrutki_leza")

        self.pool("continue").append("left_side1", only_actings = VOICE_SIDE_ONLY_ACTING)
        self.pool("continue").append("left_side2", only_actings = VOICE_SIDE_ONLY_ACTING)
        self.pool("continue").append("v_levo", only_actings = VOICE_SIDE_ONLY_ACTING)

        self.pool("continue").append("enter_nakrasana_left1", overlapse = True)
        self.pool("continue").append("enter_nakrasana_left2", overlapse = True)
        self.pool("continue").append("enter_nakrasana_left3", overlapse = True)
        self.pool("continue").append("enter_nakrasana_left4", overlapse = True)
        self.pool("continue").append("enter_nakrasana_left5", overlapse = True)


        self.tasks.append(BaseTask(
            caption=self.caption + "\nлевый бок",
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images
        ))
        self.nakrasana_float_sounds()
        self.pool("float").append("descr_nakrasana_left1")
        self.pool("end").append("otlichno")
        self.pool("end").append("vernulis'1")
        self.pool("end").append("vernulis'2")
        self.pool("end").append("vernulis'_v_ishodnuju")

        self.tasks.append(BaseTask(
            caption=self.caption + "\nправый бок, подготовка",
            property=self.tm_swap,
            metronome=MetronomeRest(),
            images=[f"nakrasana_right{x}" for x in range(1,5)]
        ))
        self.pool("start").append("i_meniaem", mandatory = True)
        for snd in SND_MENIAJEM_NOGI + SND_NA_DRUGUJU_STORONU:
            self.pool("start").append(snd, mandatory = True)
        self.pool("continue").append("enter_nakrasana_right1")
        self.pool("continue").append("enter_nakrasana_right2")
        self.pool("continue").append("enter_nakrasana_right_short")

        self.tasks.append(BaseTask(
            caption=self.caption + "\nправый бок",
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images
        ))
        self.nakrasana_float_sounds()


        # ToDo:
        #{# if glob.get('last_before_shavasana') #}
        #{# set bell='4' #}
        #{# else #}
        #{# set bell=workout_default_bell #}
        #{# endif #}
        self.tasks.append(BaseTask(
            caption=self.caption + "\nвыход",
            property=self.tm_exit,
            metronome=MetronomeRest(),
            images=self.tasks[-1].images
        ))
        self.pool("start").append("otpuskaem_levuju_nogu")
        self.pool("start").append("vernulis'_v_ishodnuju")
        self.pool("start").append("otlichno")
        self.pool("start").append("vernulis'1")
        self.pool("start").append("vernulis'2")
        self.pool("start").append("davaite_zavershat'")
        for i in SND_RASSLABILIS + SND_ZAKONCHILI_DALSHE:
            self.pool("end").append(i)

    def nakrasana_float_sounds(self):
        self.pool("float").append("descr_nakrasana1")
        self.pool("float").append("descr_nakrasana2")
        self.pool("float").append("descr_nakrasana3")
        self.pool("float").append("descr_nakrasana4")
        self.pool("float").append("common7")
        self.pool("float").append("common8")
        self.pool("float").append("common9")
        self.pool("float").append("common10")
        self.pool("float").append("common11")
        self.pool("float").append("common12")
        self.pool("float").append("common_podrasslabitsia")
        self.pool("float").append("common_potianut'_pojasnichnue_mishzi_zameret'")
        self.pool("float").append("common_ne_pererastjagivaem_mushci")
        self.pool("float").append("common_rasslabit'_lico_plechi")
        self.pool("float").append("common_akcentiruite_vidohi")
        self.pool("float").append("common_delaite_to_chto_poluchaetsia")