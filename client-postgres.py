# -*- coding: utf-8 -*-
"""
CREATE DATABASE device;
CREATE TABLE reading (
   device_name text,
   ts timestamp,
   value real
);
-
@author: mr_ro
"""

from threading import Event
import requests
import json
from datetime import datetime
import os
import psycopg2 

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

# Get database connection settings
db_host = os.environ.get('devicedb_host')
db_name = os.environ.get('devicedb_name')
db_user = os.environ.get('devicedb_user')
db_pwd = os.environ.get('devicedb_pwd')
db_port = os.environ.get('devicedb_port')

conn = psycopg2.connect(dbname=db_name, user=db_user, host=db_host, password=db_pwd, port=db_port)

cur = conn.cursor()

def pub_message(msg):
    insert_query = "INSERT INTO reading (device_name, ts, value) VALUES ('{0}','{1}',{2})".format(msg['name'],msg['ts'],msg['reading'])
    cur.execute(insert_query)
    conn.commit()
    print(insert_query, flush=True)


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

cur.close()
conn.close()