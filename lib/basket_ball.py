def game_dict():
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "position": "Point Guard",
                    "points_per_game": 21.7,
                    "rebounds_per_game": 3.3,
                    "assists_per_game": 8.6,
                    "steals_per_game": 1.3,
                    "blocks_per_game": 0.1,
                    "career_points": 3142,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Evan Mobley",
                    "number": 4,
                    "position": "Center",
                    "points_per_game": 15.0,
                    "rebounds_per_game": 8.3,
                    "assists_per_game": 2.5,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.7,
                    "career_points": 1034,
                    "age": 21,
                    "height_inches": 83,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Kevin Love",
                    "number": 0,
                    "position": "Power Forward",
                    "points_per_game": 13.6,
                    "rebounds_per_game": 7.2,
                    "assists_per_game": 2.2,
                    "steals_per_game": 0.4,
                    "blocks_per_game": 0.2,
                    "career_points": 14305,
                    "age": 34,
                    "height_inches": 80,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Isaac Okoro",
                    "number": 35,
                    "position": "Small Forward",
                    "points_per_game": 8.8,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 1.8,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 0.3,
                    "career_points": 1234,
                    "age": 21,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Ricky Rubio",
                    "number": 99,
                    "position": "Point Guard",
                    "points_per_game": 13.1,
                    "rebounds_per_game": 4.1,
                    "assists_per_game": 6.6,
                    "steals_per_game": 1.4,
                    "blocks_per_game": 0.2,
                    "career_points": 7399,
                    "age": 31,
                    "height_inches": 74,
                    "shoe_brand": "Adidas",
                },
            ],
        },
            
        "away": {
            "team_name": "Washington Wizards",
            "colors": ["Red", "White", "Navy Blue"],
            "players": [   
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "position": "Shooting Guard",
                    "points_per_game": 23.2,
                    "rebounds_per_game": 4.7,
                    "assists_per_game": 6.6,
                    "steals_per_game": 0.9,
                    "blocks_per_game": 0.4,
                    "career_points": 14231,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "position": "Power Forward",
                    "points_per_game": 17.1,
                    "rebounds_per_game": 8.5,
                    "assists_per_game": 3.5,
                    "steals_per_game": 0.6,
                    "blocks_per_game": 0.9,
                    "career_points": 5336,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
                {
                    "name": "Kentavious Caldwell-Pope",
                    "number": 1,
                    "position": "Shooting Guard",
                    "points_per_game": 13.2,
                    "rebounds_per_game": 3.4,
                    "assists_per_game": 1.9,
                    "steals_per_game": 1.1,
                    "blocks_per_game": 0.3,
                    "career_points": 7911,
                    "age": 29,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Davis Bertans",
                    "number": 42,
                    "position": "Power Forward",
                    "points_per_game": 5.6,
                    "rebounds_per_game": 2.1,
                    "assists_per_game": 0.6,
                    "steals_per_game": 0.3,
                    "blocks_per_game": 0.3,
                    "career_points": 3165,
                    "age": 29,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kristaps Porzingis",
                    "number": 6,
                    "position": "Power Forward",
                    "points_per_game": 22.1,
                    "rebounds_per_game": 8.8,
                    "assists_per_game": 2.9,
                    "steals_per_game": 0.7,
                    "blocks_per_game": 1.5,
                    "career_points": 6371,
                    "age": 27,
                    "height_inches": 87,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Rui Hachimura",
                    "number": 8,
                    "position": "Power Forward",
                    "points_per_game": 11.3,
                    "rebounds_per_game": 3.8,
                    "assists_per_game": 1.1,
                    "steals_per_game": 0.5,
                    "blocks_per_game": 0.2,
                    "career_points": 1913,
                    "age": 24,
                    "height_inches": 80,
                    "shoe_brand": "Jordan",
                },
            ]
        }
    }


import ipdb
import pprint

# HELPER METHODS
def get_all_players():
    pass
    # the python * operator does the same job as the spread operator in JS
    # create an array of all the players
    return [*game_dict()['home']['players'], *game_dict()['away']['players']]

def get_player(player_name):
    pass
    for player_obj in get_all_players():
        if player_obj['name'] == player_name:
            return player_obj
        
    return None

def get_team(team_name):
    pass
    for team in game_dict():
        pass
        current_team = game_dict()[team]
        if current_team['team_name'] == team_name:
            pass
            return current_team
    
    return None
    

# METHODS

def num_points_per_game(player_name):
    if get_player(player_name) == None:
        return "Player Not Found"
    
    return get_player(player_name)['points_per_game']
        
def player_age(player_name):
    pass
    if get_player(player_name) == None:
        return "Player Not Found"
    
    return get_player(player_name)['age']

def team_colors(team_name):
    pass
    if get_team(team_name) == None:
        return "Team Not Found"
    
    return get_team(team_name)['colors']
    

def team_names():
    pass
    team_list = []
    for team in game_dict():
        pass
        team_list.append(game_dict()[team]['team_name'])
        
    return team_list

def player_numbers(team_name):
    pass
    if get_team(team_name) == None:
        return "Team Not Found"
    
    player_numbers_list = []
    team_players = get_team(team_name)['players']
    for player in team_players:
        pass
        player_numbers_list.append(player['number'])
        
    return player_numbers_list

def player_stats(player_name):
    pass
    if get_player(player_name) == None:
        return 'Player Not Found'
    
    return get_player(player_name)

def average_rebounds_by_shoe_brand():
    pass
    all_players = get_all_players()
    my_dict = {}
    # iterate through all the players and collect each shoe brand along with the number of rebounds for that player inside of the empty dictonary
    for player in all_players:
        pass
        for stat_key in player:
            pass
            if stat_key == 'shoe_brand':
                pass
                # check if the key is already inside my_dict
                if player[stat_key] in my_dict.keys():
                    pass
                    my_dict[player[stat_key]].append(player["rebounds_per_game"])
                else:
                    pass
                    # if not, include the key in the dict, create a new array and set this element as the first element in the array
                    my_dict[player[stat_key]] = [player["rebounds_per_game"]]
    # iterate through my_dict and print the average rebounds for each show brand
    for brand in my_dict:
        pass
        print(f"{brand}: {sum(my_dict[brand])}")
    
    # ipdb.set_trace()
                

def most_career_points():
    pass
    all_players = get_all_players()
    the_one = {'name': '', 'career_points': 0 }
    # iterate through all the players and find the player with the most career points
    # then, add that players name and points to the_one dict
    # that playter becomes the player to beat, and the iteration continues
    for player in all_players:
        pass
        if player['career_points'] > the_one['career_points']:
            pass
            the_one['name'] = player['name']
            the_one['career_points'] = player['career_points']
            
    print(f"{the_one['name']} has the most career points with {the_one['career_points']} points.")

def matching_jersey_nums():
    pass
    # grab each team seperately
    home_team = game_dict()['home']['players']
    away_team = game_dict()['away']['players']
    # create a list of both teams jersey numbers
    home_nums = [player['number'] for player in home_team]
    away_nums = [player['number'] for player in away_team]
    # ipdb.set_trace()
    for idx, num in enumerate(home_nums):
        pass
        home_idx = idx
        if num in away_nums:
            pass
            away_idx = away_nums.index(num)
            return f"{home_team[home_idx]['name']} has the same jersey number as {away_team[away_idx]['name']}"
    
    return "No matches found."
    
def longest_player_name():
    pass
    all_players = get_all_players()
    longest_name = ''
    for player in all_players:
        pass
        if len(player['name']) > len(longest_name):
            pass
            longest_name = player['name']
    
    return f"{longest_name} has the longest name at {len(longest_name) - 1} characters long!"