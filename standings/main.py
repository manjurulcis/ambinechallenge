from flask import Flask
import pandas as pd
import json
from data import dataloader

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/standing/<season>')
def standing(season): 
    if type(season) != 'int':
        return 'Invalid season id'
     
    df = pd.read_csv('data/game_data.csv')
    dataframe = pd.DataFrame(df)
    teams = dataloader.dataloader().get_season_state(season)
    
    return json.dumps(teams)
