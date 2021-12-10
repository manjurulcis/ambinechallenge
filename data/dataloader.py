import pandas as pd
import numpy as np

class dataloader:
    
    def __init__(self):
        self.teams = pd.DataFrame(pd.read_csv('data/team_info.csv'))
        self.games = pd.DataFrame(pd.read_csv('data/game_data.csv'))
        
    def get_team_info(self, team_id):
        condition = self.teams['team_id'] == int(team_id)
        return self.teams[condition]
    
    def get_season_state(self, season, team_id):
        conditions = self.games['season'] == int(season) and self.games['tea']
        team = self.teams[conditions]
        print(np.unique(team.groupby('home_team_id'), axis=0))
        return team