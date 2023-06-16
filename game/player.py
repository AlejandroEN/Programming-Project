from card import get_hand, NUMBER_VALUE, const, get_reformatted_card
from pydealer import Stack

def get_players_order(players: list[str]) -> tuple[dict, list[tuple]]:
    """Generates and handles a frame of a random set of cards, uses them to determine player order, based on the list 'players'
        Returns player order as a fixed list of the 'players' list.
        Contents classified as tuples."""

    players_card_dictionary: dict = {}
    hand: Stack = get_hand(len(players))

    for i in range(len(players)): players_card_dictionary[players[i]] = hand[i]
    playing_order: list[tuple] = sorted(players_card_dictionary.items(), key=lambda item: int(NUMBER_VALUE[item[1].value] if item[1].value in const.VALUES[9:] else item[1].value), reverse=True)

    return players_card_dictionary, playing_order