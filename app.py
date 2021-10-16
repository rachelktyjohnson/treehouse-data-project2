from constants import TEAMS, PLAYERS


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


if __name__ == '__main__':
    players = clean_data(PLAYERS)

