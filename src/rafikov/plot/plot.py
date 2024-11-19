import matplotlib.pyplot as plt
from plot.Parameter import Parameter

def plot(days: list[Parameter], params: list[Parameter], name: str): 
        plt.figure(figsize=(10, 6))
        
        for param in params:
            plt.plot(param.values, label = param.label)
            
        plt.title("Population Dynamics")
        plt.xlabel("Days")
        plt.ylabel("Population")
        plt.legend()
        plt.grid()
        plt.savefig(name)
        plt.close()
