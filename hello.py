import os
import socket

from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "HelloWorld")
    hostname=socket.gethostname()
    return render_template('index.html', name=name, hostname=hostname)