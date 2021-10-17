from constants import TEAMS, PLAYERS
import pprint

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
    # split players into experienced and inexperienced and then recombine
    exp_players = []
    inexp_players = []
    for player in cleaned_players:
        if player['experience']:
            exp_players.append(player)
        else:
            inexp_players.append(player)
    all_players = exp_players + inexp_players

    # then sort evenly into teams
    balanced_teams = {}
    for team_name in raw_teams:
        balanced_teams[team_name] = []

    while len(all_players) > 0:
        for team_name in raw_teams:
            balanced_teams[team_name].append(all_players.pop(0))

    return balanced_teams


def display_team(balanced_teams, team_name):
    team = balanced_teams[team_name]
    print(f"Team {team_name} Stats")
    print("--------------------")
    print(f"Total players: {len(team)}")
    print(f"Total experienced: {len([player for player in team if player['experience'] == True]) }")
    print(f"Total experienced: {len([player for player in team if player['experience'] == False]) }")
    heights = [player['height'] for player in team]
    print(f"Average height: {round(sum(heights)/len(heights),1)}")
    print("\nPlayers on team:")
    print(", ".join([player['name'] for player in team]))
    print("\nGuardians:")
    print(", ".join([", ".join(player['guardian']) for player in team]))


if __name__ == '__main__':
    players = clean_data(PLAYERS)
    teams = balance_teams(players, TEAMS)
    display_team(teams, 'Panthers')

