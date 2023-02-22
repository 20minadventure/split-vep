# helloworld.py
import os
import sys

import utils.init


def hello():
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = 0
    """Simple program that greets NAME for a total of COUNT times."""
    print(os.path.isfile('utils/file'))
    print(os.path.isfile('file'))
    for x in range(n):
        print('Hello dnax!')

