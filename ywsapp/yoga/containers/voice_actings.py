#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  voice_acctings.py
#  
#  Copyright 2025 Dmitry Repnikov <acid454@yoga7>
#  

class VoiceActings:
    FULL = 0, 'Full'
    NO_COMMON_COMMENTS = 1, 'No common comments'
    NO_ANY_COMMENTS = 2, 'No any comments'
    ASANA_START_STOP = 3, 'Asana start and stop only'
    ASANA_START_ONLY = 4, 'Asana start only'

VOICE_SIDE_ONLY_ACTING = [VoiceActings.ASANA_START_STOP, VoiceActings.ASANA_START_ONLY]