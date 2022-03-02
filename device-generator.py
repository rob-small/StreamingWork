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
"""

from numpy.random import default_rng
from threading import Event
from datetime import datetime
import json

class myDevice:
    
    def __init__(self, mean, stdev, name = ""):
        self.mean = mean
        self.stdev = stdev
        self.name = name
        self._rng = default_rng()
  
    @property
    def name(self):
#        print ("mean getter")
        return self._name

    @name.setter
    def name(self,value):
        self._name = value
    
    @property
    def mean(self):
#        print ("mean getter")
        return self._mean
    
    @mean.setter
    def mean(self,value):
#        print ("mean setter")
        self._mean = value

    @property
    def stdev(self):
#        print ("stdev getter")
        return self._stdev
    
    @stdev.setter
    def stdev(self,value):
#        print ("stdev setter")
        self._stdev = value

    def take_reading(self):
        return self._rng.normal(self.mean,self.stdev)
        

gauge1 = myDevice(20,5,"dev1")

gauge1_out = {}
gauge1_out['name'] = gauge1.name

while 1:
    gauge1_out['timestamp'] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S:%f")
    gauge1_out['reading'] = gauge1.take_reading()
    print(json.dumps(gauge1_out), flush=True)
    Event().wait(1)