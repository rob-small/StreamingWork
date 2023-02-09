# -*- coding: utf-8 -*-
"""
To do
- Set input file name from command line
@author: mr_ro
"""

from threading import Event
import requests
import json
from datetime import datetime
import os

# Get service URL. If no environment variable set then look in config file
url_add = os.environ.get('DeviceServerUrl')

if url_add is None:
    # Opening JSON config file
    f = open('config.json')
 
    # returns JSON object as a dictionary
    config = json.load(f)

    url_add = config["device-server-url"]

    # Closing file
    f.close()

headers = {
  'Content-Type': 'application/json'
}

url_read = url_add + "/reading"
 
# Opening JSON data file
f = open('data.json')
 
# returns JSON object as a list
devices_list = json.load(f)
 
# Closing file
f.close()

from azure.cosmos import CosmosClient, PartitionKey

settings = {
    'host': os.environ.get('COSMOS_HOST'),
    'master_key': os.environ.get('COSMOS_KEY'),
    'database_id': os.environ.get('COSMOS_DATABASE', 'Device'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'Reading'),
}

client = CosmosClient(url=settings["host"], credential=settings["master_key"])
database = client.create_database_if_not_exists(id=settings["database_id"])
key_path = PartitionKey(path="/name")
container = database.create_container_if_not_exists(id=settings["container_id"], partition_key=key_path)

def pub_message(msg):
    container.create_item(msg)
    print("Posted to Cosmos -", str(datetime.now()))

while 1:
    for i in devices_list:
        payload = json.dumps({
          "name": i["name"]
        })

        response = requests.request("GET", url_read, headers=headers, data=payload)
        
        gauge_out = {}
        gauge_out['id'] = str(datetime.now())
        gauge_out['ts'] = str(datetime.now())
        gauge_out['reading'] = response.text.strip("\n")
        gauge_out['name'] =  i["name"]
        pub_message(gauge_out)
        
    Event().wait(1)


