from enum import Enum
from Interval import *

class Type(Enum):
    HOST = 1
    INFECTED = 2
    PARASITOID = 3
    
class Individual:
    def __init__(self, initialPopulation: int, type: Type, currentPopulation = 0):
        self.initialPopulation = initialPopulation
        self.currentPopulation = initialPopulation
        self.type = type

    def updateCurrentPopulation(self, newValue: int):
        self.currentPopulation = newValue

    def applyEffect(self, interval: Interval):
        if interval.effect == Effect.DIE:
            self.currentPopulation -= 1
        elif interval.effect == Effect.LIVE:
            self.currentPopulation += 1