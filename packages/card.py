from card_model import Card
from player_model import Player
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

def get_players_order(players: list[Player]) -> tuple[dict[Player, Card], list[Player]]:
    card_per_player: dict[Player, Card] = {}
    hand: Stack = _get_hand(len(players))

    for i in range(len(players)):
        reformatted_card: tuple[str, list[str]] = _get_reformatted_card(hand[i])
        card = Card(reformatted_card[0], reformatted_card[1][randint(0, 1)])
        card_per_player[players[i]] = card

    playing_order = sorted(card_per_player.items(), key=lambda item: int(_NUMBER_VALUE[item[1].value] if item[1].value in const.VALUES[9:] else item[1].value), reverse=True)
    return card_per_player, [player_card[0] for player_card in playing_order]

def _get_hand(number_of_different_cards: int) -> Stack:
    deck = Deck()
    deck.shuffle()
    return deck.deal(number_of_different_cards)

def _get_reformatted_card(card: PyDealerCard) -> tuple[str, list[str]]:
    card_value: str = _SHORT_VALUE[card.value] if card.value in const.VALUES[9:] else card.value
    card_suit: list[str] = _SYMBOLS[card.suit]
    return card_value, card_suit