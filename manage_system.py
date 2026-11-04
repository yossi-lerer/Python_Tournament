from main_menu import show_menu
from user_input_func import user_text_input, user_num_input
from team_func import organizing_team_info
from result_func import organizing_match_info, update_team_by_result
from json_fs import writing_data, read_data
from display import display_list
from validation import validate_team_not_exists, validate_not_played_in_the_past
from data_sorting import sorting_scraping_groups

def main_system():


    while True:

        show_menu()

        user_choose_menu = user_num_input("please enter the your choose for the menu")

        if  isinstance(user_choose_menu, bool):
            print("please enter only positive number")
            continue

        if user_choose_menu == 1:
            while True:
                team_name = user_text_input("to add new team please enter the team name")
                team_id = user_num_input("to add new team please enter the team team_id")
                team_info = organizing_team_info(team_id, team_name)
                if validate_team_not_exists(read_data("teams.json"), team_info):
                    print(writing_data("teams.json",team_info))
                    break
                print("the team is exist!")
        elif user_choose_menu == 2:
            display_list(read_data("teams.json"))
        elif user_choose_menu == 3:
            home_team_id = user_num_input("home_team_id")
            away_team_id = user_num_input("away_team_id")
            home_goals = user_num_input("home_goals")
            away_goals = user_num_input("away_goals")
            match_info = organizing_match_info(home_team_id, away_team_id, home_goals, away_goals)
            if validate_not_played_in_the_past(read_data("match.json"), match_info):
                print(writing_data("match.json",match_info))
                update_team_by_result(read_data("teams.json"), match_info)
            else:
                print("the game is played in the past")
        elif user_choose_menu == 4:
            display_list(sorting_scraping_groups(read_data("teams.json")))
        elif user_choose_menu == 5:
            display_list([sorting_scraping_groups(read_data("teams.json"))[0]])
        elif user_choose_menu == 6:
            pass
        elif user_choose_menu == 0:
            break
