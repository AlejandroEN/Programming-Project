class Player:
    def __init__(self, name, score) -> None:
        self.name: str = name
        self.score: int = score
        self.order: int = 0

    @property
    def playin_order(self) -> int:
        return self.order