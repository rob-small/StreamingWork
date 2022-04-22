# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 19:35:30 2022
Baseline client 
To do
- Set input file name from command line
@author: mr_ro
"""

from threading import Event
import requests
import json
from datetime import datetime

headers = {
  'Content-Type': 'application/json'
}

# Opening JSON config file
f = open('config.json')
 
# returns JSON object as a dictionary
config = json.load(f)

url_add = config["device-server-url"]
url_read = url_add + "/reading"
 
# Closing file
f.close()

# Opening JSON data file
f = open('data.json')
 
# returns JSON object as a list
devices_list = json.load(f)
 
for i in devices_list:
        payload = json.dumps(i)
        response = requests.request("POST", url_add, headers=headers, data=payload)
        print(response.text)

# Closing file
f.close()


def pub_message(msg):
    print(msg, flush=True)

while 1:
    for i in devices_list:
        payload = json.dumps({
          "name": i["name"]
        })

        response = requests.request("GET", url_read, headers=headers, data=payload)
        
        gauge_out = {}
        gauge_out['ts'] = str(datetime.now())
        gauge_out['reading'] = response.text.strip("\n")
        gauge_out['name'] =  i["name"]
        pub_message(gauge_out)
        
    Event().wait(1)


