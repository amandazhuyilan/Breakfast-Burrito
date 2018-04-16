# Assumptions made for this version of monoploy:
# - No empty or invalid inputs
# - When a player lands on other player's property, the rent paid will be correct.import
# - No trading properties allowed once the property is purchased.
# - Every player plays in the same order for each round
# - No player will leave the game until it ends, no player will be added into the game after it starts
# - Each turn is logged as "action", "price", "landed_on" sequence
# - Player only pays for property rent if it is already purchased by another owner


import sys
import re


def Monopoly():
    players_name = []  # keeping track of the players in this game, the index of the player's name will correspond to the index in roll and total_money lists
    num_players = 0  # numbers of players in the game
    rolls = []  # keeping track of player's roll
    total_money = []  # keeping track of player's total_money
    rent_money = []  # keeping track of money made from rent
    # keeping track of the properties purchased and who owns it: 'property_name': 'owner'
    property_dict = {}

    with open(sys.argv[1], 'r') as input_file:
        content_lines = input_file.readlines()

        # Get the number of players
        # reading in every turn and splitting words by space
        # each line represents one turn
        for index in range(len(content_lines)):
            # split each line by , remove {} at start and beginning of line
            line = content_lines[index]
            # remove {} at start and beginning of line
            line = line.replace("}", "")
            line = line.replace("{", "")
            line = line.replace("\n", "")
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
                    break   # once the same name shows up, break out of loop

        # initalize total_money list: each player gets $500 in the beginning
        # initalize rent_money list with 0
        for elem in range(num_players):
            total_money.append(500)
            rent_money.append(0)

        for index in range(len(content_lines)):
            # split each line by , remove {} at start and beginning of line
            line = content_lines[index]
            # remove {, }, \n a
            line = line.replace("}", "")
            line = line.replace("{", "")
            line = line.replace("\n", "")
            line = line.split(',')

            each_turn = []
            for sub_line in line:
                # append in all fields into each_turns list
                each_turn.extend(sub_line.split(':'))

            # make sure each turn's operations will result in the right player's rolls/total_money list
            player_index = index % num_players

            # calculating where player is on the board by adding each player's roll of each round
            if each_turn[-2] == "\"roll\"":
                    # populate rolls for the first round of turns
                if len(rolls) < num_players:
                        # initializing the rolls lists
                    rolls.append(int(each_turn[-1]))
                else:
                    rolls[player_index] = rolls[player_index] + \
                        int(each_turn[-1])
                    # if player has already passed 40 blocks, reset roll value (minus 40) and add $200 to player's total_money
                    if rolls[player_index] >= 40:
                        rolls[player_index] = rolls[player_index] - 40
                        total_money[player_index] = total_money[player_index] + 200

                # # tracking property purchasing information, update property_dict
                # # if player is bankrupt and tries to pay for property, will throw error and exit
            if each_turn[1] == "\"purchase\"":
                # check if player is already bankrupt before purchasing property
                if total_money[player_index] <= 0:
                    print "Player", players_name[player_index], "is bankrupt and tried to purchase property! GAME OVER!\n"
                    print_results(players_name, rolls, total_money, property_dict,
                                  rent_money, cheat=true, cheater=players_name[player_index])

                    return
                else:
                    # current player pays for property
                    total_money[player_index] = total_money[player_index] - \
                        int(each_turn[3])
                    property_dict[each_turn[5]] = players_name[player_index]

            # tracking rent paying info, look up who to pay to on property_dict
            # if player is bankrupt and tries to pay rent, will throw error and exit
            if each_turn[1] == "\"paid rent\"":
                # check if player is already bankrupt before purchasing property
                if total_money[player_index] <= 0:
                    print "Player", players_name[player_index], "is bankrupt and tried to purchase property! GAME OVER!\n"
                    print_results(players_name, rolls, total_money, property_dict,
                                  rent_money, cheat=True, cheater=players_name[player_index])
                    return

                else:
                    # current player pays for rent
                    total_money[player_index] = total_money[player_index] - \
                        int(each_turn[3])
                # property owner gets total_money
                for owned_property, owned_by in property_dict.items():
                    if owned_property == each_turn[5]:
                        owner_index = players_name.index(
                            owned_by)  # get property owner's index
                        total_money[owner_index] = total_money[owner_index] + \
                            int(each_turn[3])
                        rent_money[owner_index] = rent_money[owner_index] + \
                            int(each_turn[3])

        print_results(players_name, rolls, total_money,
                      property_dict, rent_money, cheat=False, cheater=None)


def print_results(players_name, rolls, total_money, property_dict, rent_money, cheat, cheater):
    print "Summary of game:\n"
    if cheat:
        print "Player", cheater, "cheated in the game."
    else:
        print "No one cheated!"

    max_money_index = total_money.index(max(total_money))
    print "Player ", players_name[max_money_index], "had the most money at the end of the game, $", total_money[max_money_index], ".\n"

    print "Summary of players:\n"
    for i in range(len(players_name)):
        print "Player", players_name[i], "ended with $", str(total_money[i]), ", made $", rent_money[i], "from rent, and owned the following properties:"
        for owned_property, owned_by in property_dict.items():
            if owned_by == players_name[i]:
                print owned_property
        print "\n"


if __name__ == "__main__":
    Monopoly()
