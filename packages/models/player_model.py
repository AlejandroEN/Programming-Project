class Player:
    def __init__(self, username: str) -> None:
        self._username: str = username
        self._score: int = 0

    @property
    def username(self) -> str: return self._username

    @property
    def score(self) -> int: return self._score

    @score.setter
    def score(self, value: int) -> None: self._score = value