import math
import random
import minesweeper

# config.
s_dna = 10          # DNA size
s_pop = 20          # population size
n_gen = 20          # number of generations
p_mut = 0.1         # probability of mutation
p_xover = 0.1       # probability of crossover
t_game = 10000      # game execution time

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
        
