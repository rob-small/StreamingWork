# -*- coding: utf-8 -*-
"""
@author: mr_ro
"""

import json
import boto3

# Opening JSON config file
f = open('config.json')
 
# returns JSON object as a dictionary
config = json.load(f)

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

# Get an S3.Client object
s3 = getConnection()

objects = s3.list_objects(Bucket = bucket_name)
count = 1
for i in objects['Contents']:
    s3.delete_object(Bucket = bucket_name, Key = i['Key'])
    print("Deleted {}".format(i['Key']))

