import unittest
import numpy as np
from src.KnapsackIndividual import KnapsackIndividual,KnapsackItem

from src.FunctionOptimizerIndividual import FunctionMinimizer2DIndividual

class TestKnapsackIndividualMethods(unittest.TestCase):

    def setUp(self):
        self.items = list(set([(np.random.randint(1,30),np.random.randint(1,30)) for x in range(500)]))
        self.items = [KnapsackItem(x[0], x[1]) for x in self.items]
        self.individuals = [KnapsackIndividual(self.items,max_weight=100) for x in range(50)]

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
        self.assertNotEqual(mean_item_count,mean_item_count2)


    def test_breed(self):
        i1 = self.individuals[7]
        i2 = self.individuals[9]
        i0 = i1.breed(i2)



class TestNumericalIndividualMethods(unittest.TestCase):

    def setUp(self):
        def opt_func(x,y):
            return x ** 2 - 50 * x + y ** 2
        self.individuals = [FunctionMinimizer2DIndividual(opt_func,np.random.randint(-100,100),np.random.randint(-100,100)) for x in range(20)]

    def test_mutation(self):
        mean_value_x = np.mean([x.x for x in self.individuals])
        mean_value_y = np.mean([x.y for x in self.individuals])
        for i in range(1000):
            for ind in self.individuals:
                ind.mutate(0.99)
        mean_value_x_mut = np.mean([x.x for x in self.individuals])
        mean_value_y_mut = np.mean([x.y for x in self.individuals])
        self.assertNotEqual(mean_value_x,mean_value_x_mut)
        self.assertNotEqual(mean_value_y,mean_value_y_mut)


    def test_breed(self):
        i1 = self.individuals[7]
        i2 = self.individuals[9]
        i0 = i1.breed(i2)

