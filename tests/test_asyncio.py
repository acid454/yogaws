#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  test_asyncio.py
#  
#  Copyright 2025 Repnikov Dmitry <acid454@yoga7>
#  



import asyncio

async def long_run_process():
    proc = await asyncio.create_subprocess_exec(
        'ping','8.8.8.8', '-c', '3',
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
    
    stdout, stderr = await proc.communicate()
    print(proc.returncode)
    print(stdout.decode())

async def long_sleep():
    print(">> long sleep")
    await asyncio.sleep(3)
    print("<< long sleep")

def main(args):
    loop = asyncio.get_event_loop()
    rc = loop.create_task(long_sleep())
    rc = loop.run_until_complete(long_sleep())
    loop.close()
    #
    #asyncio.run(long_sleep)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
