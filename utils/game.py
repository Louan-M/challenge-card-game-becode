from utils.player import Player
from utils.card import Deck

class Board:
    """
    """

    def start_game(number_of_players, list_of_players):

        print("Starting the game ...\n")
        cards = Deck.fill_deck()
    
        Deck.shuffle(cards)
       # print(cards)

        distribute = Deck.distribute(list_of_players, cards)
    
        number_of_turns = 52 / 2 # 26
        turn_count = 0
        
        while turn_count < number_of_turns:
            
            for name, card in distribute.items():
                
                active_card = Player.play(name, cards) 
                cards.remove(active_card)
                
            turn_count += 1
        
        print("\n*** End of the game *** ")
