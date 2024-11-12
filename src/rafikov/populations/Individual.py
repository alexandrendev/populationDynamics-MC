from enum import Enum
from Interval import *
import numpy as np
    
class Individual:
    def __init__(self, initialPopulation: int):
        self.initialPopulation = initialPopulation
        self.currentPopulation = initialPopulation

    def updateCurrentPopulation(self, newValue: int):
        self.currentPopulation = newValue

    def applyEffect(self, interval: Interval):
        if interval.effect == Effect.DIE:
            self.currentPopulation -= 1
        elif interval.effect == Effect.LIVE:
            self.currentPopulation += 1
            
            
class Host(Individual):
    def __init__(self, initialPopulation: int):
        super().__init__(initialPopulation)
        
        
    def monteCarlo(self, interval: list[Interval]):
        hostsInfected = 0
        for i in range(self.currentPopulation):
            value = np.random.uniform(interval[0].value, interval[-1].value)
            if value > 0 and value < interval[0].value:
                self.applyEffect(interval[0])
            elif value <= interval[1].value: # 1st interval
                self.applyEffect(interval[1])
            elif value <= interval[2].value:
                self.applyEffect(interval[1]) # 2nd interval
                hostsInfected += 1
            # print(individual.currentPopulation)
        return hostsInfected
    
class Infected(Individual):
    def __init__(self, initialPopulation: int):
        super().__init__(initialPopulation)
        
        
    def monteCarlo(self, interval: list[Interval]):
        hostsInfected = 0
        for i in range(self.currentPopulation):
            value = np.random.uniform(interval[0].value, interval[-1].value)
            if value > 0 and value <= interval[0].value: # last interval if it exists
                self.applyEffect(interval[2])
                hostsInfected += 1
            elif value <= interval[1].value: # 1st interval
                self.applyEffect(interval[0])
            elif value <= interval[2].value:
                self.applyEffect(interval[1]) # 2nd interval
            # print(individual.currentPopulation)
        return hostsInfected
    
class Parasitoid(Individual):
    def __init__(self, initialPopulation: int):
        super().__init__(initialPopulation)
        
    def monteCarlo(self, interval: list[Interval]):
        hostsInfected = 0
        for i in range(self.currentPopulation):
            value = np.random.uniform(interval[0].value, interval[-1].value)
            if value <= interval[0].value: # 1st interval
                self.applyEffect(interval[0])
            elif value <= interval[1].value:
                self.applyEffect(interval[1]) # 2nd interval
            # print(individual.currentPopulation)
        return hostsInfected