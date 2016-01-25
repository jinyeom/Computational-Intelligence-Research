# ga.py

import math
import random as r
import config as c
from game import Game

# tournament selection
def t_selection(agents):
    best = r.choice(agents)
    for _ in range(len(agents) - 1):
        rand = r.choice(agents)
        if rand.fitness > best.fitness:
            best = rand
    return best

# mutate a DNA
def mutation(dna):
    return [b if r.random() < c.ga['p_mut'] else not b for b in dna]

# uniform crossover
def u_crossover(dna_1, dna_2):
    c_dna_1 = []
    c_dna_2 = []

    for i in range(len(dna_1)):
        if r.random() < c.ga['p_xover']:
            c_dna_1.append(dna_1[i])
            c_dna_2.append(dna_2[i])
        else:
            c_dna_1.append(dna_2[i])
            c_dna_2.append(dna_1[i])

    return c_dna_1, c_dna_2

# execute GA
def execute():
    g = Game()
    b_fitness = -1
    b_gene = []

    for _ in range(c.ga['n_gen']):
        g.game_loop()

        if g.agents[0].fitness > b_fitness:
            b_gene = g.agents[0].brain.dna

        children_dna = []
        for __ in range(c.game['n_agents'] / 2):
            p_1 = t_selection(g.agents)
            p_2 = t_selection(g.agents)

            c_dna_1, c_dna_2 = u_crossover(p_1.brain.dna, p_2.brain.dna)

            children_dna.append(mutation(c_dna_1))
            children_dna.append(mutation(c_dna_2))

        for i, a in enumerate(g.agents):
            a.brain.init_weights(children_dna[i])
            a.reset()

        for t in g.targets:
            t.reset()

        g.generation += 1

    # g.game_loop(True)
    pygame.quit()

if __name__ == '__main__':
    execute()
