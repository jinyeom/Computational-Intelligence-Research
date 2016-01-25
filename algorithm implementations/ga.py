# ga.py

import math
import random as r

# genetic algorithm constants
p_mutation = 0.1
p_xover = 0.1

# set mutation probability
def set_p_mutation(p):
    p_mutation = p

def set_p_crossover(p):
    p_xover = p

# tournament selection
def t_selection(population):
    best = r.choice(population)
    for _ in range(len(population) - 1):
        rand = r.choice(population)
        if rand.fitness > best.fitness:
            best = rand
    return best

# mutate a DNA
def mutation(dna):
    return [b if r.random() < P_MUT else not b for b in dna]

# uniform crossover
def u_crossover(dna_1, dna_2):
    c_dna_1 = []
    c_dna_2 = []

    for i in range(len(dna_1)):
        if r.random() < P_XOVER:
            c_dna_1.append(dna_1[i])
            c_dna_2.append(dna_2[i])
        else:
            c_dna_1.append(dna_2[i])
            c_dna_2.append(dna_1[i])

    return c_dna_1, c_dna_2
