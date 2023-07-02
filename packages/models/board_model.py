from .card_model import Card

class Board:
    """
    Represents a board.
    """
    def __init__(self) -> None:
        """
        Initializes a new instance of the Board class.
        """
        self._difficulty: int = 0
        self._cards: list[Card] = []
        self._board: list[list[Card]] = [[] for _ in range(4)]
        self._cards_per_row: int = 0

    @property
    def cards(self) -> list[Card]:
        """
        Gets the cards of the board.
        """
        return self._cards

    @property
    def difficulty(self) -> int:
        """
        Gets the difficulty of the board.
        """
        return self._difficulty

    @difficulty.setter
    def difficulty(self, value: int) -> None:
        """
        Sets the difficulty of the board.
        """
        self._difficulty = value

        match self._difficulty:
            case 0: self._cards_per_row = 4
            case 1: self._cards_per_row = 8
            case 2: self._cards_per_row = 13
            case _: pass

    def fill(self, pairs_of_cards: list[Card]) -> None:
        """
        Fills the board with pairs of cards.
        """
        self._cards = pairs_of_cards
        step: int = 0

        for i in range(4):
            self._board[i] = pairs_of_cards[step:step + self._cards_per_row]
            step += self._cards_per_row

    def display(self) -> None:
        """
        Displays the board.
        """
        for row in self._board:
            displayed_values: list[str] = []

            for card in row:
                if not card.is_visible:
                    displayed_values.append(f"[  {card.hidden_value} ]" if len(str(card.hidden_value)) == 1 else f"[ {card.hidden_value} ]")
                else:
                    displayed_values.append(f"{card.value} {card.suit} " if len(card.value) == 1 else f"{card.value} {card.suit}")

            print('    '.join(displayed_values))