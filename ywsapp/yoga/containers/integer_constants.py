#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  voice_acctings.py
#  
#  Copyright 2025 Dmitry Repnikov <acid454@yoga7>
#  

from django.db import models


class VoiceActing(models.IntegerChoices):
    FULL = 0, 'Full'
    NO_COMMON_COMMENTS = 1, 'No common comments'
    NO_ANY_COMMENTS = 2, 'No any comments'
    ASANA_START_STOP = 3, 'Asana start and stop only'
    ASANA_NAME_ONLY = 4, 'Asana name only'

VOICE_SIDE_ONLY_ACTING = [VoiceActing.ASANA_START_STOP, VoiceActing.ASANA_NAME_ONLY]


class ShavasanaActing(models.IntegerChoices):
    SETTINGS_DEPEND = 0, 'Depends on settings'
    ALWAYS_ACTING = 1, 'Acting always'
    NEVER_ACTING = 2, 'Never acting'

class MetronomeTicks(models.IntegerChoices):
    FULL = 0, 'Full'
    ONLY_BELLS = 1, 'Bells only'
    NONE = 2, 'No metronome sound'
