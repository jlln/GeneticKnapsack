import numpy as np
from src.KnapsackIndividual import Individual, KnapsackItem

from src.Evolution import breed_population,evolve_knapsack_population

np.random.seed(1234)
items = list(set([(np.random.randint(1, 30), np.random.randint(1, 30)) for x in range(500)]))
items = [KnapsackItem(x[0], x[1]) for x in items]
individuals = [Individual(items, max_weight=100) for x in range(50)]


evolve_knapsack_population(individuals,0.25,25,100,0.1)