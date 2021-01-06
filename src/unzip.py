#!/usr/bin/python
# -*- coding: UTF-8 -*-

import zlib, sys, os

def xunzip(path):
	print(path)
	with open(path, 'rb') as f:
	        buf = f.read()
	        ret = zlib.decompress(buf)
	        with open(path, 'wb') as f2:
	            f2.write(ret)

if __name__ == "__main__":
    path = sys.argv[1]

    for root, dirs, files in os.walk(path, topdown=False):
	    for name in files:
	        xunzip(str(os.path.join(root, name)))

	    
