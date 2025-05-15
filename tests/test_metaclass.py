#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  test_metaclass.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  


class LittleMeta(type):
    def __new__(cls, clsname, superclasses, attributedict):
        print("clsname: ", clsname)
        print("superclasses: ", superclasses)
        print("attributedict: ", attributedict)
        return type.__new__(cls, clsname, superclasses, attributedict)

class S:
    pass

class A(S, metaclass=LittleMeta):
    pass

def main(args):
    a = A()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
