from json_fs import read_data, update_data

def organizing_match_info(home_team_id, away_team_id, home_goals, away_goals):
    match = {
        "home_team_id": home_team_id, 
        "away_team_id": away_team_id,
        "home_goals": home_goals, 
        "away_goals": away_goals
        }
    return match

def update_team_by_result(teams, match_result):
    for team in teams:
        if team["id"] == match_result["home_team_id"]:
            team["goals_for"] += match_result["home_goals"]
            team["goals_against"] += match_result["away_goals"]

            if match_result["home_goals"] > match_result["away_goals"]:
                team["wins"] += 1
                team["points"] += 3
            elif match_result["home_goals"] == match_result["away_goals"]:
                team["draws"] += 1
                team["points"] += 1
            elif match_result["home_goals"] < match_result["away_goals"]:
                team["losses"] += 1
            
        if team["id"] == match_result["away_team_id"]:
            team["goals_for"] += match_result["away_goals"]
            team["goals_against"] += match_result["home_goals"]

            if match_result["away_goals"] > match_result["home_goals"]:
                team["wins"] += 1
                team["points"] += 3
            elif match_result["away_goals"] == match_result["home_goals"]:
                team["draws"] += 1
                team["points"] += 1
            elif match_result["away_goals"] < match_result["home_goals"]:
                team["losses"] += 1
            
    update_data("teams.json", teams)
