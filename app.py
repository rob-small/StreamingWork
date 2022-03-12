# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 22:23:34 2022

@author: mr_ro

Expose all methods via web service
Initialize values via command line
Make port # configurable by command line

"""
# save this as app.py
from flask import Flask, jsonify, request
from mydevice import myDevice

app = Flask(__name__)


theDevice =  myDevice(20,5,'dev1')

@app.route('/device_name')
def get_name():
    return jsonify(theDevice.name)

@app.route('/device_reading')
def get_reading():
    return jsonify(theDevice.take_reading())

@app.route('/device_settings',methods = ['GET','PUT'])
def device_settings():
    if(request.method == 'GET'):
        settings = {
                'mean':theDevice.mean,
                'stdev':theDevice.stdev
            }
        return jsonify(settings)
    else:
        pass      
        if request.is_json:
            settings = request.get_json()
            theDevice.mean = float(settings["mean"])
            theDevice.stdev = float(settings["stdev"])
            return "success", 201
        else:
            return {"error": "Request must be JSON"}, 415

if __name__ == "__main__":
    app.run()