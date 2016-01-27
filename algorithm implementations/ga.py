import math
import random as r

class GA:
    def __init__(self, n_gen, n_pop, p_mut, p_xover, l_dna):
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
        return [self.gen_DNA() for _ in range(self.n_pop)]

    def t_selection(self, scores):
        best = r.randrange(self.n_pop)
        for _ in range(self.n_pop - 1):
            rand = r.randrange(self.n_pop)
            if scores[rand] > scores[best]:
                best = rand

        # return the index
        return best

    def mutation(self, dna):
        mutated = ""

        for b in dna:
            if r.random() < self.p_mut: mutated += b
            else:
                if b == "1": mutated += "0"
                else: mutated += "1"

        return mutated

    def u_crossover(self, dna_1, dna_2):
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

    def to_decimal(self, dna):
        d_num = 0

        for i, b in enumerate(dna):
            if b == "1": d_num += 2 ** i

        return d_num

    def in_context(self, x_min, x_max, d_num, l_dna):
        r_min = 0.0
        r_max = 2 ** l_dna - 1
        precision = (x_max - x_min) / (r_max - r_min)

        return x_min + d_num * precision
