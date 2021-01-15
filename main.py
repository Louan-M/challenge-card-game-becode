''' 
    Start of the program

    :attrib player_list list of player's names
    :attrib player_name is the name of the player
    
'''

from utils.game import Board

list_of_players = ['Louan', 'Theano']
Board.start_game(2, list_of_players)