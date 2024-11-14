from Param import *
from Interval import *

class Equation:
    def __init__(self, initialValues: list[int]):
        self.initialValues = initialValues
        
        
    def getFirstLineInterval(self, p: Param):
        H, I, P = self.initialValues
        
        # firstLine = p.r * (1 - H / p.K) * H - p.n1 * H - p.beta * H * P
        
        firstTerm = p.r * (1 - H / p.K) * H
        secondTerm = p.n1 * H 
        thirdTerm = p.beta * H * P
        
        values = [
            Interval(firstTerm, Effect.LIVE),
            Interval(firstTerm + secondTerm, Effect.DIE),
            Interval(firstTerm + secondTerm + thirdTerm, Effect.DIE)]
        
        return values        
    
    def getSecondLineInterval(self, p: Param):
        H, I, P = self.initialValues
        # secondLine = p.beta * H *  - p.m2 * I - p.n2 * I
        firstTerm = p.beta * H * P
        secondTerm = p.m2 * I
        thirdTerm = p.n2 * I
        
        values = [
            Interval(firstTerm, Effect.LIVE),
            Interval(firstTerm + secondTerm, Effect.DIE),
            Interval(firstTerm + secondTerm + thirdTerm, Effect.DIE)]
    
        return values
    
    
    def getThirdLineInterval(self, p:Param):
        H, I, P = self.initialValues
        # thirdLine = p.gamma * p.n2 * I - p.m3 * P
        
        firstTerm = p.gamma * p.n2 * I
        secondTerm = p.m3 * P
        
        values = [
            Interval(firstTerm, Effect.LIVE),
            Interval(firstTerm + secondTerm, Effect.DIE),
        ]
        
        return values