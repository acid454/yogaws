#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  gen_previews.py
#  
#  Copyright 2025 Repnikov Dmitry <acid454@yoga7>
#  
#  

import os
from PIL import Image
from os import listdir
from os.path import isfile, join


def main(args):
    size = 256, 256
    cur_path = os.path.abspath(os.path.dirname(__file__))
    res_path = os.path.join(cur_path, 'ywsapp/static/ywsapp/res/imgs')
    res_files = [f for f in listdir(res_path) if (isfile(join(res_path, f)) and f.endswith('.png'))]

    for res_file in res_files:
        try:
            im = Image.open(join(res_path, res_file))
            im.thumbnail(size, Image.Resampling.LANCZOS)
            im.save(join(res_path, 'thumbnails', res_file), "JPEG")
        except IOError:
            print("cannot create thumbnail for '%s'" % res_file)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
