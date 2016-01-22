import math
import random
import game

# initialize population
def init_population():
    return [gen_DNA() for _ in range(n_pop)]

# generate a dna
def gen_DNA():
    return [(random.random() > 0.5) for _ in range(s_dna)]

# tournament selection
def t_selection():




# mutate a DNA
def mutation(dna):
    for i in range(len(dna)):
        if random.random() < p_mut:
            dna[i] = not dna[i]

# uniform crossover
def u_crossover(dna_1, dna_2):
    for i in range(len(dna_1)):
        if random.random() < p_xover:
            temp = dna_1[i]
            dna_1[i] = dna_2[i]
            dna_2[i] = temp

# execute GA
def execute():
    population = init_population()
    best = None
    for _ in range(n_gen):
        scores = minesweeper.gameLoop(t_game)
