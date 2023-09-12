#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  surya_namaskar.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseSet
from properties import IntProperty
from gorka import GorkaBase
from uttanasana import Uttanasana
from sobaka_mordoi_vverh import SobakaMordoiVverh


class SuryaNamaskar(BaseSet):
    def __init__(self):
        super().__init__(caption="Сурья Намаскар", asanas=[
            Uttanasana(),
            GorkaBase(),
            SobakaMordoiVverh()
        ])
        self.properties.append(IntProperty(caption="количество циклов", short="cnt", default=9))