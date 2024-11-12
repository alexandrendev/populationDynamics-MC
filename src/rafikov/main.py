from Param import *
from Interval import *
from Equation import Equation
from populations.Individual import *
import numpy as np

# dHdt = r * (1 - H / K) * H - n1 * H - beta * H * P
# dIdt = beta * H * P - m2 * I - n2 * I
# dPdt = gamma * n2 * I - m3 * P

def initialValues(hosts: Individual, infected: Individual, parasitoid: Individual) -> list[int]:
    return [
        hosts.currentPopulation,
        infected.currentPopulation,
        parasitoid.currentPopulation
    ]

def monteCarlo(interval: list[Interval], individual: Individual):
    current = individual.initialPopulation
    
    for i in range(current):
        value = np.random.uniform(0, interval[-1].value)

        if len(interval) == 3 and value > interval[1].value:
            individual.applyEffect(interval[2])
        elif value <= interval[0].value:
            individual.applyEffect(interval[0])
        elif value <= interval[1].value:
            individual.applyEffect(interval[1])
        # print(individual.currentPopulation)
        individual.initialPopulation = individual.currentPopulation


# pegar os intrvalos de novo e passar para os próximos dias
def execute():
    hosts = Individual(3000, Type.HOST)
    infected = Individual(600, Type.INFECTED)
    parasitoid = Individual(3000, Type.PARASITOID)

    params = Param(Equilibrium.FIRST)
    e = Equation(initialValues(hosts, infected, parasitoid)) 

    hostInterval = e.getFirstLineInterval(params)
    infectedInterval = e.getSecondLineInterval(params)
    parasitoidInterval = e.getThirdLineInterval(params)


    days = 10

    for _ in range(days):
        monteCarlo(hostInterval, hosts)
        hosts.initialPopulation = hosts.currentPopulation

        monteCarlo(infectedInterval, infected)
        infected.initialPopulation = infected.currentPopulation
        
        monteCarlo(parasitoidInterval, parasitoid)
        parasitoid.initialPopulation = parasitoid.currentPopulation

        e = Equation(initialValues(
            hosts,
            infected,
            parasitoid
        ))

        hostInterval = e.getFirstLineInterval(params)
        infectedInterval = e.getSecondLineInterval(params)
        parasitoidInterval = e.getThirdLineInterval(params)
    
    print(hosts.currentPopulation)
    print(infected.currentPopulation)
    print(parasitoid.currentPopulation)

execute()