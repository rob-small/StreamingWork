# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 15:41:10 2022

@author: mr_ro

x - Setup as an object
x - Have mean and standard deviation changeable
x - Have it run every second and pump out a reading to stdout
Add name attribute
Add timestamp and name to output
"""

from numpy.random import default_rng
from threading import Event

class myDevice:
    
    def __init__(self, mean, stdev):
        self.mean = mean
        self.stdev = stdev  
        self._rng = default_rng()
  
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
        

gauge1 = myDevice(20,5)

while 1:
    print(gauge1.take_reading())
    Event().wait(1)