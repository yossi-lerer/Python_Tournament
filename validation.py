def validate_positive_number(number):
    try:
        if int(number) >= 0 and isinstance(int(number), int) and not isinstance(int(number), bool):
            return True
        else:
            return False
    except:
        return False

def validate_str_empty(text):
    if text.strip() != "":
        return True
    
def validate_team_not_exists(teams, new_team):
    for team in teams:
        if team["id"] == new_team["id"]:
            return False
        if team["name"].upper() == new_team["name"].upper():
            return False
    return True

def validate_not_played_in_the_past(matches, new_match):
    for match in matches:
        if match["home_team_id"] == new_match["home_team_id"] and match["away_team_id"] == new_match["away_team_id"]:
            return False
        if match["home_team_id"] == new_match["away_team_id"] and match["away_team_id"] == new_match["home_team_id"]:
            return False
        if new_match["home_team_id"] == new_match["away_team_id"]:
            return False
    return True

if __name__ == "__main__":
    print(validate_not_played_in_the_past([
    {
        "home_team_id": 1,
        "away_team_id": 2,
        "home_goals": 1,
        "away_goals": 0
    }], 
    {
        "home_team_id": 2,
        "away_team_id": 5,
        "home_goals": 1,
        "away_goals": 0
    }))