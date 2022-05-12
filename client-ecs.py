# -*- coding: utf-8 -*-
"""
@author: mr_ro
"""

from threading import Event
import requests
import json
import boto3
from datetime import datetime

# Opening JSON config file
f = open('config.json')
 
# returns JSON object as a dictionary
config = json.load(f)

url_add = config["device-server-url"]
url_read = url_add + "/reading"

host = config["ecs-host"]
access_key_id = config["ecs-id"]
secret_key = config["ecs-secret-key"]
bucket_name = config["ecs-bucket"]
 
# Closing file
f.close()

# set connection sample code
def getConnection() -> boto3.client:
    # ECS runs S3 with SSL/TLS on 9021 and plaintext on 9020.  Behind a load balancer this will usually be remapped to 80/443
    secure = False
    s3 = boto3.client('s3', aws_access_key_id=access_key_id, aws_secret_access_key=secret_key, use_ssl=secure, endpoint_url=host)
    return s3

s3 = getConnection()

# # Opening JSON data file
f = open('data.json')
 
# # returns JSON object as a list
devices_list = json.load(f)

# Closing file
f.close()

i_msg_count = 1
out_buffer = []

def pub_message(msg):
    global i_msg_count
    global out_buffer
    
    print(i_msg_count, flush=True)
    # collect every 10 messages and then flush them to a new s3 object
    if i_msg_count == 10:
        i_msg_count = 1
        response = s3.put_object(Body = json.dumps(out_buffer),
                     Bucket = bucket_name,
                     Key = "device-"+ datetime.now().strftime("%d%m%y-%H-%M-%S")
                     )
        print(response)
        out_buffer.clear()
        print("object created", flush=True)
    else:
        i_msg_count += 1
        out_buffer.append(msg)
        

headers = {  'Content-Type': 'application/json' }

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


