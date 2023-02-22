# helloworld.py
import os
import sys

import utils.init
import pkg_resources
try:
    print(pkg_resources.resource_filename('helloworld', 'utils/file'))
except:
    pass
try:
    print(pkg_resources.resource_filename('helloworld', 'file'))
except:
    pass
file_path2 = pkg_resources.resource_filename('analysis', 'file')
file_path3 = pkg_resources.resource_filename('utils', 'file')


def hello():
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = 0
    """Simple program that greets NAME for a total of COUNT times."""
    print(os.path.isfile('utils/file'))
    print(os.path.isfile('file'))
    #print(os.path.isfile(file_path1))
    print(os.path.isfile(file_path2))
    print(os.path.isfile(file_path3))
    for x in range(n):
        print('Hello dnax!')

