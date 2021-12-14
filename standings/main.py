from flask import Flask
import pandas as pd
import json
import numbers
from data import dataloader

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/standing/<season>')
def standing(season): 
    try:
      season = int(season)
    except:
      return "Invalid season id"
    teams = dataloader.dataloader().get_season_state(season)
    
    return json.dumps(teams)
