#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  test_singleton.py
#  
#  Copyright 2023 Dmitry Repnikov <acid454@x220>
#  



class BaseClassOfSingleton:
    def __init__(self):
        self.base = 1

class SingletonClass(BaseClassOfSingleton):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance


def main(args):
    singleton = SingletonClass()
    new_singleton = SingletonClass()
    
    print(singleton is new_singleton)
    
    singleton.singl_variable = "Singleton Variable"
    print(new_singleton.singl_variable)

    print(singleton.base)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
