import unittest
import numpy as np
from src.KnapsackIndividual import Individual
from src.KnapsackItem import Item


class TestIndividualMethods(unittest.TestCase):

    def setUp(self):
        self.items = list(set([(np.random.randint(1,30),np.random.randint(1,30)) for x in range(500)]))
        self.items = [Item(x[0], x[1]) for x in self.items]
        self.individuals = [Individual(self.items,max_weight=100) for x in range(50)]

    def test_fitness_scores(self):
        for i in self.individuals:
            self.assertIsInstance(i.fitness_score(),float)

    def test_mutation(self):
        mean_item_count = np.mean([len(x.items) for x in self.individuals])
        print(mean_item_count)
        for i in range(1000):
            for y in self.individuals:
                y.mutate(0.99)
        mean_item_count2 = np.mean([len(x.items) for x in self.individuals])
        change = np.abs(mean_item_count2 - mean_item_count)
        self.assertLess(change,0.5)


    def test_breed(self):
        i1 = self.individuals[7]
        i2 = self.individuals[9]
        i0 = i1.breed(i2)


