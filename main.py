""" 
    Start of the program

    :attrib player_list list of player's names
    :attrib player_name is the name of the player
    
"""

from utils.game import Board

# Players

list_of_players = []

print('Please enter your names. Only two players allowed.')
player_1 = input("First player: ")
list_of_players.append(player_1)
player_2 = input("Second player: ")
list_of_players.append(player_2)
print(f"\nWelcome {player_1} and {player_2} ! Are you ready ? Let's play!")


# Starting the game by calling the function start_game() from the Board class
Board.start_game(2, list_of_players)
