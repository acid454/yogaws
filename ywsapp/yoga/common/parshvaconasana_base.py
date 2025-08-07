#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  parshvaconasana_base.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import AsanaLegForward
from dataclasses import dataclass
from snd_pools import SND_MENIAJEM_NOGI, SND_LEG_LEFT_FORWARD, SND_LEG_RIGHT_FORWARD, SND_S_VIDOHOM_VNIZ, FIKSIRUEM, STOIM


@dataclass
class BaseParshvaconasana(AsanaLegForward):
    prepare_tm_for_swap_hands: int = 8

    def preparation_sounds_with_hand(self):
        self.pool("end").append("potianem_ruku_vpered_a_vot_teper'")
        self.pool("end").append("krug_rukoi_i_potianuli_ee_vpered")
        self.pool("end").append("krug_rukoi_provorot")
        self.pool("end").append("ruku_vpered_a_sami_v_potolok")

    def utthita_parivritta_main_sounds(self):
        self.pool("start").append("makushka_golovi_tianet_vpered")
        self.pool("start").append("upr_potjanulis_vpered1")
        self.pool("start").append("upr_potjanulis_vpered2")
        self.pool("start").append("upr_potjanulis_vpered3")
        self.pool("start").append("upr_potjanulis_vpered5")
        self.pool("start").append("upr_potjanulis_vpered7")
        self.pool("start").append("vitjanulis'1")
        self.pool("start").append("vitjanulis'2")
        self.pool("continue").append(FIKSIRUEM + STOIM)
        self.pool("continue").append("descr_virabhadrasana_obrashaem_vnimanie_na_stupniu_i_koleno")
        self.pool("continue").append("descr_virabhadrasana_telo_odna_linija")
        self.pool("float").append("descr_parivritta_parshvakonasana2", float_on_start = True)
        self.pool("float").append("descr_parivritta_parshvakonasana3", float_on_start = True)
        self.pool("float").append("descr_parivritta_parshvakonasana5", float_on_start = True)
        self.pool("float").append("descr_utthita_vzgliad_v_potolok")
        self.pool("float").append("descr_utthita_stupnia_ruka")
        self.pool("float").append("common1")
        self.pool("float").append("common3")
        self.pool("float").append("common4")
        self.pool("float").append("common6")
        self.pool("float").append("common7")
        self.pool("float").append("common10")
        self.pool("float").append("common12")
        self.pool("float").append("common_derzimsia_dushim")
        self.pool("float").append("common_i_postojat'_podushat'")
        self.pool("float").append("common_duhanie_rovnoe_estestvennoe")
        self.pool("float").append("common_sledim_za_geometriei_kak_zadumanno")
        self.pool("float").append("common_sbrasivaete_napriajenie_s_litca_s_shivota")
        self.pool("end").append("i_s_vidohom_opuskaem_ruku_vniz")
        self.pool("end").append("i_s_vidohom_opustili_ruku")
        self.pool("end").append("provernuli_ruku_opustili_vniz")
        self.pool("end").append("exit_provernuv_ruku_opuskaem_ee_vniz")
        self.pool("end").append(SND_S_VIDOHOM_VNIZ)

    def build(self, workout, _set):
        super().build(workout, _set)

        if len(self.tasks[0].pool("start").items) != 0:
            print("WARNING! Base Parshvaconasana task start pool not empty, but need to be!")
        
        prev_asana = workout.prev_item(self)
        if issubclass(type(prev_asana), AsanaLegForward):
            if prev_asana.side == self.side:
                # this and prev asana is same legs (same side), but different hands
                self.build_snd_swap_hands()
                self.tm_prepare.default = self.prepare_tm_for_swap_hands
            else:
                # different leg forward
                self.tasks[0].pool("start").append(SND_MENIAJEM_NOGI, mandatory = True)
        else:
            # prev asana was not leg-forwarded
            if self.side == 'left':
                self.tasks[0].pool("start").append(SND_LEG_LEFT_FORWARD, mandatory = True)
            else:
                self.tasks[0].pool("start").append(SND_LEG_RIGHT_FORWARD, mandatory = True)
        self.build_snd_name(prev_asana)

    def build_snd_swap_hands(self):
        self.tasks[0].pool("start").append("i_meniaem", mandatory = True)
        self.tasks[0].pool("start").append("ladoni_ruk_menijautsia_mestami", mandatory = True)
        self.tasks[0].pool("start").append("obratnaja_ei", mandatory = True)
