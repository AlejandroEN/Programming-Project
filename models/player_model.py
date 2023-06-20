class Player:
    def __init__(self, username) -> None:
        self._username: str = username
        self._score: int = -1

    @property
    def username(self) -> str:
        return self._username