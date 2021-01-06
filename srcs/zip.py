#!/usr/bin/python
# -*- coding: UTF-8 -*-

import zlib, sys

if __name__ == "__main__":

    for args in sys.argv:
        print(args)
    path = sys.argv[1]

    with open(path, 'rb') as f:
        buf = f.read()
        ret = zlib.compress(buf)
        with open(path, 'wb') as f2:
            f2.write(ret)
