from main_menu import show_menu
from user_input_func import user_text_input, user_num_input
from team_func import organizing_team_info
from result_func import organizing_match_info
from json_fs import writing_data, read_data
from validation import positive_number
def main_system():


    while True:

        show_menu()

        user_choose_menu = user_num_input("please enter the your choose for the menu")

        if not (user_choose_menu and positive_number(user_choose_menu)):
            print("please enter only positive number")
            continue

        if user_choose_menu == 1:
            team_name = user_text_input("to add new team please enter the team name")
            team_id = user_num_input("to add new team please enter the team team_id")
            if not (team_id and positive_number(team_id)):
                team_info = organizing_team_info(team_id, team_name)
                print(writing_data("teams.json",team_info))

        elif user_choose_menu == 2:
            print(read_data("teams.json"))

        elif user_choose_menu == 3:
            home_team_id = user_num_input("home_team_id")
            away_team_id = user_num_input("away_team_id")
            home_goals = user_num_input("home_goals")
            away_goals = user_num_input("away_goals")
            match_info = organizing_match_info(home_team_id, away_team_id, home_goals, away_goals)
            print(writing_data("match.json",match_info))
        
        elif user_choose_menu == 0:
            break
