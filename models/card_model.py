class Card:
    def __init__(self, value: str, suit: str) -> None:
        self._is_visible: bool = False
        self._hidden_value: int = 0
        self._value: str = value
        self._suit: str = suit

    @property
    def hidden_value(self) -> int: return self._hidden_value

    @hidden_value.setter
    def hidden_value(self, value: int) -> None: self._hidden_value = value

    @property
    def is_visible(self) -> bool: return self._is_visible

    @is_visible.setter
    def is_visible(self, value: bool) -> None: self._is_visible = value

    @property
    def value(self) -> str: return self._value

    @property
    def suit(self) -> str: return self._suit