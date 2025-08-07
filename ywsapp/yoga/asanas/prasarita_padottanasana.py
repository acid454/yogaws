#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  prasarita_padottanasana.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import *


class PrasaritaPadottanasana(BaseAsana):
    def __init__(self, with_legs = True, with_hands = False, **kwargs):
        super().__init__(name="prasarita_padottanasana", caption="Прасарита Падоттанасана")
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=11))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=80))
        if with_legs:
            self.properties.append(IntProperty(caption="наклон к ногам", short="tm_legs", default=30))
        if with_hands:
            self.properties.append(IntProperty(caption="подготовка рук", short="tm_hands_prep", default=5))
            self.properties.append(IntProperty(caption="подъём рук", short="tm_hands_main", default=30))
        self.properties.append(IntProperty(caption="выход", short="tm_exit", default=6))
        self.update_props(kwargs)


        self.tasks.append(BaseTask(
            caption=self.caption + "\n(подготовка)",
            property=self.tm_prepare,
            metronome=MetronomeRest(),
            images=["prasarita_padottanasana"]
        ))
        self.pool("name").append("name_prasarita_padottanasana1")
        self.pool("name").append("name_prasarita_padottanasana2")
        self.pool("continue").append("razveli_nashi_nogi")
        self.pool("continue").append("razvodim_nogi_v_storoni1")
        self.pool("continue").append("razvodim_nogi_v_storoni2")
        self.pool("end").append("upr_vitiagivanie_vniz5")
        self.pool("end").append("upr_vitiagivanie_vniz7")

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images
        ))
        self.pool("float").append("descr_prasarita_padottanasana1")
        self.pool("float").append("common_dlya_spinu_i_pozvonochnika")
        self.pool("float").append("common_i_postojat'_podushat'")
        self.pool("float").append("common_dushim_derzim_t'anemsia")
        self.pool("float").append("common_vashna_geometria_i_tochnost")
        self.pool("float").append("common_rasslabit'_lico_plechi")
        self.pool("float").append("common1")
        self.pool("float").append("common3")
        self.pool("float").append("common4")
        self.pool("float").append("common7")
        self.pool("float").append("common10")
        self.pool("float").append("common_duhanie_rovnoe_estestvennoe")
        self.pool("float").append("common_sledim_za_geometriei_kak_zadumanno")
        self.pool("float").append("common_sbrasivaete_napriajenie_s_litca_s_shivota")
        self.pool("float").append("common_isportit'_usediem")

        if with_legs:
            self.tasks.append(BaseTask(
                caption=self.caption + "\n(наклон к левой ноге)",
                property=self.tm_legs,
                metronome=MetronomeWork(),
                images=["prasarita_padottanasana_leg_left"]
            ))
            self.pool("name").append("upr_potjanulis_k_levoi_noge1")
            self.pool("name").append("upr_potjanulis_k_levoi_noge2")
            self.pool("name").append("upr_potjanulis_v_levuju_storonu")
            self.pool("continue").append("descr_prasarita_potjanulis_k_levoi_noge")
            self.pool("continue").append("descr_prasarita_potjanulis_k_noge_common")
            self.pool("float").append("common7")

            self.tasks.append(BaseTask(
                caption=self.caption + "\n(наклон к правой ноге)",
                property=self.tm_legs,
                metronome=MetronomeWork(),
                images=["prasarita_padottanasana_leg_right"]
            ))
            self.pool("name").append("k_pravoi_noge")
            self.pool("name").append(SND_NA_DRUGUJU_STORONU)
            self.pool("float").append("descr_prasarita_potjanulis_k_noge_common")
            self.pool("float").append("common_tianemsia_2x")
            self.pool("float").append("common_i_postojat'_podushat'")
            self.pool("float").append("common7")
            self.pool("float").append("common_sledim_za_geometriei_kak_zadumanno")
            self.pool("float").append("common_sbrasivaete_napriajenie_s_litca_s_shivota")

        if with_hands:
            self.append_hands_tasks()

        self.tasks.append(BaseTask(
            caption=self.caption + "\n(выход)",
            property=self.tm_exit,
            metronome=MetronomeWork(),
            images=["prasarita_padottanasana"]
        ))

        if with_legs or with_hands:
            self.pool("name").append(SND_VERNULIS + SND_COMPLETION_OTHERS)

        self.pool("continue").append("so_vdohom_vverh1")
        self.pool("continue").append("upr_podnimaemsia_vverh1")
        self.pool("continue").append("upr_podnimaemsia_vverh2")
    
    def append_hands_tasks(self):
        self.tasks.append(BaseTask(
            caption=self.caption + "\n(правая рука, подготовка)",
            property=self.tm_hands_prep,
            metronome=MetronomeRest(),
            images=["prasarita_padottanasana_ruki_pered_soboi2"]
        ))
        self.pool("start").append("ladoni_ruk_pered_soboi1")
        self.pool("start").append("ladoni_ruk_pered_soboi2")
        self.pool("start").append("ruki_pered_soboi1")
        self.pool("start").append("ruki_pered_soboi2")
        self.pool("end").append("enter_prasarita_padottanasana_right")

        self.tasks.append(BaseTask(
            caption=self.caption + "\n(разорот вправо)",
            property=self.tm_hands_main,
            metronome=MetronomeWork(),
            images=["prasarita_padottanasana_right"]
        ))
        self.pool("start").append("i_delaem_shirokie_razvoroti")
        self.pool("continue").append(SND_SIDE_RIGHT)
        self.pool("float").append("common_dlya_spinu_i_pozvonochnika")
        self.pool("float").append("common_i_postojat'_podushat'")
        self.pool("float").append("common_dushim_derzim_t'anemsia")
        self.pool("float").append("common_vashna_geometria_i_tochnost")
        self.pool("float").append("common1")
        self.pool("float").append("common3")
        self.pool("float").append("common4")
        self.pool("float").append("common7")
        self.pool("float").append("common10")
        self.pool("float").append("common_duhanie_rovnoe_estestvennoe")
        self.pool("float").append("common_sledim_za_geometriei_kak_zadumanno")
        self.pool("float").append("common_akcentiruite_vidohi")
        self.pool("end").append("i_provernuli")
        self.pool("end").append(SND_VERNULIS + SND_COMPLETION_OTHERS + SND_S_VIDOHOM_VNIZ)
        
        self.tasks.append(BaseTask(
            caption=self.caption + "\n(левая рука, подготовка)",
            property=self.tm_hands_prep,
            metronome=MetronomeRest(),
            images=["prasarita_padottanasana_left"]
        ))
        self.pool("start").append("i_meniaem")
        self.pool("start").append(SND_NA_DRUGUJU_STORONU)

        self.tasks.append(BaseTask(
            caption=self.caption + "\n(разорот влево)",
            property=self.tm_hands_main,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images
        ))
        self.pool("float").append("common_dlya_spinu_i_pozvonochnika")
        self.pool("float").append("common_i_postojat'_podushat'")
        self.pool("float").append("common_dushim_derzim_t'anemsia")
        self.pool("float").append("common_vashna_geometria_i_tochnost")
        self.pool("float").append("common1")
        self.pool("float").append("common3")
        self.pool("float").append("common4")
        self.pool("float").append("common7")
        self.pool("float").append("common10")
        self.pool("float").append("common_duhanie_rovnoe_estestvennoe")
        self.pool("float").append("common_sledim_za_geometriei_kak_zadumanno")
        self.pool("end").append("opustili_ruku")
    