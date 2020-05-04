#Usual imports
import subprocess, ujson, re, xmltodict
from flask import Response
from app import app


@app.route('/cipherscan/<target>')
def cipherscan(target):
    completed = subprocess.run("cat ./json/cipherscan.json", shell=True, stdout=subprocess.PIPE)
    output = completed.stdout.decode('utf-8')
    
    return Response(output, mimetype="application/json")
