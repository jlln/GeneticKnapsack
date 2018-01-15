import numpy as np

class Mating:
    '''
    Convenience class to hold mating records
    '''
    def __init__(self,parent_a,parent_b,children,generation):
        self.generation = generation
        self.parent_a = parent_a
        self.parent_b = parent_b
        self.children = children


class Individual:
    def is_legal(self):
        #Boolean indicating if the individual fits the problem constraints
        pass
    def fitness_score(self):
        #Float value defining the fitness of the individual within the problem constraints. Higher is better
        pass
    def mutate(self):
        #Modifies the individual in-place. Randomly alters the individuals properties.
        pass
    def breed(self,other):
        #Returns a single offspring with traits inherited from both this object and the other object.
        pass
    def report(self):
        #Returns a string describing the individual
        pass

def breed_population(population,mating_rate,litter_size,mutation_prob,generation):
    '''
    Function implementing genetic algorithm. Operates on collections of objects subclassed from the Individual class.
    :param population: A collection of individuals
    :param mating_rate: The frequency at which individuals mate.
    :param litter_size: The number of offspring produced by each mating
    :param mutation_prob: The probability of an offspring acquiring a mutation.
    :param generation: The number of generations since the experiment began
    :return:
    '''
    children = []
    matings = []
    total_fitness = np.sum([x.fitness_score() for x in population])
    probabilities = [x.fitness_score()/total_fitness for x in population]
    for i in range(int(np.round(len(population) * mating_rate))):
        partner_a = np.random.choice(population,size=1,p=probabilities)[0]
        partner_b = np.random.choice(population,size=1,p=probabilities)[0]
        for c in range(litter_size):
            child=(partner_a.breed(partner_b))
            child.mutate(mutation_prob)
            children.append(child)
        matings.append(Mating(partner_a,partner_b,children,generation))
    pop_size = len(population)
    combined_population = population + children
    combined_population = [x for x in combined_population if x.is_legal()]
    combined_population = sorted(combined_population,key = lambda x: x.fitness_score(),reverse=True)
    return combined_population[:pop_size],matings

def evolve_knapsack_population(population,mating_rate,litter_size,step,mutation_prob):
    '''
    Wrapper function on breed_population to solve the 0-1 Knapsack Problem
    :param population:
    :param mating_rate:
    :param litter_size:
    :param step:
    :param mutation_prob:
    :return:
    '''
    generations = []
    population_record = [population]
    mean_values = []
    weights = []
    values = []
    fitness_scores = []
    mean_fitness_scores = []
    best_of_generations = []
    matings = []
    with open("output_ga.txt",'w') as outfile:
        for generation in range(step):
            legal_population = [x for x in population if x.is_legal()]
            print("Generation {}".format(generation))
            print( "{}% Population Legal".format(len(legal_population)/len(population) * 100))
            print("Mean Fitness: {}".format(np.mean([x.fitness_score() for x in population])))
            print("Best Value: {}".format(np.max([x.total_value() for x in legal_population])))
            most_fit = sorted(population,key=lambda x: x.fitness_score())[-1]
            print("Most Fit:")
            print("   value: {} weight: {} fitness: {}".format(most_fit.total_value(),most_fit.total_weight(),most_fit.fitness_score()))
            population,mating_set = breed_population(population,mating_rate = mating_rate,litter_size=litter_size,mutation_prob=mutation_prob,generation=generation)
            matings.append(mating_set)
            population_record.append(population)
            outfile.write(most_fit.report() + "\n")
            best_of_generations.append(most_fit)
            generations.append(generation)
            values = values + [x.total_value() for x in population]
            weights = weights + [x.total_weight() for x in population]
            fitness_scores = fitness_scores + [x.fitness_score() for x in population]
            mean_fitness_scores = mean_fitness_scores + [np.mean([x.fitness_score() for x in population])]
            mean_values.append(np.mean([x.total_value() for x in population]))
    return generations,mean_values,weights,values,fitness_scores,mean_fitness_scores,population,best_of_generations,matings,population_record


def evolve_numeric_optimizer_population(population,mating_rate,litter_size,step,mutation_prob):
    '''
    Wrapper function on breed_population to solve 2D function minimization problems.
    :param population:
    :param mating_rate:
    :param litter_size:
    :param step:
    :param mutation_prob:
    :return:
    '''
    generations = []
    population_record = [population]
    xs = []
    ys = []
    fitness_scores = []
    mean_fitness_scores = []
    best_of_generations = []
    with open("output_ga.txt",'w') as outfile:
        for generation in range(step):
            print("Generation {}".format(generation))
            most_fit = sorted(population,key=lambda x: x.fitness_score())[-1]
            population,mating_set = breed_population(population,mating_rate = mating_rate,litter_size=litter_size,mutation_prob=mutation_prob,generation=generation)
            population_record.append(population)
            outfile.write(most_fit.report() + "\n")
            best_of_generations.append(most_fit)
            generations.append(generation)
            fitness_scores = fitness_scores + [x.fitness_score() for x in population]
            mean_fitness_scores = mean_fitness_scores + [np.mean([x.fitness_score() for x in population])]
    return generations,xs,ys,fitness_scores,mean_fitness_scores,population,best_of_generations,population_record