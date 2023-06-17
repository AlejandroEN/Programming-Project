from card_model import Card
from card import get_pairs_of_cards

class Board:
    def __init__(self, difficulty: int) -> None:
        self._difficulty: int = difficulty
        self._cards: list[Card] = []
        self._board: list[list[Card]] = [[]]

    def _generate(self, difficulty: int) -> None:
        """Set board dimensions "x" x "y", display in strings for simple assimilation.
        'x' represents amount of columns, and 'y' represents amount of rows"""

        x: int = 0

        match difficulty:
            case 0: x = 4
            case 1: x = 8
            case 2: x = 13

        for i in range(0, 4):
            self._board.append(['[]'] * x)

    def _fill(self) -> None:
        """Assigns respective keys to each individual element on board list.
            Does not include card 'values' (values = symbolic and numerical cards)."""

        step: int = 0

        for row in self._board:
            for column in range(len(row)):
                row[column] = f"[ {card_pair[step]} ]"
                step += 1