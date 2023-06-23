from card_model import Card

class Board:
    def __init__(self) -> None:
        self._difficulty: int = 0
        self._cards: list[Card] = []
        self._board: list[list[Card]] = [[] for _ in range(4)]
        self._cards_per_row: int = 0

    @property
    def cards(self) -> list[Card]: return self._cards

    @property
    def difficulty(self) -> int: return self._difficulty

    @difficulty.setter
    def difficulty(self, value) -> None:
        self._difficulty = value

        match self._difficulty - 1:
            case 0: self._cards_per_row = 4
            case 1: self._cards_per_row = 8
            case 2: self._cards_per_row = 13

    def fill(self, pairs_of_cards: list[Card]) -> None:
        self._cards = pairs_of_cards
        step: int = 0

        for i in range(4):
            self._board[i] = pairs_of_cards[step:step + self._cards_per_row]
            step += self._cards_per_row

    def display(self) -> None:
        for row in self._board:
            displayed_values: list[str] = []

            for card in row:
                if not card.is_matched:
                    displayed_values.append(f"[  {card.hidden_value} ]" if len(str(card.hidden_value)) == 1 else f"[ {card.hidden_value} ]")
                else:
                    displayed_values.append(f"{card.value} {card.suit} " if len(card.value) == 1 else f"{card.value} {card.suit}")

            print('    '.join(displayed_values))