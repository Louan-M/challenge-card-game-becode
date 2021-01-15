import random

class Symbol:
    """
    """

    def __init__(self, color, icon):
        self.color = color
        self.icon = icon


class Card(Symbol):
    """
    """

    def __init__(self, color, icon, value):
        super().__init__(color, icon)
        self.value = value

    def cards():
        
        value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        icon = ["♥", "♦","♠","♣"]
        cards = []
        
        for i in range(0, 4):
            for j in range(0, 13):
                cards.append(value[j] + " " + icon[i])
        return cards
    

class Deck:
    """
    Class that generates the deck (52 cards)
    """

    def fill_deck():

        cards = Card.cards()
        return cards
    

    def shuffle(cards):
 
        random.shuffle(cards)
        

    def distribute(list_of_players, cards):  
   
        distrib_cards  = {list_of_players[0]: cards[0:26], list_of_players[1]: cards[26:52]}
        return distrib_cards 
    