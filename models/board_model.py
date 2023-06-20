from card_model import Card

class Board:
    def __init__(self) -> None:
        self._difficulty: int = 0
        self._cards: list[Card] = []
        self._board: list[list[Card]] = [[]]

    @property
    def difficulty(self) -> int:
        return self._difficulty

    @difficulty.setter
    def difficulty(self, value) -> None:
        self._difficulty = value
        self._generate(value)

    def fill(self, pairs_of_cards: list[Card]) -> None:
        step: int = 0

        for row in self._board:
            for column in range(len(row)):
                row[column] = f"[ {pairs_of_cards[step]} ]"
                step += 1

    def display(self) -> None:
        for row in self._board: print('    '.join([card.value for card in row]))

    def _generate(self, difficulty: int) -> None:
        x: int = 0

        match difficulty:
            case 0: x = 4
            case 1: x = 8
            case 2: x = 13

        for i in range(0, 4): self._board.append([] * x)