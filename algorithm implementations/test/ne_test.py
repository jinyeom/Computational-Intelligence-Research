import math
from ga import GA
from ne import NNetwork

n_i = 2
n_hl = 1
n_hln = 3
n_o = 1

n_gen = 100
n_pop = 100
p_mut = 0.1
p_xover = 0.1
p_weight = 7
l_dna = (n_hln * (n_i + n_hln * n_hl + n_o) + n_o) * p_weight

g = GA(n_gen, n_pop, n_mut, n_xover, l_dna)

b_gene = []
b_fitness = -1

g.init_population()

for _ in range()
