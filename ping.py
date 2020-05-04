#Usual imports
import subprocess, ujson
from flask import Response
from app import app

#This code will be executed when the URL is reached.
#<target> means that we give it a parameter
@app.route('/ping/<target>')
def ping(target):
    completed = subprocess.run("cat ./json/ping.json", shell=True, stdout=subprocess.PIPE)
    output = completed.stdout.decode('utf-8')
    return Response(output, mimetype="application/json")