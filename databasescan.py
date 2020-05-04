#!/usr/bin/env python

import re
import subprocess, ujson
from flask import Response
from app import app

@app.route('/databasescan/<target>')
def databasescan(target):
    completed = subprocess.run("cat ./json/dbscan.json", shell=True, stdout=subprocess.PIPE)
    output = completed.stdout.decode('utf-8')
    return Response(output, mimetype="application/json")



