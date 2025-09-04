#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_pickle.py
#  
#  Copyright 2025 Repnikov Dmitry <acid454@yoga7>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import pickle, sys

class MyClass:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class TestClass:
    pass

def main(args):
    obj = MyClass("example", 123)
    serialized_obj = pickle.dumps(obj)
    deserialized_obj = pickle.loads(serialized_obj)
    print(serialized_obj)
    print(deserialized_obj)
    
    print(getattr(sys.modules[__name__], 'MyClass', None))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
