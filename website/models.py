
""" 
from . import db

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from flask import render_template
from flask import Blueprint
from sqlalchemy.sql import func

import pickle

class Note(db.Model):
    id = db.column(db.Integer,primary_key=True)
    data = db.column(db.string(10000)) 

class wineV(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    variety = db.Column(db.String(50))


model = Blueprint('models', __name__) 

@model.route('/models/', methods=['GET', 'POST'])
def showModel():

    return render_template('models.html')
"""