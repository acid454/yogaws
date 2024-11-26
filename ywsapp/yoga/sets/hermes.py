#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  hermes.py
#  
#  Copyright 2024 Repnikov Dmitry <acid454@yoga7>
#  

from base import BaseSet
from properties import IntProperty
from asanas import Asanas


class HermesGymnastics(BaseSet):
    def __init__(self, **kwargs):
        super().__init__(caption="Комплекс упражнений Гермеса Трисмегиста")
        self.properties.append(IntProperty(caption="количество циклов на упражнение", short="cnt", default=4))
        self.properties.append(IntProperty(caption="подготовка", short="tm_prepare", default=10))
        self.properties.append(IntProperty(caption="вход", short="tm_action", default=2))
        self.properties.append(IntProperty(caption="фиксация", short="tm_fixation", default=4))
        self.properties.append(IntProperty(caption="расслабление", short="tm_relax", default=6))
        self.properties.append(IntProperty(caption="завершение", short="tm_exit", default=10))
        self.update_props(kwargs)
    
    def build(self, workout):
        self.asanas.append(Asanas.breath.Breath(_inhale = False, action_text = "встаём ровно", tm_main = self.tm_prepare.value))
        self.asanas[-1].set_images(["hermes_stand"])
        self.asanas[-1].pool("start").append("begin_vstaem_rovno_ruki_vdol'_tulovisha")
        self.asanas[-1].pool("end").append("poehali")
        
        for i in range(self.cnt.value):
            self.asanas.append(Asanas.breath.Breath(_inhale = True, action_text = "вдох", include_sounds = True, tm_main = self.tm_action.value))
            self.asanas[-1].set_images(["hermes_inhale1"])
            self.asanas[-1].tasks[-1].metronome.bell = self.asanas[-1].tasks[-1].metronome.tick

            self.asanas.append(Asanas.breath.Breath(_inhale = True, action_text = "фиксация", tm_main = self.tm_fixation.value))
            self.asanas[-1].set_images(["hermes_inhale1"])

            self.asanas.append(Asanas.breath.Breath(_inhale = False, action_text = "расслабление", include_sounds = True, tm_main = self.tm_relax.value))
            self.asanas[-1].set_images(["hermes_relax1"])
            for i in range(1,8):
                self.asanas[-1].pool("start").append(f"i_rasslabilis{i}")
        #self.asanas[-1].pool("start").clear()
        #self.asanas[-1].pool("end").append("i_zakanchivaem")
        #self.asanas[-1].pool("end").append("zakanchivaem_s_nei_i_dal'she")
        for i in range(1,3):
            self.asanas[-1].pool("end").append(f"i_dvishemsia_dalshe{i}")


        for i in range(self.cnt.value):
            if i % 2 == 0:
                self.asanas.append(Asanas.breath.Breath(_inhale = True, include_sounds = True, action_text = "вдох-вправо", tm_main = self.tm_action.value))
                self.asanas[-1].set_images(["hermes_inhale2"])  # ToDo: arrows on images
            else:
                self.asanas.append(Asanas.breath.Breath(_inhale = True, include_sounds = True, action_text = "вдох-влево", tm_main = self.tm_action.value))
                self.asanas[-1].set_images(["hermes_inhale2"])  # ToDo: arrows on images
            self.asanas[-1].tasks[-1].metronome.bell = self.asanas[-1].tasks[-1].metronome.tick
        
            self.asanas.append(Asanas.breath.Breath(_inhale = True, action_text = "фиксация", tm_main = self.tm_fixation.value))
            self.asanas[-1].set_images(["hermes_inhale2"])

            self.asanas.append(Asanas.breath.Breath(_inhale = False, include_sounds = True, action_text = "расслабление", tm_main = self.tm_relax.value))
            self.asanas[-1].set_images(["hermes_relax1"])
            for i in range(1,8):
                self.asanas[-1].pool("start").append(f"i_rasslabilis{i}")
        

        self.asanas.append(Asanas.short_poses.PodnimaemsiaVvreh())
        self.asanas[-1].pool("end").append("upr_razvodim_ruki_v_storoni")

        
        for i in range(self.cnt.value):
            if i % 2 == 0:
                self.asanas.append(Asanas.breath.Breath(_inhale = True, include_sounds = True, action_text = "вдох-вправо", tm_main = self.tm_action.value))
                self.asanas[-1].set_images(["hermes_stand_right"])
            else:
                self.asanas.append(Asanas.breath.Breath(_inhale = True, include_sounds = True, action_text = "вдох-влево", tm_main = self.tm_action.value))
                self.asanas[-1].set_images(["hermes_stand_left"])
            self.asanas[-1].tasks[-1].metronome.bell = self.asanas[-1].tasks[-1].metronome.tick
        
            self.asanas.append(Asanas.breath.Breath(_inhale = True, action_text = "фиксация", tm_main = self.tm_fixation.value))
            self.asanas[-1].set_images( self.asanas[-2].tasks[-1].images )

            self.asanas.append(Asanas.breath.Breath(_inhale = False, include_sounds = True, action_text = "расслабление", tm_main = self.tm_relax.value))
            self.asanas[-1].set_images(["hermes_stand"])
            for i in range(1,8):
                self.asanas[-1].pool("start").append(f"i_rasslabilis{i}")
        #self.asanas[-1].pool("start").clear()
        self.asanas[-1].pool("end").append("i_zakanchivaem")
        for i in range(1,3):
            self.asanas[-1].pool("end").append(f"i_dvishemsia_dalshe{i}")
        
        self.asanas.append(Asanas.breath.Breath(_inhale = False, action_text = "встаём ровно", tm_main = self.tm_prepare.value))
        self.asanas[-1].set_images(["hermes_spreading_stand1"])
        for i in range(self.cnt.value):
            self.asanas.append(Asanas.breath.Breath(_inhale = True, action_text = "вдох", include_sounds = True, tm_main = self.tm_action.value))
            self.asanas[-1].set_images(["hermes_spreading_arch1"])
            self.asanas[-1].tasks[-1].metronome.bell = self.asanas[-1].tasks[-1].metronome.tick

            self.asanas.append(Asanas.breath.Breath(_inhale = True, action_text = "фиксация", tm_main = self.tm_fixation.value))
            self.asanas[-1].set_images(["hermes_spreading_arch1"])

            self.asanas.append(Asanas.breath.Breath(_inhale = False, action_text = "расслабление", include_sounds = True, tm_main = self.tm_relax.value))
            self.asanas[-1].set_images(["hermes_spreading_stand"])
        #self.asanas[-1].pool("start").clear()
        self.asanas[-1].pool("end").append("i_zakanchivaem")
        for i in range(1,3):
            self.asanas[-1].pool("end").append(f"i_dvishemsia_dalshe{i}")

        self.asanas.append(Asanas.breath.Breath(_inhale = False, action_text = "наклон вниз", tm_main = self.tm_prepare.value))
        self.asanas[-1].set_images(["hermes_spreading_low"])
        for i in range(self.cnt.value):
            self.asanas.append(Asanas.breath.Breath(_inhale = True, action_text = "вдох", include_sounds = True, tm_main = self.tm_action.value))
            self.asanas[-1].set_images(["hermes_spreading_arch2"])
            self.asanas[-1].tasks[-1].metronome.bell = self.asanas[-1].tasks[-1].metronome.tick

            self.asanas.append(Asanas.breath.Breath(_inhale = True, action_text = "фиксация", tm_main = self.tm_fixation.value))
            self.asanas[-1].set_images(["hermes_spreading_arch2"])

            self.asanas.append(Asanas.breath.Breath(_inhale = False, action_text = "расслабление", include_sounds = True, tm_main = self.tm_relax.value))
            self.asanas[-1].set_images(["hermes_spreading_low"])
        #self.asanas[-1].pool("start").clear()
        self.asanas[-1].pool("end").append("i_zakanchivaem")
        for i in range(1,3):
            self.asanas[-1].pool("end").append(f"i_dvishemsia_dalshe{i}")

        self.asanas.append(Asanas.breath.Breath(_inhale = False, action_text = "встаём ровно", tm_main = self.tm_prepare.value))
        self.asanas[-1].set_images(["hermes_spreading_stand1"])
        for i in range(self.cnt.value):
            if i % 2 == 0:
                self.asanas.append(Asanas.breath.Breath(_inhale = True, action_text = "вдох-вправо", include_sounds = True, tm_main = self.tm_action.value))
                self.asanas[-1].set_images(["hermes_spreading_right"])
            else:
                self.asanas.append(Asanas.breath.Breath(_inhale = True, action_text = "вдох-влево", include_sounds = True, tm_main = self.tm_action.value))
                self.asanas[-1].set_images(["hermes_spreading_left"])
            self.asanas[-1].tasks[-1].metronome.bell = self.asanas[-1].tasks[-1].metronome.tick

            self.asanas.append(Asanas.breath.Breath(_inhale = True, action_text = "фиксация", tm_main = self.tm_fixation.value))
            self.asanas[-1].set_images( self.asanas[-2].tasks[-1].images )

            self.asanas.append(Asanas.breath.Breath(_inhale = False, action_text = "расслабление", include_sounds = True, tm_main = self.tm_relax.value))
            self.asanas[-1].set_images(["hermes_spreading_stand2"])
        #self.asanas[-1].pool("start").clear()
        self.asanas[-1].pool("end").append("i_zakanchivaem")
        for i in range(1,3):
            self.asanas[-1].pool("end").append(f"i_dvishemsia_dalshe{i}")

        self.asanas.append(Asanas.breath.Breath(_inhale = False, action_text = "завершение упражнения", tm_main = self.tm_exit.value))
        self.asanas[-1].set_images(["hermes_spreading_stand1"])

        super().build(workout)
