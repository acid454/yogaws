#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  uttanasana.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork
from snd_pools import SND_S_VIDOHOM_VNIZ, SND_ZAKONCHILI_DALSHE, SND_COMPLETION_OTHERS


class UttanasanaBase(BaseAsana):
    def __init__(self, name, caption):
        BaseAsana.__init__(self, name=name, caption=caption)
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=40))
        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=[f"uttanasana{x}" for x in range(1,5)]
        ))
        self.pool("start").append(SND_S_VIDOHOM_VNIZ)
        self.pool("start").append("upr_vitiagivanie_vniz1")
        self.pool("start").append("upr_vitiagivanie_vniz2")
        self.pool("start").append("upr_vitiagivanie_vniz3")
        self.pool("start").append("upr_vitiagivanie_vniz4")
        self.pool("name").append("name_uttanasana1")
        self.pool("name").append("name_uttanasana2")
        self.pool("name").append("name_uttanasana3")
        self.pool("name").append("name_uttanasana4")
        self.pool("continue").append("descr_vitjashenie_vniz2")
        self.pool("continue").append("descr_vitjashenie_vniz6")
        self.pool("continue").append("descr_uttanasana3")
        self.pool("continue").append("na_skol'ko_eto_poluchaetsia")
        self.pool("continue").append("i_tianemsia_lbom_v_pol")
        self.pool("float").append("descr_uttanasana1")
        self.pool("float").append("descr_uttanasana2")
        self.pool("float").append("descr_vitjashenie_vniz3")
        self.pool("float").append("descr_vitjashenie_vniz4")
        self.pool("float").append("descr_vitjashenie_vniz5")
        self.construct_end_pool()

    def construct_common_pool(self):
        self.pool("float").append("common_dlya_spinu_i_pozvonochnika")
        self.pool("float").append("common_telo_prosedajet")
        self.pool("float").append("common_potianut'_pojasnichnue_mishzi_zameret'")
        self.pool("float").append("common_tianemsia_2x")
        self.pool("float").append("common_i_postojat'_podushat'")
        self.pool("float").append("common7")
        self.pool("float").append("common_delaem_medlenno_pomogaja_duhaniem")
        self.pool("float").append("common_duhanie_rovnoe_estestvennoe")
        self.pool("float").append("common_povtoriaushiesia_pozu")

    def construct_end_pool(self):
        self.pool("end").append(SND_ZAKONCHILI_DALSHE + SND_COMPLETION_OTHERS)


class Uttanasana(UttanasanaBase):
    def __init__(self, **kwargs):
        UttanasanaBase.__init__(self, name="uttanasana", caption="Уттанасана")
        self.update_props(kwargs)
        self.tasks[-1].pool("start").append("upr_vitiagivanie_vniz5")
        self.tasks[-1].pool("start").append("upr_vitiagivanie_vniz7")
        self.tasks[-1].pool("continue").append("descr_vitjashenie_vniz1")

class UttanasanaWithCompensation(UttanasanaBase):
    def __init__(self, **kwargs):
        UttanasanaBase.__init__(self, name="uttanasana", caption="Уттанасана")
        self.properties.append(IntProperty(caption="время компенсации", short="tm_compensation", default=10))
        self.update_props(kwargs)

        self.pool("end").clear()
        self.tasks.append(BaseTask(
            caption=self.caption + "\nкомпенсация",
            property=self.tm_compensation,
            metronome=MetronomeWork(),
            images=["vigibaemsia_vpered1", "vigibaemsia_vpered2"]
        ))
        self.pool("start").append("upr_podnimaem_golovu_vugibaemsia", mandatory = True)
        self.pool("start").append("upr_podnimaem_golovu_ottolknulis'_ot_nog", mandatory = True)
        self.construct_common_pool()
        self.construct_end_pool()

class Uttanasana_ruki_v_zamke(UttanasanaBase):
    def __init__(self, **kwargs):
        UttanasanaBase.__init__(self, name="uttanasana_ruki_v_zamke", caption="Уттанасана (руки в замке)")
        self.properties.append(IntProperty(caption="замок", short="tm_zamok", default=25))
        self.update_props(kwargs)

        self.pool("end").clear()
        self.tasks.append(BaseTask(
            caption=self.caption + "\nруки в замке",
            property=self.tm_zamok,
            metronome=MetronomeWork(),
            images=["uttanasana_zamok1", "uttanasana_zamok2", "uttanasana4_zamok"]
        ))
        self.pool("start").append("upr_ruki_v_zamke_za_spinoi1", mandatory = True)
        self.pool("start").append("upr_ruki_v_zamke_za_spinoi2", mandatory = True)
        self.pool("continue").append("descr_ruki_v_zamke_za_spinoi1")
        self.pool("continue").append(None)
        self.construct_common_pool()
        self.construct_end_pool()
        self.tasks[-1].pool("end").append("rascepliaem_ruki")
        
        # descr_vitjashenie_vniz7_v_zamke
