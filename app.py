# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 22:23:34 2022

@author: mr_ro

x - Expose all methods via web service
x- Add support for more than one device
x - Add support for dynamic creation of device
Initialize values via command line
Make port # configurable by command line

"""
# save this as app.py
from flask import Flask, jsonify, request, render_template
from mydevice import myDevice

app = Flask(__name__)

device_list = {}

@app.route('/devices',methods = ['GET','POST'])
def devices():
    dlist = []
    for d in device_list:
        dlist.append(dict(name = device_list[d].name,
                           mean = device_list[d].mean,
                           stdev = device_list[d].stdev)
                      )                        

    if(request.method == 'GET'):
        if request.is_json:
            return jsonify(dlist)
        else:
            return render_template('home.html', items=dlist)
    else:            
        settings = request.get_json()

        new_device = myDevice(float(settings["mean"]),
                                float(settings["stdev"]),
                                settings["name"])

        device_list[settings["name"]] = new_device
        
        dlist.append(dict(name = new_device.name,
                           mean = new_device.mean,
                           stdev = new_device.stdev)
                      )
        return jsonify(dlist)
       
@app.route('/devices',methods = ['PUT'])
def device_set():
    if request.is_json:
        settings = request.get_json()
        dev = device_list[settings["name"]]
        dev.mean = float(settings["mean"])
        dev.stdev = float(settings["stdev"])
        return "success", 201
    else:
        return {"error": "Request must be JSON"}, 415

@app.route('/devices/reading',methods = ['GET'])
def get_reading():
    if request.is_json:
        settings = request.get_json()
        dev = device_list[settings["name"]]
        return jsonify(dev.take_reading())
    else:
        return {"error": "Request must be JSON"}, 415

if __name__ == "__main__":
    app.run()