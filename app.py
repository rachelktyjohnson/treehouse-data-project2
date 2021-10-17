from constants import TEAMS, PLAYERS
from time import sleep


def clean_data(raw_players):
    clean_players = []

    for player in raw_players:
        new_player = {
            'name': player['name'],
            'height': int(player['height'].split(' ')[0]),
            'experience': True if player['experience'] == 'YES' else False,
            'guardian': player['guardians'].split(' and ')
        }
        clean_players.append(new_player)
    return clean_players


def balance_teams(cleaned_players, raw_teams):
    # order players by experience
    all_players = sorted(cleaned_players, key=lambda d: (d['experience']), reverse=True)

    # then sort evenly into teams
    balanced_teams = {}
    for team_name in raw_teams:
        balanced_teams[team_name] = {}
        balanced_teams[team_name]['players'] = []

    while len(all_players) > 0:
        for team_name in raw_teams:
            balanced_teams[team_name]['players'].append(all_players.pop(0))

    for team_name in raw_teams:
        team = balanced_teams[team_name]
        team['players'] = sorted(team['players'], key=lambda d: (d['height']), reverse=True)
        team['experienced'] = len([player for player in team['players'] if player['experience']])
        team['inexperienced'] = len([player for player in team['players'] if player['experience'] is False])
        heights = [player['height'] for player in team['players']]
        team['avg_height'] = round(sum(heights) / len(heights), 1)
    return balanced_teams


def display_team(balanced_teams, team_name):
    team = balanced_teams[team_name]
    print(f"Team {team_name} Stats")
    print("--------------------")
    print(f"Total players: {len(team['players'])}")
    print(f"Total experienced: {team['experienced']}")
    print(f"Total inexperienced: {team['inexperienced']}")
    print(f"Average height: {team['avg_height']}")
    print("\nPlayers on team:")
    print(", ".join([f"{player['name']} ({player['height']})" for player in team['players']]))
    print("\nGuardians:")
    print(", ".join([", ".join(player['guardian']) for player in team['players']]))


def show_menu():
    running = True
    while running:
        print("\n---- MENU----\n")
        print("Here are your choice:")
        print("A) Display Team Stats")
        print("B) Quit")
        menu_option = input("Please enter an option (A/B): ")
        while menu_option not in ['A', 'B']:
            menu_option = input("Please enter an option (A/B): ")
        if menu_option == 'B':
            running = False
        else:
            print("\nWhat team do you want to view the stats of?\n")
            print("A) Panthers")
            print("B) Bandits")
            print("C) Warriors")
            team_option = input("Please enter an option (A/B/C): ")
            while team_option not in ['A', 'B', 'C']:
                team_option = input("Please enter an option (A/B/C): ")
            if team_option == 'A':
                display_team(teams, 'Panthers')
            elif team_option == 'B':
                display_team(teams, 'Bandits')
            else:
                display_team(teams, 'Warriors')

            input("\nPress ENTER to continue...\n")


if __name__ == '__main__':
    print("└[∵┌]└[ ∵ ]┘[┐∵]┘")
    print("Welcome to the Basketball Team Stats Tool!")
    sleep(0.5)
    print("Cleaning data...")
    sleep(0.5)
    print("Balancing teams...")
    sleep(0.5)

    players = clean_data(PLAYERS)
    teams = balance_teams(players, TEAMS)
    show_menu()
    print("Thanks for using the Basketball Team Stats Tool!")
