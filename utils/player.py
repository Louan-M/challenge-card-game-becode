import random

class Player:
    """
    Class containing the Players
    
    """

    def play(name, cards):
     
        # Give a random card to the player by using random.choice from random
        active_card = random.choice(cards)
        print(f"Player name: {name} \n {active_card}")
        
        return active_card