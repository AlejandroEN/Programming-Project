from .models.card_model import Card
from .models.player_model import Player
from pydealer import Deck, const, Stack, Card as PyDealerCard
from random import shuffle, randint

_SYMBOLS: dict[str, list[str]] = {"Diamonds": ["♦", "♢"], "Clubs": ["♣", "♧"], "Hearts": ["♥", "♡"], "Spades": ["♠", "♤"]}
_SHORT_VALUE: dict[str, str] = {"Jack": "J", "Queen": "Q", "King": "K", "Ace": "A"}
_EXTENDED_VALUE: dict[str, str] = {value: key for key, value in _SHORT_VALUE.items()}
_NUMBER_VALUE: dict[str, int] = {"J": 11, "Q": 12, "K": 13, "A": 14}

def get_pairs_of_cards(number_of_different_cards: int) -> list[Card]:
    """
    Function generates a list that contains a pair of cards, utilizing the class Card.
    Defines a set number of cards to generate, appends them on list and shuffles said list.
    Each card is assigned both their respective values and hidden values.
    """
    hand: Stack = _get_hand(number_of_different_cards)
    list_of_cards: list[Card] = []

    for py_dealer_card in hand:
        formatted_card: tuple[str, list[str]] = _get_reformatted_card(py_dealer_card)
        value: str = formatted_card[0]
        suit: str = formatted_card[1][randint(0, 1)]
        for _ in range(2): list_of_cards.append(Card(value, suit))

    shuffle(list_of_cards)
    for i in range(len(list_of_cards)): list_of_cards[i].hidden_value = i + 1
    return list_of_cards

def get_players_order(players: list[Player]) -> tuple[dict[Player, Card], list[Player]]:
    """
    Generates a random player order by using list of active players.
    Returns a tuple containing player order defined by a random card pull measure, using as keys the players and card assignment.
    """
    card_per_player: dict[Player, Card] = {}
    hand: Stack = _get_hand(len(players))

    for i in range(len(players)):
        reformatted_card: tuple[str, list[str]] = _get_reformatted_card(hand[i])
        card = Card(reformatted_card[0], reformatted_card[1][randint(0, 1)])
        card_per_player[players[i]] = card

    playing_order = sorted(card_per_player.items(), key=lambda item: int(_NUMBER_VALUE[item[1].value] if item[1].value in _EXTENDED_VALUE else item[1].value), reverse=True)
    return card_per_player, [player_card[0] for player_card in playing_order]

def _get_hand(number_of_different_cards: int) -> Stack:
    """
    Function generates a random set number of cards based on variable.
    Returns object of Stack type, representing a collection of cards.
    """
    deck = Deck()
    deck.shuffle()
    return deck.deal(number_of_different_cards)

def _get_reformatted_card(card: PyDealerCard) -> tuple[str, list[str]]:
    """
    Function performs reformation of cards for respective visual representations.
    Returns tuple containing card values and card suits assigned.
    """
    card_value: str = _SHORT_VALUE[card.value] if card.value in const.VALUES[9:] else card.value
    card_suit: list[str] = _SYMBOLS[card.suit]
    return card_value, card_suit