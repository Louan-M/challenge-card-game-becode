import random

class Player:
    """
    """

    def play(name, cards):
     
        active_card = random.choice(cards)
        print(f"Player name: {name} \n {active_card}")
        
        return active_card
    
    