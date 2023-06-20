class Card:
    def __init__(self, value: str, suit: str) -> None:
        self._is_hidden: bool = False
        self._hidden_value: int = 0
        self._value: str = value
        self._suit: str = suit

    @property
    def hidden_value(self) -> int:
        return self._hidden_value

    @property
    def is_hidden(self) -> bool:
        return self._is_hidden

    @property
    def value(self) -> str:
        return self._value

    @property
    def suit(self) -> str:
        return self._suit