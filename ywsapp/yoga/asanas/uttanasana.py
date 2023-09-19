#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  uttanasana.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask, SoundPool
from properties import IntProperty
from metronomes import MetronomeWork
from snd_pools import SND_ZAKONCHILI_DALSHE


class UttanasanaBase(BaseAsana):
    def __init__(self, name, caption):
        BaseAsana.__init__(self, name=name, caption=caption)
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=40))
        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            snd_pools = [
                SoundPool(name="start", files=[
                    "i_uhodim_vniz",
                    "s_vidohom_uhodim_vniz1",
                    "s_vidohom_uhodim_vniz2",
                    "s_vidohom_uhodim_vniz3",
                    "i_s_vidohom_opustilis'_vniz1",
                    "i_s_vidohom_opustilis'_vniz2",
                    "i_s_vidohom_opustilis'_vniz3",
                    "upr_vitiagivanie_vniz1",
                    "upr_vitiagivanie_vniz2",
                    "upr_vitiagivanie_vniz3",
                    "upr_vitiagivanie_vniz4" ]),
                SoundPool(name="name", files = [
                     "name_uttanasana1",
                     "name_uttanasana2",
                     "name_uttanasana3",
                     "name_uttanasana4"]),
                SoundPool(name="continue", files = [
                     "descr_vitjashenie_vniz2",
                     "descr_vitjashenie_vniz6",
                     "na_skol'ko_eto_poluchaetsia"]),
                SoundPool(name="float", files = [
                    "descr_uttanasana1",
                    "descr_uttanasana2",
                    "descr_vitjashenie_vniz3",
                    "descr_vitjashenie_vniz4",
                    "descr_vitjashenie_vniz5",
                    "common_dlya_spinu_i_pozvonochnika",
                    "common_telo_prosedajet",
                    "common_potianut'_pojasnichnue_mishzi_zameret'",
                    "common_tianemsia_2x",
                    "common_i_postojat'_podushat'",
                    "common7"]),
                SoundPool(name="end", files = [
                    "_horosho1", "_horosho2"] + SND_ZAKONCHILI_DALSHE)
                ]))

class Uttanasana(UttanasanaBase):
    def __init__(self):
        UttanasanaBase.__init__(self, name="uttanasana", caption="Уттанасана")
        self.tasks[-1].images = ["uttanasana1", "uttanasana2", "uttanasana3"]
        self.tasks[-1].pool("start").append("upr_vitiagivanie_vniz5")
        self.tasks[-1].pool("start").append("upr_vitiagivanie_vniz7")
        self.tasks[-1].pool("continue").append("descr_vitjashenie_vniz1")


class Uttanasana_ruki_v_zamke(UttanasanaBase):
    def __init__(self):
        UttanasanaBase.__init__(self, name="uttanasana_ruki_v_zamke", caption="Уттанасана (руки в замке)")
        self.tasks[-1].images = ["uttanasana_zamok1", "uttanasana_zamok2 ", "uttanasana4_zamok"]
        self.tasks[-1].pool("continue").clear()
        self.tasks[-1].pool("continue").append("upr_ruki_v_zamke_za_spinoi1")
        self.tasks[-1].pool("continue").append("upr_ruki_v_zamke_za_spinoi2")
        self.tasks[-1].pool("continue_").append("descr_ruki_v_zamke_za_spinoi1")
        self.tasks[-1].pool("continue_").append(None)
        self.tasks[-1].pool("end").append("rascepliaem_ruki")
        
        # descr_vitjashenie_vniz7_v_zamke
