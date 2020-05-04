#Usual imports
from flask import Response
from app import app
import subprocess, ujson, re


@app.route('/servicescan/<target>/<ports>')
def servicescan(target, ports):
    completed = subprocess.run("cat ./json/servicescan.json", shell=True, stdout=subprocess.PIPE)
    output = completed.stdout.decode('utf-8')
    return Response(output, mimetype="application/json") # Send a response using JSON