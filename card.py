from pydealer import Deck, const
from random import shuffle

SYMBOLS = {"Diamonds": ["♦", "♢"], "Clubs": ["♣", "♧"], "Hearts": ["♥", "♡"], "Spades": ["♠", "♤"]}
SHORT_VALUE = {"Jack": "J", "Queen": "Q", "King": "K", "Ace": "1"}

def get_cards(number_of_different_cards: int):
    """Generates a list, containing a disorganized group of pairs of cards."""
    deck = Deck()
    deck.shuffle()
    hand = deck.deal(number_of_different_cards)
    list_of_cards = []

    for card in hand:
        new_card_value = f"{SHORT_VALUE[card.value] if card.value in const.VALUES[9:] else card.value}"
        new_card_suit = SYMBOLS[card.suit]
        list_of_cards.append(f"{new_card_value} {new_card_suit[0]}")
        list_of_cards.append(f"{new_card_value} {new_card_suit[1]}")

    shuffle(list_of_cards)

    return list_of_cards

def get_players_order(players):
    playing_order = []
    players_card_dictionary = {}

    for i in players:
        deck = Deck()
        deck.shuffle()
        hand = deck.deal(1)
        players_card_dictionary[i] = hand[0]

    sorted_players = sorted(players_card_dictionary.items(), key=lambda x: x[1].value, reverse=True)

    for player, card in sorted_players:
        print(f"{player}: {card}")

get_players_order(["1", "2"])