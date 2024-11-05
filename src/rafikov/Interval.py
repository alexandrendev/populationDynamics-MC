from enum import Enum

class Position(Enum):
    MAX = (1, "max")
    MID = (2, "mid")
    MIN = (3, "min")

class Effect(Enum):
    LIVE = (1, "+1")
    DIE = (2, "-1")

class Interval:
    def __init__(self, value: float, position: Position, effect: Effect):
        self.value = value
        self.position = position
        self.effect = effect
        
    def __str__(self) -> str:
        return f'{self.value} {self.effect}'