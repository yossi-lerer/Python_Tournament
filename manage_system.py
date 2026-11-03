from main_menu import show_menu
from user_input_func import user_input
from team_func import add_team, display_team, get_all_teams, organizing_team_info

def main_system():

    teams = []
    show_menu()
    user_choose_menu = user_input("please enter the your choose for the menu")

    while True:
        if user_choose_menu == "1":
            team_name = user_input("to add new team please enter the team name")
            team_info = organizing_team_info(team_name)
            teams.append(team_info)
            print(teams)
        elif user_choose_menu == "2":
            display_team(get_all_teams())
        elif user_choose_menu == "exit":
            break
        user_choose_menu = user_input("please enter the your choose for the menu")
