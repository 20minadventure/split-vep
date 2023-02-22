# helloworld.py
import sys

import utils.init


def hello():
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = 0
    """Simple program that greets NAME for a total of COUNT times."""
    with open('file') as f:
        print(f.readlines())
    for x in range(n):
        print('Hello dnax!')

