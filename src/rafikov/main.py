from Param import *
from Interval import *
from random import random
from Equation import Equation

# dHdt = r * (1 - H / K) * H - n1 * H - beta * H * P
# dIdt = beta * H * P - m2 * I - n2 * I
# dPdt = gamma * n2 * I - m3 * P




'''
-----------------------------------------------------------------------
'''
Hosts = 3000
Infected = 600
Parasitoid = 3000
initialValues = [Hosts, Infected, Parasitoid]

p = Param(Equilibrium.FIRST)
e = Equation(initialValues)

HostInterval = e.getFirstLineInterval(p)
InfectedInterval = e.getSecondLineInterval(p)
ParasitoidInterval = e.getThirdLineInterval(p)

minimo = list(filter(lambda x: x.position == Position.MIN, HostInterval))
maximo = list(filter(lambda x: x.position == Position.MAX, HostInterval))

print(maximo)
print(minimo)
# print(ParasitoidInterval[1])