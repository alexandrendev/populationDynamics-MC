from Param import *
from Interval import *

p = Param(Equilibrium.FIRST)
def getHostIntervals(initialValues: list[int]) -> list[float]:
    H, I, P = initialValues

    first = p.r * (1 - H / p.K) * H
    second = p.n1 * H 
    third = p.beta * H * P
    
    values = [
        (first, Effect.LIVE),
        (second, Effect.DIE),
        (third, Effect.DIE)]
    
    sortedValues = sorted(values, key=lambda x: x[0])
    
    intervals = [
        Interval(sortedValues[0][0], Position.MIN, sortedValues[0][1]),
        Interval(sortedValues[1][0], Position.MID, sortedValues[1][1]),
        Interval(sortedValues[2][0], Position.MAX, sortedValues[2][1]),
    ]
    
    return intervals


Hosts = 3000
Infected = 600
Parasitoid = 3000

initialValues = [Hosts, Infected, Parasitoid]
intervals = getHostIntervals(initialValues)





