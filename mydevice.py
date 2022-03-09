# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 16:14:19 2022

@author: mr_ro
"""
from numpy.random import default_rng

class myDevice:
    
    def __init__(self, mean, stdev, name = ""):
        self.mean = mean
        self.stdev = stdev
        self.name = name
        self._rng = default_rng()
  
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name = value
    
    @property
    def mean(self):
        return self._mean
    
    @mean.setter
    def mean(self,value):
        self._mean = value

    @property
    def stdev(self):
        return self._stdev
    
    @stdev.setter
    def stdev(self,value):
        self._stdev = value

    def take_reading(self):
        return self._rng.normal(self.mean,self.stdev)
