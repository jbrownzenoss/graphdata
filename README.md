inflate, deflate, JSON graph data URL

use with Zenoss JSON API

ex.
zenoss_api device_router DeviceRouter getGraphDefs '{"uid":"/zport/dmd/Devices/Server/SSH/Linux/devices/10.90.36.164","drange":129600}' | python | graphdata.py
