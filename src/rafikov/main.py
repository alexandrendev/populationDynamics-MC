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

# pegar os intrvalos de novo e passar para os próximos dias
def execute():
    hosts = Host(3000, Type.HOST)
    infected = Infected(600, Type.INFECTED)
    parasitoid = Parasitoid(3000, Type.PARASITOID)

    params = Param(Equilibrium.FIRST)
    e = Equation(initialValues(hosts, infected, parasitoid)) 

    hostInterval = e.getFirstLineInterval(params)
    infectedInterval = e.getSecondLineInterval(params)
    parasitoidInterval = e.getThirdLineInterval(params)


    days = 10

    for _ in range(days):
        hosts.monteCarlo(hostInterval)
        hosts.initialPopulation = hosts.currentPopulation

        infected.monteCarlo(infectedInterval)
        infected.initialPopulation = infected.currentPopulation
        
        parasitoid.monteCarlo(parasitoidInterval)
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