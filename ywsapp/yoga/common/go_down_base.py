#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  go_down_base.py
#  
#  Copyright 2025 Dmitry Repnikov <acid454@x220>
#  

from base import BaseTask
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import SND_OPUSTILIS, SND_S_VIDOHOM_VNIZ, SND_VERNULIS, SND_COMPLETION_OTHERS


class AsanaGoDown:
    def go_down_task(self, tm_main, tm_exit, float_sounds = None):
        self.tasks.append(BaseTask(
            caption=self.caption + "\nложимся",
            property=tm_main,
            metronome=MetronomeWork(),
            images=self.tasks[-1].images            # We made a ref to prev task's images
        ))
        self.pool("name").append("i_potianulis'_vniz")
        self.pool("name").append(SND_OPUSTILIS + SND_S_VIDOHOM_VNIZ)

        if float_sounds is not None:
            float_sounds()

        self.tasks.append(BaseTask(
            caption=self.caption + "\nвыход",
            property=tm_exit,
            metronome=MetronomeRest(),
            images=self.tasks[0].images            # We made a ref to prev task's images
        ))
        self.pool("name").append(SND_VERNULIS + SND_COMPLETION_OTHERS)
