#!/usr/bin/env python3.6

import subprocess
import os
from argparse import ArgumentParser

parser = ArgumentParser(description='kill the running listening on a given port')
parser.add_argument('port', type=int, help='the port number to search for')

port = parser.parse_arg().port

try:
    result = subprocess.run(
            ['lsof', '-n', "-i4TCP:%s" % port],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
except subprocess.CalledProcessError:
    print(f"No process listening on port {port}")
    exit(1)
else:
    listening = None

    for line in result.stdout.splitlines():
        if "LISTEN" in str(line):
            listening = line
            break

    if listening:
        # PID is the second column in the output
        pid = int(listen.split()[1])
        os.kill(pid, 9)
        print(f"Killed process {pid}")
    else:
        print(f"No process listening on port {port}")
        exit(1)
