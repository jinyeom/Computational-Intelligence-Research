import math
import random as r

class GA:
    def __init__(self, n_gen, n_pop, n_mut, n_xover, l_dna):
        self.n_gen = n_gen
        self.n_pop = n_pop
        self.p_mut = p_mut
        self.p_xover = p_xover
        self.l_dna = l_dna
        self.population = self.init_population()

    def set_n_gen(self, n):
        self.n_gen = n

    def set_n_pop(self, n):
        self.n_pop = n

    def set_p_mutation(self, p):
        self.p_mut = p

    def set_p_crossover(self, p):
        self.p_xover = p

    def set_l_dna(self, n):
        self.l_dna = n

    def gen_dna(self):
        return [r.random() > 0.5 for _ in range(self.l_dna)]

    def init_population(self):
        return [self.gen_dna() for _ in range(self.n_pop)]

    def t_selection(self):
        best = r.choice(self.population)
        for _ in range(n_pop - 1):
            rand = r.choice(self.population)
            if rand.fitness > best.fitness:
                best = rand

        return best

    def mutation(self, dna):
        return [b if r.random() < self.p_mut else not b for b in dna]

    def u_crossover(self, dna_1, dna_2):
        c_dna_1 = []
        c_dna_2 = []

        for i in range(len(dna_1)):
            if r.random() < self.p_xover:
                c_dna_1.append(dna_1[i])
                c_dna_2.append(dna_2[i])
            else:
                c_dna_1.append(dna_2[i])
                c_dna_2.append(dna_1[i])

        return c_dna_1, c_dna_2
