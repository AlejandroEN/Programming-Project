class Player:
    """
    Represents a player.
    """
    def __init__(self, username: str) -> None:
        """
        Initializes a new instance of the Player class.
        """
        self._username: str = username
        self._score: int = 0

    @property
    def username(self) -> str:
        """
        Gets the username of the player.
        """
        return self._username

    @property
    def score(self) -> int:
        """
        Gets the score of the player.
        """
        return self._score

    @score.setter
    def score(self, value: int) -> None:
        """
        Sets the score of the player.
        """
        self._score = value