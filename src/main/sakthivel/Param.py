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
            self.m1 = 0.03566
            self.m2 = 0.03566
            self.m3 = 0.00256
            self.n1 = 0.1
            self.n2 = 0.10000
            self.n3 = 0.02439
            self.K = 25000
            self.beta = 0.11566
            self.alpha = 0.0001723
            self.equilibrium = equilibrium
        elif equilibrium == Equilibrium.SECOND:
            self.m1 = 0.03566
            self.m2 = 0.03566
            self.m3 = 0.00256
            self.n1 = 0.1
            self.n2 = 0.10000
            self.n3 = 0.02439
            self.K = 25000
            self.beta = 0.139
            self.alpha = 0.0001723
            self.equilibrium = equilibrium
        elif equilibrium == Equilibrium.THIRD:
            self.m1 = 0.03566
            self.m2 = 0.03566
            self.m3 = 0.00256
            self.n1 = 0.1
            self.n2 = 0.10000
            self.n3 = 0.02439
            self.K = 25000
            self.beta = 0.1908
            self.alpha = 0.0001723
            self.equilibrium = equilibrium