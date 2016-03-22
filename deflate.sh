#!/usr/bin/python

import sys
import zlib
import base64

s =  open(sys.argv[1], 'r')
data = s.read()
z = base64.b64encode(zlib.compress(data))
print z
