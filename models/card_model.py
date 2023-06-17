class Card:
    def __init__(self, value: str, suit: str) -> None:
        """Initializes the card's value and suit."""

        self._is_hidden: bool = False
        self._hidden_value: int = 0
        self._value: str = value
        self._suit: str = suit

    @property
    def hidden_value(self) -> int:
        """Returns the hidden value of the card."""

        return self._hidden_value

    @property
    def is_hidden(self) -> bool:
        """Returns the state of the card."""

        return self._is_hidden