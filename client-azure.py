# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 19:35:30 2022
Azuze event hub client
@author: mr_ro
"""

from threading import Event
import requests
import json
from datetime import datetime

from azure.eventhub import EventData, EventHubProducerClient

headers = {
  'Content-Type': 'application/json'
}

# Opening JSON config file
f = open('config.json')
 
# returns JSON object as a dictionary
config = json.load(f)

url_add = config["device-server-url"]
url_read = url_add + "/reading"
azure_namespace = config["azure-hub-namespace"]
azure_hub = config["azure-hub-name"]
 
# Closing file
f.close()

# Opening JSON data file
f = open('data.json')
 
# returns JSON object as a list
devices_list = json.load(f)
 
# Closing file
f.close()

# the event hub name.
producer = EventHubProducerClient.from_connection_string(conn_str=azure_namespace, eventhub_name=azure_hub)

def pub_message(msg):

    # Create a batch.
    event_data_batch = producer.create_batch()
    
    # Add events to the batch.
    event_data_batch.add(EventData(json.dumps(msg)))
    # Send the batch of events to the event hub.
    producer.send_batch(event_data_batch)
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
