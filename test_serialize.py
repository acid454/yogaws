#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  test_serialize.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  

import jsons
from dataclasses import dataclass, field
from typing import List

#
# serialize - https://stackoverflow.com/questions/3768895/how-to-make-a-class-json-serializable
# desirialize - https://stackoverflow.com/questions/6578986/how-to-convert-json-data-into-a-python-object
# https://stackoverflow.com/questions/52063759/passing-default-list-argument-to-dataclasses
#

@dataclass
class BaseClass:
    name: str = None
    caption: str = None
    tasks: list = field(default_factory=lambda: [])
    properties: list = field(default_factory=lambda:[])

@dataclass
class BaseProperty:
    type: str = None
    caption: str = "Без названия"
    default = None
    value = None

@dataclass
class IntProp(BaseProperty):
    type: str = "int"

@dataclass
class Gorka(BaseClass):
    name: str = "gorka"
    caption: str = "Горка"
    properties: list = field(default_factory=lambda: [IntProp(caption="подготовка")])
    


def main(args):
    g = Gorka()

    g.properties[0].value = 10
    s = jsons.dump(g)
    print(s)
    
    x = jsons.load(s, Gorka)
    print(x.caption)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
