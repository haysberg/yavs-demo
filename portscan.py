import subprocess, ujson, socket, threading, sys, time
from flask import Response
from app import app
from threading import Thread, Lock
from queue import Queue

from concurrent.futures import ThreadPoolExecutor
import threading
import random

#This is the function we call when the user reaches
@app.route('/portscan/<target>')
#We have a special route here allowing us to choose what number of workers we want to run our port scanning.
#The optimal one should be "number of cores - 1"
@app.route('/portscan/<target>/<workers>')
def portscan(target, workers = 3):
    completed = subprocess.run("cat ./json/portscan.json", shell=True, stdout=subprocess.PIPE)
    output = completed.stdout.decode('utf-8')
    return Response(output, mimetype="application/json") # Send a response using JSON