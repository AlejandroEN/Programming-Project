from pydealer import Deck, const
from random import shuffle

SYMBOLS = {"Diamonds": ["♦", "♢"], "Clubs": ["♣", "♧"], "Hearts": ["♥", "♡"], "Spades": ["♠", "♤"]}
SHORT_VALUE = {"Jack": "J", "Queen": "Q", "King": "K", "Ace": "1"}

def get_cards(number_of_different_cards: int):
    deck = Deck().shuffle()
    hand = deck.deal(number_of_different_cards)
    list_of_cards = []

    for card in hand:
        new_card_value = f"{SHORT_VALUE[card.value] if card.value in const.VALUES[9:] else card.value}"
        new_card_suit = SYMBOLS[card.suit]
        list_of_cards.append(f"{new_card_value} {new_card_suit[0]}")
        list_of_cards.append(f"{new_card_value} {new_card_suit[1]}")

    return shuffle(list_of_cards)

def get_players_order(players):
    playing_order = []
    player

    for i in players:
        deck = Deck().shuffle()
        card = deck.deal(1)
