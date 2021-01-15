import random


class Symbol:
    def __init__(self, color, icon):
        self.color = color
        self.icon = icon


class Card(Symbol):
    """
    Class that inherits from the class Symbol
    :attrib value is a string from ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'  ]
    """

    def __init__(self, color, icon, value):
        super().__init__(color, icon)
        self.value = value

    def cards():

        value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        icon = ["♥", "♦", "♠", "♣"]
        cards = []

        # Loop to fill "cards" variable with 4*13 = 52 cards
        for i in range(0, 4):
            for j in range(0, 13):
                cards.append(value[j] + " " + icon[i])
        return cards


class Deck:
    """
    Class that generates the deck (52 cards)
    """

    def fill_deck():
        # Call of the .cards() function from Card class to fill the deck

        cards = Card.cards()
        return cards

    def shuffle(cards):

        # Shuffle "cards" with random.shuffle() function
        random.shuffle(cards)

    def distribute(list_of_players, cards):

        # Split of the deck ("cards" variable) between the players
        distrib_cards = {
            list_of_players[0]: cards[0:26],
            list_of_players[1]: cards[26:52],
        }
        return distrib_cards
