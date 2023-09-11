#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  metronomes.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import MetronomeSounds
from dataclasses import dataclass


TICK_REST = 1
TICK_WORK = 2
BELL_BEGIN_NORM = 3
BELL_COMPLETE_NORM = 4

@dataclass
class MetronomeRest(MetronomeSounds):
    tick: int = TICK_REST
    bell: int = BELL_BEGIN_NORM


@dataclass
class MetronomeWork(MetronomeSounds):
    tick: int = TICK_WORK
    bell: int = BELL_COMPLETE_NORM