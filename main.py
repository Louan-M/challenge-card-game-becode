import random


class Player:
    """
    Class containing the Players

    """

    def play(name, cards):


        print(cards)
        
        input_card = input(f"{name}, please choose a card from the list: ")
        
        if input_card in cards:
            active_card = input_card
        else:
            print("The card chosen is not in the list. Please choose a card again: ")
            active_card = input(f"{name}, please choose a card from the list: ")
        

        return active_card


