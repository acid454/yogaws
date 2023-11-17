#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  parshvaconasana_base.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import AsanaLegForward
from dataclasses import dataclass
from surya_namaskar import SuryaNamaskar
from snd_pools import *


@dataclass
class BaseParshvaconasana(AsanaLegForward):
    prepare_tm_for_swap_hands: int = 8

    def build(self, workout, _set):
        # are we in suria? if yes - delete preparation
        if type(_set) is SuryaNamaskar:
            del self.tasks[0]
        
        prev_asana = workout.prev_item(self)
        if type(prev_asana) is AsanaLegForward:
            if prev_asana.side == self.side:
                # this and prev asana is same legs (same side), but different hands
                self.build_snd_swap_hands()
                self.tm_prepare.default = self.prepare_tm_for_swap_hands
            else:
                # different leg forward
                for snd in SND_MENIAJEM_NOGI:
                    self.tasks[0].pool("start").append(snd)
        else:
            # prev asana was not leg-forwarded
            if self.side == 'left':
                self.tasks[0].pool("start").append("leg_left_forward1")
                self.tasks[0].pool("start").append("leg_left_forward2")
                self.tasks[0].pool("start").append("leg_left_forward3")
                self.tasks[0].pool("start").append("leg_left_forward4")
                self.tasks[0].pool("start").append("leg_left_forward5")
                self.tasks[0].pool("start").append("leg_left_forward6")
            else:
                for snd in SND_LEG_RIGHT_FORWARD:
                    self.tasks[0].pool("start").append(snd)
        
        if type(prev_asana) is not type(self):
            self.build_snd_name()

    def build_snd_swap_hands(self):
        self.tasks[0].pool("start").append("ladoni_ruk_menijautsia_mestami")
        self.tasks[0].pool("start").append("obratnaja_ei")  #?? not everytime