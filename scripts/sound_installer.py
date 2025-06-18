#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  sound_installer.py
#  
#  Copyright 2021 Dmitry Repnikov <acid454@x220>
#  

import os, sys, re

def main(args):
    mp3gain = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mp3gain')
    
    results = {}
    for root, subFolders, files in os.walk(args[1]):
        for f in sorted(files):
            print(f)
            g = re.match(r'\A(h1\.)*(\d+)\.(\d+) (?P<dest>.+)\.mp3\Z', f)
            if g != None:
                dest = g.group('dest') + ".mp3"
            else:
                dest = f
            
            if dest in results.keys():
                print("Duplicate file:", results[dest], root + "/" + f)
                sys.exit(1)
            else:
                results[dest] = root + "/" + f
    print(f"Processing {len(results.keys())} files...")
    for k in results.keys():
        print("\t%s -> %s"%(results[k], k))
        #if os.system(f"cp \"{results[k]}\" \"{args[2]}/{k}\"") != 0:
        #    sys.exit(1)
        if os.system(f"ffmpeg -i \"{results[k]}\" -vn -ar 44100 -ac 1 -b:a 192k \"{args[2]}/{k}\"") != 0:
            sys.exit(1)
        #print 'ln "' + results[k] + '" "./sounds_merged/' + k + '"'


    return os.system(f"{mp3gain} -r {args[2]}/*.mp3")

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
