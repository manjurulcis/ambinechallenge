from flask import Flask
import pandas as pd
import json
from data import dataloader

app = Flask(__name__)

@app.route('/')
def hello_world():
    df = pd.read_csv('data/game_data.csv')
    dataframe = pd.DataFrame(df)
    print(dataframe[dataframe['season'] == 20112012])
    return 'Hello, World!'


@app.route('/standing/<season>')
def standing(season):
    df = pd.read_csv('data/game_data.csv')
    dataframe = pd.DataFrame(df)
    print(dataframe[dataframe['season'] == int(season)])
    return 'Hello, World!'

@app.route('/team/<team_id>')
def team_info(team_id):
    dl = dataloader.dataloader().get_team_info(team_id)
    team = dl.to_numpy()[0]
    return {'success' : 'true', 'team' : str(team[2])}
# TODO: Add route(s) here serving standings
