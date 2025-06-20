#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  test_multiprocessing.py
#  
#  Copyright 2025 Repnikov Dmitry <acid454@yoga7>
#  
#  

import time
import multiprocessing


def long_run_process(connector, arg):
    for i in range(9):
        print(f">> long run process {arg}")
        time.sleep(0.3)
    print("<< long run complete")
    
    connector.send(10)
    connector.send(b"return string")

def main(args):
    conn1, conn2 = multiprocessing.Pipe(duplex=False)
    
    proc = multiprocessing.Process(target=long_run_process, args=(conn2, 'bob',))
    proc.start()
    
    print("Mainline running...")
    for i in range(6):
        print(f"  proc alive: {proc.is_alive()}")
        print(f"  conn1 poll: {conn1.poll()}")
        time.sleep(1)
    print(f"Mainline complete, join")
    proc.join()
    
    print(conn1.recv())
    print(conn1.recv())
    conn1.close()
    conn2.close()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
