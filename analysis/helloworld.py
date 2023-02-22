# helloworld.py
import sys

import utils.init


def hello():
    if len(sys.argv) > 1:
        n = int(sys.agrv[1])
    else:
        n = 0
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(n):
        print('Hello dnax!')

if __name__ == '__main__':
    hello()
