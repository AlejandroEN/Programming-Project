class Card:
    def __init__(self, value: str, suit: str) -> None:
        self._is_hidden: bool = False
        self._hidden_value: int = 0
        self._value: str = value
        self._suit: str = suit
        self._is_matched: bool = False

    @property
    def hidden_value(self) -> int: return self._hidden_value

    @hidden_value.setter
    def hidden_value(self, value: int) -> None: self._hidden_value = value

    @property
    def is_hidden(self) -> bool: return self._is_hidden

    @property
    def value(self) -> str: return self._value

    @property
    def suit(self) -> str: return self._suit

    @property
    def is_matched(self) -> bool: return self._is_matched

    @is_matched.setter
    def is_matched(self, value: bool) -> None: self._is_matched = value