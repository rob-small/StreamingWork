# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 22:23:34 2022

@author: mr_ro
"""
# save this as app.py
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)