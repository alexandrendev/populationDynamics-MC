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
    hosts = Host(3000)
    infected = Infected(600)
    parasitoid = Parasitoid(3000)

    params = Param(Equilibrium.FIRST)
    e = Equation(initialValues(hosts, infected, parasitoid)) 

    hostInterval = e.getFirstLineInterval(params)
    infectedInterval = e.getSecondLineInterval(params)
    parasitoidInterval = e.getThirdLineInterval(params)


    days = 20

    for _ in range(days):
        
        infectedHosts = hosts.monteCarlo(hostInterval)
        
        infected.monteCarlo(infectedInterval)
        
        parasitoid.monteCarlo(parasitoidInterval)
        
        infected.updateCurrentPopulation(infected.currentPopulation + infectedHosts)

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