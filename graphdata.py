#!/usr/bin/python

import sys
import zlib
import json
import base64

data = sys.stdin.read()
parsed_json = json.loads(data)
for i in range(len(parsed_json['result']['data'])):
        title = parsed_json['result']['data'][i]['contextTitle']
        graph = str(parsed_json['result']['data'][i])
        graph = str.replace(graph, "u'", '"')
        graph = str.replace(graph, "'", '"')
        graph = str.replace(graph, "True", "true")
        graph = str.replace(graph, "False", "false")
        graph = str.replace(graph, "None", "null")
        data = base64.b64encode(zlib.compress(graph))
        print title + "\n\n" + data + "\n"
