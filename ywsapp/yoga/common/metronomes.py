#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  metronomes.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import MetronomeSounds
from dataclasses import dataclass


@dataclass
class MetronomeRest(MetronomeSounds):
    tick: str = "tick_rest"
    bell: str = "task_begin_norm"

@dataclass
class MetronomeRestComplete(MetronomeSounds):
    tick: str = "tick_rest"
    bell: str = "task_complete_norm"

@dataclass
class MetronomeWork(MetronomeSounds):
    tick: str = "tick_work"
    bell: str = "task_complete_norm"

@dataclass
class MetronomeShavasana(MetronomeSounds):
    tick: str = None
    bell: str = "workout_complete"
