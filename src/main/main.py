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
import time
    
load_dotenv()
EQUILIBRIUM = os.getenv('EQUILIBRIUM')
DAYS = int(os.getenv('DAYS'))
SIMULATIONS = int(os.getenv('SIMULATIONS'))
# dHdt = r * (1 - H / K) * H - n1 * H - beta * H * P
# dIdt = beta * H * P - m2 * I - n2 * I
# dPdt = gamma * n2 * I - m3 * P

daysList = []

'''==============================================='''
def initialValues(hosts, infected, parasitoid): 
    return [
        hosts,
        infected,
        parasitoid
    ]

'''==============================================='''
def initializeEquilibrium(host: int, infected: int, parasitoid: int):
    hosts = Host(host)
    infected = Infected(infected)
    parasitoid = Parasitoid(parasitoid)
    params = Param(Equilibrium[EQUILIBRIUM])
    e = Equation(initialValues(
        hosts.currentPopulation,
        infected.currentPopulation,
        parasitoid.currentPopulation
    ))
    return hosts, infected, parasitoid, params, e

'''==============================================='''
def simulateDay(day, hosts, infected, parasitoid, params, e):
    hosts.monteCarlo(e.getFirstLineInterval(params))
    infected.monteCarlo(e.getSecondLineInterval(params))
    parasitoid.monteCarlo(e.getThirdLineInterval(params))
    e = Equation(initialValues(
        hosts.currentPopulation,
        infected.currentPopulation,
        parasitoid.currentPopulation
    ))
    daysList.append(Day(day+1, hosts.currentPopulation, infected.currentPopulation, parasitoid.currentPopulation))
    return hosts, infected, parasitoid, params, e

'''==============================================='''
def execute(equilibrium: Equilibrium, days = DAYS):
    hosts, infected, parasitoid, params, e = initializeEquilibrium(3000, 600, 3000)    


    dataHosts = [hosts.currentPopulation]
    dataInfected = [infected.currentPopulation]
    dataParasitoid = [parasitoid.currentPopulation]
    dataDays = []
    
    for day in range(DAYS):
        # print(f'Executando dia {day + 1} \t Início: {time.ctime()}')
        dataDays.append(day)
        hosts, infected, parasitoid, params, e = simulateDay(day, hosts, infected, parasitoid, params, e)

        dataHosts.append(hosts.currentPopulation)
        dataInfected.append(infected.currentPopulation)
        dataParasitoid.append(parasitoid.currentPopulation)
        
        '''==============================================='''
    params = [
        Parameter(dataHosts, "Hosts"),
        Parameter(dataInfected, "Infected"),
        Parameter(dataParasitoid, "Parasitoid")
    ]

    # paramDay = Parameter(dataDays, "Days")
    # name = f'graphs/rafikov{equilibrium.name.lower()}.png' 
    # plot(paramDay, params, name)
    

''' ===============================================
        CHAMADA DE @X SIMULAÇÕES PASSANDO O DEVIDO
        EQUILIBRIO COM O VALOR DA VARIÁVEL DE AMBIENTE
    ==============================================='''
for _ in range(SIMULATIONS):
    print(f'Simulação {_+1} \t Time: {time.ctime()}')
    execute(Equilibrium[EQUILIBRIUM])

medias = {}

''' ===============================================
        CÁLCULO DOS VALORES MÉDIOS PARA CADA DIA DA
        SIMULAÇÃO
    ==============================================='''
for i in range(DAYS + 1):
    dia = list(filter(lambda x: x.day == i, daysList))
    
    if dia:
        hosts_values = [d.hosts for d in dia]
        infected_values = [d.infected for d in dia]
        parasitoid_values = [d.parasitoids for d in dia]
        
        meanHosts = sum(hosts_values) / len(hosts_values)
        meanInfected = sum(infected_values) / len(infected_values)
        meanParasitoid = sum(parasitoid_values) / len(parasitoid_values)
        
        medias[i] = [meanHosts, meanInfected, meanParasitoid]
    else:
        print(f"Nenhum dado para o dia {i + 1}")


'''==============================================='''
mediaHosts = [medias[day][0] for day in range(1, DAYS)]
mediaInfected = [medias[day][1] for day in range(1, DAYS)]
mediaParasitoid = [medias[day][2] for day in range(1, DAYS)]

paramDay = Parameter(list(range(1, DAYS + 1)), "Days")

params = [
    Parameter(mediaHosts, "Hosts (Média)"),
    Parameter(mediaInfected, "Infected (Média)"),
    Parameter(mediaParasitoid, "Parasitoid (Média)")
]

name = f'graphs/medias_populacao-{EQUILIBRIUM}.png'

'''==============================================='''
plot(paramDay, params, name)