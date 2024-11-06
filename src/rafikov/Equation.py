from Param import *
from Interval import *

class Equation:
    def __init__(self, initialValues: list[int]):
        self.initialValues = initialValues
        
        
from Param import *
from Interval import *

class Equation:
    def __init__(self, initialValues: list[int]):
        self.initialValues = initialValues
        
        
    def getFirstLineInterval(self, p: Param) -> list[float]:
        H, I, P = self.initialValues
        
        # firstLine = p.r * (1 - H / p.K) * H - p.n1 * H - p.beta * H * P
        
        firstTerm = p.r * (1 - H / p.K) * H
        secondTerm = p.n1 * H 
        thirdTerm = p.beta * H * P
        
        values = [
            (firstTerm, Effect.LIVE),
            (secondTerm, Effect.DIE),
            (thirdTerm, Effect.DIE)]
        
        sortedValues = sorted(values, key=lambda x: x[0])
        
        intervals = [
            Interval(sortedValues[0][0], Position.MIN, sortedValues[0][1]),
            Interval(sortedValues[1][0], Position.MID, sortedValues[1][1]),
            Interval(sortedValues[2][0], Position.MAX, sortedValues[2][1]),
        ]
        
        return intervals
    
    def getSecondLineInterval(self, p: Param) -> list[float]:
        H, I, P = self.initialValues
        # secondLine = p.beta * H *  - p.m2 * I - p.n2 * I
        firstTerm = p.beta * H * P
        secondTerm = p.m2 * I
        thirdTerm = p.n2 * I
        
        values = [
            (firstTerm, Effect.LIVE),
            (secondTerm, Effect.DIE),
            (thirdTerm, Effect.DIE)]
        
        sortedValues = sorted(values, key=lambda x: x[0])
        
        intervals = [
            Interval(sortedValues[0][0], Position.MIN, sortedValues[0][1]),
            Interval(sortedValues[1][0], Position.MID, sortedValues[1][1]),
            Interval(sortedValues[2][0], Position.MAX, sortedValues[2][1]),
        ]
        
        return intervals
    
    
    def getThirdLineInterval(self, p:Param) -> list[float]:
        H, I, P = self.initialValues
        # thirdLine = p.gamma * p.n2 * I - p.m3 * P
        
        firstTerm = p.gamma * p.n2 * I
        secondTerm = p.m3 * P
        
        values = [
            (firstTerm, Effect.LIVE),
            (secondTerm, Effect.DIE),
        ]
        
        sortedValues = sorted(values, key=lambda x: x[0])
        
        intervals = [
            Interval(sortedValues[0][0], Position.MIN, sortedValues[0][1]),
            Interval(sortedValues[1][0], Position.MAX, sortedValues[1][1]),
        ]
        
        return intervals