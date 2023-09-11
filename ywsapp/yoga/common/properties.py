#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  properties.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from dataclasses import dataclass
from base import BaseProperty

@dataclass
class IntProperty(BaseProperty):
    type: str = "int"
    default: int  = 0
