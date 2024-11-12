from enum import Enum
from Interval import *
import numpy as np

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
            
            
class Host(Individual):
    def __init__(self, initialPopulation: int, type: Type, currentPopulation=0):
        super().__init__(initialPopulation, type, currentPopulation)
        
        
    def monteCarlo(self, interval: list[Interval]):
        current = self.initialPopulation
        hostsInfected = 0
        for i in range(current):
            value = np.random.uniform(0, interval[-1].value)
            if len(interval) == 3 and value > interval[1].value: # last interval if it exists
                self.applyEffect(interval[2])
                hostsInfected += 1
            elif value <= interval[0].value: # 1st interval
                self.applyEffect(interval[0])
            elif value <= interval[1].value:
                self.applyEffect(interval[1]) # 2nd interval
            # print(individual.currentPopulation)
        self.initialPopulation = self.currentPopulation
        return hostsInfected
    
class Infected(Individual):
    def __init__(self, initialPopulation: int, type: Type, currentPopulation=0):
        super().__init__(initialPopulation, type, currentPopulation)
        
        
    def monteCarlo(self, interval: list[Interval]):
        current = self.initialPopulation
        hostsInfected = 0
        for i in range(current):
            value = np.random.uniform(0, interval[-1].value)
            if len(interval) == 3 and value > interval[1].value: # last interval if it exists
                self.applyEffect(interval[2])
                hostsInfected += 1
            elif value <= interval[0].value: # 1st interval
                self.applyEffect(interval[0])
            elif value <= interval[1].value:
                self.applyEffect(interval[1]) # 2nd interval
            # print(individual.currentPopulation)
        self.initialPopulation = self.currentPopulation
        return hostsInfected
    
class Parasitoid(Individual):
    def __init__(self, initialPopulation: int, type: Type, currentPopulation=0):
        super().__init__(initialPopulation, type, currentPopulation)
        
    def monteCarlo(self, interval: list[Interval]):
        current = self.initialPopulation
        hostsInfected = 0
        for i in range(current):
            value = np.random.uniform(0, interval[-1].value)
            if value <= interval[0].value: # 1st interval
                self.applyEffect(interval[0])
            elif value <= interval[1].value:
                self.applyEffect(interval[1]) # 2nd interval
            # print(individual.currentPopulation)
        self.initialPopulation = self.currentPopulation
        return hostsInfected