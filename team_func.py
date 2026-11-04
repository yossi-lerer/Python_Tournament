def organizing_team_info(team_id, team_name):
    team = {
    "id": team_id,
    "name": team_name, 
    "played": 0,
    "wins": 0, 
    "draws": 0, 
    "losses": 0,
    "goals_for": 0, 
    "goals_against": 0, 
    "points": 0
    }
    return team

def add_team():
    pass


def get_all_teams():
    teams = [{
    "id": 1,
    "name": "Maccabi", 
    "played": 0,
    "wins": 0, 
    "draws": 0, 
    "losses": 0,
    "goals_for": 0, 
    "goals_against": 0, 
    "points": 0
    },{
    "id": 1,
    "name": "Maccabi", 
    "played": 0,
    "wins": 0, 
    "draws": 0, 
    "losses": 0,
    "goals_for": 0, 
    "goals_against": 0, 
    "points": 0
    }]
    return teams

def display_team(teams:list):
    print(teams)