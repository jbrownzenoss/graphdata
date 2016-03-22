#!/usr/bin/python

import sys
import zlib
import base64

s =  open(sys.argv[1], 'r')
data = s.read()
z = zlib.decompress(base64.b64decode(data))
print z
