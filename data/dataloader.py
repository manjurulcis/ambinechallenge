import pandas as pd
import numpy as np
import json
from collections import OrderedDict

class dataloader:
    
    def __init__(self):
        self.teams = pd.DataFrame(pd.read_csv('data/team_info.csv'))
        self.games = pd.DataFrame(pd.read_csv('data/game_data.csv'))
        
    def get_team_info(self, team_id):
        condition = self.teams['team_id'] == int(team_id)
        return self.teams[condition]
    
    def get_season_state(self, season):
        conditions = self.games['season'] == int(season)
        seasongames = self.games[conditions]
        seasongames = seasongames.to_json(orient='records')
        teams = self.teams.to_json(orient='records')
        
        #return season teams
        returnData = list()
        for team in json.loads(teams):
            teamGoals = dict()
            teamGoals['name'] = team['teamName']
            teamGoals['points'] = 0
            teamGoals['wins'] = 0
            teamGoals['lossed'] = 0
            teamGoals['total'] = 0
            for game in json.loads(seasongames):
                if team['team_id'] == game['away_team_id'] and int(game['away_goals']) > int(game['home_goals']) and game['type'] == 'R':
                    teamGoals['points'] += 2
                    teamGoals['wins'] += 1
                    teamGoals['total'] += 1
                    
                elif team['team_id'] == game['home_team_id'] and int(game['away_goals']) < int(game['home_goals']) and game['type'] == 'R':     
                    teamGoals['points'] += 2
                    teamGoals['wins'] += 1
                    teamGoals['total'] += 1
                    
                elif team['team_id'] == game['away_team_id'] and int(game['away_goals']) < int(game['home_goals']) and game['type'] == 'R':
                    teamGoals['lossed'] += 1
                    teamGoals['total'] += 1
                    
                elif team['team_id'] == game['home_team_id'] and int(game['away_goals']) > int(game['home_goals']) and game['type'] == 'R':     
                    teamGoals['lossed'] += 1
                    teamGoals['total'] += 1    
                    
                elif team['team_id'] == game['home_team_id'] or team['team_id'] == game['away_team_id'] and game['type'] == 'P':     
                    teamGoals['points'] += 1
                    teamGoals['total'] += 1                          
                    
            returnData.append(teamGoals)        
                    
        return returnData
            