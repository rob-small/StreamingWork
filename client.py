# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 19:35:30 2022

@author: mr_ro
"""

from threading import Event
import requests
import json
from datetime import datetime

from mydevice import myDevice
        
url_add = "http://192.168.56.101:5000/devices"
headers = {
  'Content-Type': 'application/json'
}

devices_list = [
        myDevice(20,5,'dev1'),
        myDevice(25,1,'dev2'),
        myDevice(35,3,'dev3'),
        myDevice(10,2,'dev4')
    ]

for i in devices_list:
        payload = json.dumps({
          "name": i.name,
          "mean": i.mean,
          "stdev": i.stdev
        })
        
        response = requests.request("POST", url_add, headers=headers, data=payload)

        print(response.text)

url_read = "http://192.168.56.101:5000/devices/reading"

while 1:
    for i in devices_list:
        payload = json.dumps({
          "name": i.name
        })

        response = requests.request("GET", url_read, headers=headers, data=payload)
        
        gauge_out = {}
        gauge_out['timestamp'] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S:%f")
        gauge_out['reading'] = response.text
        gauge_out['name'] =  i.name
        print(json.dumps(gauge_out), flush=True)

    Event().wait(1)



