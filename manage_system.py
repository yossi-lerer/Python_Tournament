from main_menu import show_menu
from user_input_func import user_text_input, user_positive_num_input
from team_func import add_team, display_team, get_all_teams, organizing_team_info
from result_func import add_match_result

def main_system():

    teams = []

    while True:
        show_menu()
        user_choose_menu = user_positive_num_input("please enter the your choose for the menu")
        if user_choose_menu == 1:
            team_name = user_text_input("to add new team please enter the team name")
            team_id = user_positive_num_input("to add new team please enter the team team_id")

            team_info = organizing_team_info(team_id, team_name)
            teams.append(team_info)
            print(teams)
        elif user_choose_menu == 2:
            display_team(get_all_teams())
        elif user_choose_menu == 3:
            home_team_id = user_positive_num_input("home_team_id")
            away_team_id = user_positive_num_input("away_team_id")
            home_goals = user_positive_num_input("home_goals")
            away_goals = user_positive_num_input("away_goals")
            print(add_match_result(home_team_id, away_team_id, home_goals, away_goals))
        elif user_choose_menu == 0:
            break
