#!/bin/python3
import ujson
import sys
import subprocess
from flask import Flask, Response, request
from app import app

@app.route("/webappscan/<target>")
def webappscan(target):
    completed = subprocess.run("cat ./json/webappscan.json", shell=True, stdout=subprocess.PIPE)
    output = completed.stdout.decode('utf-8')
    return Response(output, mimetype="application/json") # Send a response using JSON
    
