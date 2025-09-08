#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  go_down_base.py
#  
#  Copyright 2025 Dmitry Repnikov <acid454@x220>
#  

from base import BaseTask, AsanaLegForward
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import SND_VERNULIS, SND_COMPLETION_OTHERS


class AsanaGoDown:
    def go_down_task(self, tm_main, tm_exit, float_sounds = None):
        self.tasks.append(BaseTask(
            caption=self.caption + "\nложимся",
            property=tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images            # We made a ref to prev task's images
        ))
        self.pool("start").append("malasana_ladoni_v_pol", mandatory = True)
        self.pool("start").append("ruki_pered_soboi1")
        self.pool("start").append("ruki_pered_soboi2")
        self.pool("start").append("ruki_pered_soboi_i_stavim")
        self.pool("start").append("ladoni_ruk_pered_soboi1")
        self.pool("start").append("ladoni_ruk_pered_soboi2")
        
        self.pool("name").append("i_potianulis'_vniz")
        self.pool("name").append("i_tianemsia_lbom_v_pol")
        self.pool("name").append("upr_vitiagivanie_vniz1")
        self.pool("name").append("upr_vitiagivanie_vniz2")
        self.pool("name").append("upr_vitiagivanie_vniz4")
        self.pool("name").append("upr_vitiagivanie_vniz6")
        if isinstance(self, AsanaLegForward):
            self.pool("start").append("ubrali_ruki_vpravo" if self.side == AsanaLegForward.SIDE_LEFT else "ruki_vlevo")

        if float_sounds is not None:
            float_sounds()

        self.tasks.append(BaseTask(
            caption=self.caption + "\nвыход",
            property=tm_exit,
            metronome=MetronomeRest(),
            images=self.tasks[0].images            # We made a ref to prev task's images
        ))
        self.pool("name").append(SND_VERNULIS + SND_COMPLETION_OTHERS)
