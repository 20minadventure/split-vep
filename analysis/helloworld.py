# helloworld.py
import os
import sys

import utils.init
import pkg_resources
file_path = pkg_resources.resource_filename('', 'utils/file')


def hello():
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = 0
    """Simple program that greets NAME for a total of COUNT times."""
    print(os.path.isfile('utils/file'))
    print(os.path.isfile('file'))
    print(os.path.isfile(file_path))
    for x in range(n):
        print('Hello dnax!')

