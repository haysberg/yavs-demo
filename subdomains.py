#Imports
import ujson
import requests
import sys, subprocess
from app import app
from flask import Response, request


#This function takes the full subdomain URL from the subdomains() function, and checks if it's accessible.
@app.route('/subdomains/<target>')
def request_subdomain(target):
        completed = subprocess.run("cat ./json/subdomainscan.json", shell=True, stdout=subprocess.PIPE)
        output = completed.stdout.decode('utf-8')
        return Response(output, mimetype="application/json") # Send a response using JSON


