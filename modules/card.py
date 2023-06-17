from card_model import Card
from pydealer import Deck, const, Stack, Card as PyDealerCard
from random import shuffle, randint

_SYMBOLS = {"Diamonds": ["♦", "♢"], "Clubs": ["♣", "♧"], "Hearts": ["♥", "♡"], "Spades": ["♠", "♤"]}
_SHORT_VALUE = {"Jack": "J", "Queen": "Q", "King": "K", "Ace": "A"}
_NUMBER_VALUE = {"Jack": 11, "Queen": 12, "King": 13, "Ace": 14}

def get_pairs_of_cards(number_of_different_cards: int) -> list[Card]:
    hand: Stack = _get_hand(number_of_different_cards)
    list_of_cards: list[Card] = []

    for py_dealer_card in hand:
        formatted_card: tuple[str, list[str]] = _get_reformatted_card(py_dealer_card)
        value: str = formatted_card[0]
        suit: str = formatted_card[1][randint(0, 1)]

        card = Card(value, suit)
        list_of_cards.append(card)

    list_of_cards *= 2
    shuffle(list_of_cards)
    return list_of_cards

def _get_hand(number_of_different_cards: int) -> Stack:
    """Generates and sorts the choosen set of cards for one hand deal.
        Structured for constant usage."""

    deck = Deck()
    deck.shuffle()
    return deck.deal(number_of_different_cards)

def _get_reformatted_card(card: PyDealerCard) -> tuple[str, list[str]]:
    """Calls for the card type and asigns symbols to each card in through.
        Designed for constant interaction."""

    card_value: str = _SHORT_VALUE[card.value] if card.value in const.VALUES[9:] else card.value
    card_suit: list[str] = _SYMBOLS[card.suit]
    return card_value, card_suit