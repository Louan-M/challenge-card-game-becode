from utils.player import Player
from utils.card import Deck


class Board:
    """
     Class containing the board

    :attrib turn_count
    :attrib active_cards

    """

    def start_game(number_of_players, list_of_players):

        print("Starting the game ...\n")

        # Call of .fill_deck() function from Deck class
        cards = Deck.fill_deck()

        # Call of .shuffle() function from Deck class
        Deck.shuffle(cards)

        # Call of the .distribute() function from Deck class
        distribute = Deck.distribute(list_of_players, cards)

        number_of_turns = 52 / 2  # 26
        turn_count = 0

        # Looping until no cards left
        while turn_count < number_of_turns:

            for name, card in distribute.items():

                # Call of .play() function from Player class
                active_card = Player.play(name, cards)

                # Remove the active card from the player cards
                cards.remove(active_card)

            turn_count += 1

        print("\n*** End of the game *** ")
