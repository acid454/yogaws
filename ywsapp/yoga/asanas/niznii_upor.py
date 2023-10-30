#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  niznii_upor.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

from base import BaseAsana, BaseTask, SoundPool
from properties import IntProperty
from metronomes import MetronomeWork, MetronomeRest


class NizniiUpor(BaseAsana):
    def __init__(self, **kwargs):
        BaseAsana.__init__(self, name="niznii_upor", caption="Нижний упор")
        self.properties.append(IntProperty(caption="время фиксации", short="tm_main", default=15))
        self.update_props(kwargs)

        self.tasks.append(BaseTask(
            caption=self.caption,
            property=self.tm_main,
            metronome=MetronomeWork(),
            images=["niznii_upor"]))
        
        self.pool("start").append("ruki_pered_soboi1")
        self.pool("start").append("ruki_pered_soboi2")
        self.pool("start").append("ladoni_ruk_pered_soboi1")
        self.pool("start").append("ladoni_ruk_pered_soboi2")
        self.pool("start").append("ladoni_ruk_pered_soboi_sgibaem_nogi")

        self.pool("continue").append("upr_niznii_upor1")
        self.pool("continue").append("upr_niznii_upor2")
        self.pool("continue").append("upr_niznii_upor3")
        self.pool("continue").append("upr_niznii_upor4")
        self.pool("continue").append("upr_niznii_upor5")
