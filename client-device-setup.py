# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 19:35:30 2022
Setup initial device configuration on servers
@author: mr_ro
"""

import requests
import json

# Opening JSON config file
f = open('config.json')
 
# returns JSON object as a dictionary
config = json.load(f)

# Closing file
f.close()

# Opening JSON data file
f = open('data.json')
 
# returns JSON object as a list
devices_list = json.load(f)

headers = {
  'Content-Type': 'application/json'
}

url_add = config["device-server-url"]
 
for i in devices_list:
        payload = json.dumps(i)
        response = requests.request("POST", url_add, headers=headers, data=payload)
        print(response.text)

# Closing file
f.close()




