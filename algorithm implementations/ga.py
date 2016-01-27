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

    def gen_DNA(self):
        dna = ""

        for _ in range(self.l_dna):
            if r.random() > 0.5: dna += "1"
            else: dna += "0"

        return dna

    def init_population(self):
        return [self.gen_dna() for _ in range(self.n_pop)]

    def t_selection(self, fitness):
        best = r.choice(self.population)
        for _ in range(n_pop - 1):
            rand = r.choice(self.population)
            if fitness(rand) > fitness(best):
                best = rand

        return best

    def mutation(dna):
        mutated = ""

        for b in dna:
            if r.random() < self.p_mut: mutated += b
            else:
                if b == "1": mutated += "0"
                else: mutated += "1"

        return mutated

    def u_crossover(dna_1, dna_2):
        c_dna_1 = ""
        c_dna_2 = ""

        for i in range(len(dna_1)):

            if r.random() < self.p_xover:
                c_dna_1 += dna_1[i]
                c_dna_2 += dna_2[i]
            else:
                c_dna_1 += dna_2[i]
                c_dna_2 += dna_1[i]

        return c_dna_1, c_dna_2
