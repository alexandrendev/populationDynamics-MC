from Param import *
from Interval import *
from Equation import Equation
from populations.Individual import *
import numpy as np
from plot.Parameter import Parameter
from plot.plot import plot
from populations.Day import Day
from dotenv import load_dotenv
import os


output_dir = '/app/graphs'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    
load_dotenv()
eq = os.getenv('EQUILIBRIUM')
# dHdt = r * (1 - H / K) * H - n1 * H - beta * H * P
# dIdt = beta * H * P - m2 * I - n2 * I
# dPdt = gamma * n2 * I - m3 * P

daysList = []

def initialValues(hosts, infected, parasitoid): 
    return [
        hosts,
        infected,
        parasitoid
    ]

def execute(equilibrium: Equilibrium, days = 500):

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

    dataHosts = [
        hosts.currentPopulation
    ]
    dataInfected = [
        infected.currentPopulation
    ]
    dataParasitoid= [
        parasitoid.currentPopulation
    ]
    dataDays = []
    
    for day in range(days):
        dataDays.append(day)
        hosts.monteCarlo(hostInterval)
        
        infected.monteCarlo(infectedInterval)
        
        parasitoid.monteCarlo(parasitoidInterval)

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

        daysList.append(Day(day+1, hosts.currentPopulation, infected.currentPopulation, parasitoid.currentPopulation))
        
        '''==============================================='''
    params = [
        Parameter(dataHosts, "Hosts"),
        Parameter(dataInfected, "Infected"),
        Parameter(dataParasitoid, "Parasitoid")
    ]
    
    paramDay = Parameter(dataDays, "Days")
    name = f'graphs/rafikov{equilibrium.name.lower()}.png' 
    plot(paramDay, params, name)
    
    # print(hosts.currentPopulation)
    # print(infected.currentPopulation)
    # print(parasitoid.currentPopulation)
    


for _ in range(500):
    execute(Equilibrium[eq])

medias = {}

for i in range(500):
    dia = list(filter(lambda x: x.day == i + 1, daysList))
    
    if dia:
        hosts_values = [d.hosts for d in dia]
        infected_values = [d.infected for d in dia]
        parasitoid_values = [d.parasitoids for d in dia]
        
        meanHosts = sum(hosts_values) / len(hosts_values)
        meanInfected = sum(infected_values) / len(infected_values)
        meanParasitoid = sum(parasitoid_values) / len(parasitoid_values)
        
        medias[i + 1] = [meanHosts, meanInfected, meanParasitoid]
    else:
        print(f"Nenhum dado para o dia {i + 1}")
        
mediaHosts = [medias[day][0] for day in range(1, 251)]
mediaInfected = [medias[day][1] for day in range(1, 251)]
mediaParasitoid = [medias[day][2] for day in range(1, 251)]


paramDay = Parameter(list(range(1, 251)), "Days")

params = [
    Parameter(mediaHosts, "Hosts (Média)"),
    Parameter(mediaInfected, "Infected (Média)"),
    Parameter(mediaParasitoid, "Parasitoid (Média)")
]

name = f'graphs/medias_populacao-{eq}.png'

plot(paramDay, params, name)


# print(daysList[0].day)
    # execute(Equilibrium.SECOND)
    # execute(Equilibrium.THIRD)
