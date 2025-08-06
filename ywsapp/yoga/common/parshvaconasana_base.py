#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  parshvaconasana_base.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import AsanaLegForward
from dataclasses import dataclass
from snd_pools import SND_MENIAJEM_NOGI, SND_LEG_LEFT_FORWARD, SND_LEG_RIGHT_FORWARD


@dataclass
class BaseParshvaconasana(AsanaLegForward):
    prepare_tm_for_swap_hands: int = 8

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
