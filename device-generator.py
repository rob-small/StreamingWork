# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 15:41:10 2022

@author: mr_ro

x - Setup as an object
x - Have mean and standard deviation changeable
x - Have it run every second and pump out a reading to stdout
x - Add name attribute
x - Add name to output
x - Add timestamp to output
x - Flush output regularly
x - Put a delimiter in the output
x - convert output to json
x - initialize a list of devices
"""

from numpy.random import default_rng
from threading import Event
from datetime import datetime
import json

from mydevice import myDevice
        
devices_list = [
        myDevice(20,5,'dev1'),
        myDevice(25,1,'dev2'),
        myDevice(35,3,'dev3'),
        myDevice(10,2,'dev4')
    ]


while 1:
    for i in devices_list:
        gauge_out = {}
        gauge_out['timestamp'] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S:%f")
        gauge_out['reading'] = i.take_reading()
        gauge_out['name'] =  i.name
        print(json.dumps(gauge_out), flush=True)
    Event().wait(1)

