class Day:
    
    def __init__(self, day: int, hosts: int, infected: int, parasitoids: int):
        self.day = day
        self.hosts = hosts
        self.infected = infected
        self.parasitoids = parasitoids
    
    def __str__(self):
        return f"{self.day},{self.hosts},{self.infected},{self.parasitoids}"