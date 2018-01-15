import numpy as np
from src.Evolution import Individual

class FunctionMinimizer2DIndividual(Individual):
    def __init__(self,function,x,y):
        self.x = x
        self.y = y
        self.function = function
        self.z = function(x,y)

    def is_legal(self):
        return True
    def fitness_score(self):
        return np.max([0,1 - self.z])

    def mutate(self,prob):
        cutoff = np.random.random()
        if prob < cutoff:
            choice = np.random.randn()
            if choice < 0:
                self.x = (np.random.randn() +1) * self.x
            else:
                self.y = (np.random.randn() + 1) * self.y
        self.z = self.function(self.x, self.y)

    def breed(self,partner):
        if partner.x == self.x:
            x = self.x * (np.random.randn() + 1)
        else:
            xes = sorted([self.x,partner.x])
            x = np.random.uniform(xes[0] ,xes[1])
        if partner.y == self.y:
            y = self.y * (np.random.randn() + 1)
        else:
            yes = sorted([self.y, partner.y])
            y = np.random.uniform(yes[0],yes[1])
        offspring = FunctionMinimizer2DIndividual(self.function,x,y)
        offspring.mutate(0.1)
        return offspring

    def report(self):
        return ";".join([str(self.x), str(self.y),str(self.z)])