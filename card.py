from pydealer import Deck

symbols = {"Diamonds": ["♦", "♢"], "Clubs": ["♣", "♧"], "Hearts": ["♥", "♡"], "Spades": ["♠", "♤"]}


def get_cards(number_of_different_cards: int):
    deck: Deck = Deck()
    deck.shuffle()
    hand = deck.deal(number_of_different_cards)
    list_of_cards = []

    for card in hand:
        new_card = f"{card.value} {symbols[card.suit][0]}"
        print(new_card)


get_cards(20)