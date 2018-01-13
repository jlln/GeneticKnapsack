import numpy as np

class Individual:
    def fitness_score(self):
        if self.total_weight() > self.max_weight:
            scaling_extra = self.total_weight() - (self.max_weight + 1)  # penalize being overweight
            scaling = self.total_weight() + scaling_extra
        else:
            scaling = self.total_weight() ** 0.5
        return self.total_value() ** 3 / (scaling + 1)

    def __init__(self, item_pool, max_weight=100):
        self.expected = int(np.round(max_weight / np.mean([x.weight for x in item_pool])))
        if self.expected > len(item_pool):
            self.expected = len(item_pool)
        self.items = np.random.choice(item_pool, size=self.expected, replace=False)
        self.item_pool = item_pool
        self.max_weight = max_weight

    def total_weight(self):
        return np.sum([x.weight for x in self.items])

    def total_value(self):
        return np.sum([x.value for x in self.items])


    def report(self):
        return ";".join([str([i.weight,i.value]) for i in self.items])


    def mutate(self, prob):
        n_items = len(self.items)
        cutoff = np.random.random()
        if prob < cutoff:
            action = np.random.choice(["i","m","d"])
            if action == "i" or len(self.items) < 2:
                #             Insert
                if len(self.items) < len(self.item_pool):
                    self.items = list(self.items) + list(
                        np.random.choice([x for x in self.item_pool if x not in self.items], size=1))

            elif action == "m":
                #             Modify
                mut_index = np.random.randint(0, n_items)
                if len([x for x in self.item_pool if x not in self.items]) > 0:
                    self.items[mut_index] = np.random.choice([x for x in self.item_pool if x not in self.items])
            else:
                #             Delete
                mut_element = np.random.choice(self.items)
                self.items = [x for x in self.items if x != mut_element]

    def breed(self, partner):
        combined_genes = list(set(list(self.items) + list(partner.items)))
        offspring = Individual(combined_genes, self.max_weight)
        offspring.mutate(0.05)
        return offspring