from Param import *
from Interval import *
from Equation import Equation
from populations.Individual import *
import numpy as np
from plot.Parameter import Parameter
from plot.plot import plot

# dHdt = r * (1 - H / K) * H - n1 * H - beta * H * P
# dIdt = beta * H * P - m2 * I - n2 * I
# dPdt = gamma * n2 * I - m3 * P

def initialValues(hosts, infected, parasitoid): 
    return [
        hosts,
        infected,
        parasitoid
    ]

def execute(equilibrium: Equilibrium):

    '''
    --------------------
    INITIAL POPULATIONS
    --------------------
    '''
    hosts = Host(3000)
    infected = Infected(600)
    parasitoid = Parasitoid(3000)

    params = Param(equilibrium)
    e = Equation(initialValues(
        hosts.currentPopulation,
        infected.currentPopulation,
        parasitoid.currentPopulation
    )) 

    hostInterval = e.getFirstLineInterval(params)
    infectedInterval = e.getSecondLineInterval(params)
    parasitoidInterval = e.getThirdLineInterval(params)


    days = 250
    dataHosts = []
    dataInfected = []
    dataParasitoid= []
    dataDays = []
    for day in range(days):

        dataDays.append(day)
        infectedHosts = hosts.monteCarlo(hostInterval)
        
        deadInfected = infected.monteCarlo(infectedInterval)
        
        parasitoid.monteCarlo(parasitoidInterval)
        
        infected.updateCurrentPopulation(infected.currentPopulation + infectedHosts)
        parasitoid.updateCurrentPopulation(parasitoid.currentPopulation - deadInfected)

        e = Equation(initialValues(
            hosts.currentPopulation,
            infected.currentPopulation,
            parasitoid.currentPopulation
        ))

        hostInterval = e.getFirstLineInterval(params)
        infectedInterval = e.getSecondLineInterval(params)
        parasitoidInterval = e.getThirdLineInterval(params)
        
        dataHosts.append(hosts.currentPopulation)
        dataInfected.append(infected.currentPopulation)
        dataParasitoid.append(parasitoid.currentPopulation)

    params = [
        Parameter(dataHosts, "Hosts"),
        Parameter(dataInfected, "Infected"),
        Parameter(dataParasitoid, "Parasitoid")
    ]
    
    paramDay = Parameter(dataDays, "Days")
    name = f'graphs/rafikov{equilibrium.name.lower()}.png' 
    plot(paramDay, params, name)
    print(hosts.currentPopulation)
    print(infected.currentPopulation)
    print(parasitoid.currentPopulation)

execute(Equilibrium.FIRST)