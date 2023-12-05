#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  virabhadrasana3.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseTask
from parshvaconasana_base import BaseParshvaconasana
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest
from snd_pools import *


class Virabhadrasana3Base(BaseParshvaconasana):
    def __init__(self, _side, _caption):
        super().__init__(name="virabhadrasana3_%s"%(_side), caption=_caption, side = _side, prepare_tm_for_swap_hands = 7)
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=7))
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=40))

        self.tasks.append(BaseTask(
            caption=self.caption + "\nподготовка",
            property=self.tm_prepare,
            metronome=MetronomeRest()
        ))

        #ToDo: description is long and can overlapse - but, with next task!
        #  now we can overlapse only inside same task.
        self.pool("continue").append("descr_virabhadrasana_tri1_overlapse")
        self.pool("continue").append("descr_virabhadrasana_tri2_overlapse")

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork()
        ))

        self.pool("float").append("common3")
        self.pool("float").append("common_derzimsia_dushim")
        self.pool("float").append("common_vashna_geometria_i_tochnost")
        self.pool("float").append("common1")
        self.pool("float").append("common4")

        for i in SND_RASSLABILIS + SND_EXHALE + SND_S_VIDOHOM_VNIZ:
            self.pool("end").append(i) 
    
    def build_snd_name(self, prev_asana):
        if issubclass(type(prev_asana), Virabhadrasana3Base):
            return
        self.tasks[0].pool("name").append("name_virabhadrasana_tri")
    
    def build_snd_swap_hands(self):
        pass

class Virabhadrasana3Left(Virabhadrasana3Base):
    def __init__(self, **kwargs):
        super().__init__('left', "Вирабхадрасана 3\n(левая нога)")
        self.update_props(kwargs)
        self.update_all_tasks_images(["virabhadrasana3_left"])

class Virabhadrasana3Right(Virabhadrasana3Base):
    def __init__(self, **kwargs):
        super().__init__('right', "Вирабхадрасана 3\n(правая нога)")
        self.update_props(kwargs)
        self.update_all_tasks_images(["virabhadrasana3_right"])
