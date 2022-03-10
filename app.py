# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 22:23:34 2022

@author: mr_ro
"""
# save this as app.py
from flask import Flask, jsonify
from mydevice import myDevice

app = Flask(__name__)


theDevice =  myDevice(20,5,'dev1')

@app.route('/device_name')
def get_name():
    return jsonify(theDevice.name)

@app.route('/device_reading')
def get_reading():
    return jsonify(theDevice.take_reading())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)