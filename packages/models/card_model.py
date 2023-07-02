class Card:
    """
    Represents a card.
    """
    def __init__(self, value: str, suit: str) -> None:
        """
        Initializes a new instance of the Card class.
        """
        self._is_visible: bool = False
        self._hidden_value: int = 0
        self._value: str = value
        self._suit: str = suit

    @property
    def hidden_value(self) -> int:
        """
        Gets the hidden value of the card.
        """
        return self._hidden_value

    @hidden_value.setter
    def hidden_value(self, value: int) -> None:
        """
        Sets the hidden value of the card.
        """
        self._hidden_value = value

    @property
    def is_visible(self) -> bool:
        """
        Gets the visibility of the card.
        """
        return self._is_visible

    @is_visible.setter
    def is_visible(self, value: bool) -> None:
        """
        Sets the visibility of the card.
        """
        self._is_visible = value

    @property
    def value(self) -> str:
        """
        Gets the value of the card.
        """
        return self._value

    @property
    def suit(self) -> str:
        """
        Gets the suit of the card.
        """
        return self._suit