# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 19:35:30 2022
x -Read device list from JSON file
Set URL and PORT number from command line
Set file name from command line
@author: mr_ro
"""

from threading import Event
import requests
import json
from datetime import datetime

url_add = "http://192.168.56.101:5000/devices"
headers = {
  'Content-Type': 'application/json'
}

# Opening JSON file
f = open('data.json')
 
# returns JSON object as a list
devices_list = json.load(f)
 
for i in devices_list:
        payload = json.dumps(i)
        response = requests.request("POST", url_add, headers=headers, data=payload)
        print(response.text)

# Closing file
f.close()

url_read = "http://192.168.56.101:5000/devices/reading"

while 1:
    for i in devices_list:
        payload = json.dumps({
          "name": i["name"]
        })

        response = requests.request("GET", url_read, headers=headers, data=payload)
        
        gauge_out = {}
        gauge_out['timestamp'] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S:%f")
        gauge_out['reading'] = response.text
        gauge_out['name'] =  i["name"]
        print(json.dumps(gauge_out), flush=True)

    Event().wait(1)



