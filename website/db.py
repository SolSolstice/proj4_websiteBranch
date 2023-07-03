
# set up flask application 
import os
from flask import Flask
#from flask_pymongo import PyMongo
#
#from pymongo import MongoClient

from flask import render_template
from flask import request
from flask import jsonify
import csv
import json

import pandas as pd

from flask import Blueprint


app = Flask(__name__)

d_b = Blueprint('db', __name__) 


#def get_data():
#    data = data
#    return jsonify(data)

@d_b.route('/db/')
def db():
    data = 'wineDF.csv'

    return render_template('d3.html',data=data)

if __name__ == '__main__':
    app.run()


"""
import os 





basedir = os.path.abspath(os.path.dirname(__file__))
data_file = os.path.join(basedir, 'static/js/large.js')

WORDS = []
with open(data_file, "r") as file:
    for line in file.readlines():
        WORDS.append(line.rstrip())

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    q = request.args.get("q")
    words = [word for word in WORDS if word.startswith(q)]
    return jsonify(words)

    """

