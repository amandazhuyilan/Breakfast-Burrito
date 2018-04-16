# Assumptions made for this version of monoploy:
# - When a player lands on other player's property, the rent paid will be correct.import
# - No trading properties allowed once the property is purchased.
# - Every player plays in the same order for each round
# - No player will leave the game until it ends, no player will be added into the game after it starts


import sys
import re


def Monopoly():
    players_name = []  # keeping track of the players in this game, the index of the player's name will correspond to the index in roll and money lists
    num_players = 0 # numbers of players in the game 
    rolls = []  # keeping track of player's roll
    money = []  # keeping track of player's money
    property_owned = []  # keeping track of the properties purchased in the entire game

    with open(sys.argv[1], 'r') as input_file:
        content_lines = input_file.readlines()

        # reading in every turn and splitting words by space
        # each line represents one turn
        for index in range(len(content_lines)):
            # split each line by , remove {} at start and beginning of line
            line = content_lines[index]
            # remove {} at start and beginning of line
            line = line.replace("}","")
            line = line.replace("{","")
            line = line.replace("\n","")
            line = line.split(',')
            for sub_line in line:
                entry = sub_line.split(':')
                # # 1. add names into players_name and players_info
                if entry[0] == "\"player\"":
                    player_name = entry[1]
                    player_name = player_name.replace("\xe2\x80\x9c", "").replace(
                        "\xe2\x80\x9d", "")   # remove hex characters

                    if player_name not in players_name:
                        players_name.append(player_name)
                    else:
                        num_players = len(players_name)
                    break

        for index in range(len(content_lines)):
            # split each line by , remove {} at start and beginning of line
            line = content_lines[index]
            # remove {} at start and beginning of line
            line = line.replace("}","")
            line = line.replace("{","")
            line = line.replace("\n","")
            line = line.split(',')
 
            # # 2. adding rolls 
            for sub_line in line:
                entry = sub_line.split(':')            
                if entry[0] == "\"roll\"":
                    if len(rolls) < num_players:
                        rolls.append(int(entry[1]))   #initializing the rolls lists
                        print("added in rolls")
                    else:
                        player_index = index % num_players
                        rolls[player_index] = rolls[player_index] + int(entry[1])

            print rolls

if __name__ == "__main__":
    Monopoly()
