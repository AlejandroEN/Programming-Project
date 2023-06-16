from pydealer import Deck, const, Stack, Card
from random import shuffle

SYMBOLS = {"Diamonds": ["♦", "♢"], "Clubs": ["♣", "♧"], "Hearts": ["♥", "♡"], "Spades": ["♠", "♤"]}
SHORT_VALUE = {"Jack": "J", "Queen": "Q", "King": "K", "Ace": "A"}
NUMBER_VALUE = {"Jack": 11, "Queen": 12, "King": 13, "Ace": 14}

def get_cards(number_of_different_cards: int) -> list[str]:
    """Generates a list, containing a disorganized group of pairs of cards."""

    hand: Stack = get_hand(number_of_different_cards)
    list_of_cards: list[str] = []

    for card in hand:
        card = get_reformatted_card(card)
        list_of_cards.append(f"{card[0]} {card[1][0]}")
        list_of_cards.append(f"{card[0]} {card[1][1]}")

    shuffle(list_of_cards)
    return list_of_cards

def get_hand(number_of_different_cards) -> Stack:
    deck = Deck()
    deck.shuffle()
    return deck.deal(number_of_different_cards)

def get_reformatted_card(card: Card) -> tuple[str, list[str]]:
    card_value = SHORT_VALUE[card.value] if card.value in const.VALUES[9:] else card.value
    card_suit = SYMBOLS[card.suit]
    return card_value, card_suit