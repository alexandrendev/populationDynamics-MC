from enum import Enum

class Equilibrium(Enum):
    FIRST = (1, 'First-Equilibrium')
    SECOND = (2, 'Second-Equilibrium')
    THIRD = (3, 'Third-Equilibrium')
    
    def __init__(self, value, description):
        self._value_ = value
        self.description = description

class Param:
    def __init__(self, equilibrium: Equilibrium):
        if equilibrium == Equilibrium.FIRST:
            self.n1 = 0.15
            self.r = 0.1
            self.beta = 4.147e-07
            self.m2 = 0.036
            self.n2 = 0.0625
            self.m3 = 0.5
            self.K = 25000
            self.gamma = 40
            self.equilibrium = equilibrium
        elif equilibrium == Equilibrium.SECOND:
            self.n1 = 0.02
            self.r = 0.025
            self.beta = 1.9700e-06
            self.m2 = 0.036
            self.n2 = 0.0625
            self.m3 = 0.5
            self.K = 25000
            self.gamma = 40
            self.equilibrium = equilibrium
        elif equilibrium == Equilibrium.THIRD:
            self.n1 = 0.02
            self.r = 0.25
            self.beta = 4.1105e-06
            self.m2 = 0.036
            self.n2 = 0.0625
            self.m3 = 0.5
            self.K = 25000
            self.gamma = 40
            self.equilibrium = equilibrium