import math
import random

class GA:
    def __init__(self, s_dna, s_pop, n_gen, p_mut, p_xover):
        # config.
        self.s_dna = s_dna          # DNA size
        self.s_pop = s_pop          # population size
        self.n_gen = n_gen          # number of generations
        self.p_mut = p_mut          # probability of mutation
        self.p_xover = p_xover      # probability of crossover

        # population
        self.population = self.init_population()

    # initialize population
    def init_population(self):
        return [self.gen_DNA() for _ in range(self.n_pop)]

    # generate a dna
    def gen_DNA(self):
        return [(random.random() > 0.5) for _ in range(self.s_dna)]

    # mutation
    def mutation(self):
        for _, dna in enumerate(self.population):
            for i in range(len(dna))

    # uniform crossover
    def u_crossover(self):


    # execute GA
    def execute(self):




if __name__ == "__main__":
