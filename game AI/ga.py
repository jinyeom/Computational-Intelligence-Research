# ga.py
import math
import pygame
import random as r
import config as c
from agent import Agent
from game import Game
from neural_network import NNetwork as NNet

# initialize population given number of population and length of each DNA
def init_population(n_pop, l_dna):
    return [gen_DNA(l_dna) for _ in range(n_pop)]

def gen_DNA(l_dna):
    dna = ""

    for _ in range(l_dna):
        if r.random() > 0.5: dna += "1"
        else: dna += "0"

    return dna

# tournament selection (returns the best index)
def t_selection(agents):
    best = r.randrange(len(agents))

    for _ in range(len(agents) - 1):
        rand = r.randrange(len(agents))

        if agents[rand].fitness > agents[best].fitness:
            best = rand

    return best

# return a mutated deep copy of a DNA
def mutation(dna):
    mutated = ""

    for b in dna:
        if r.random() < c.ga['p_mut']: mutated += b
        else:
            if b == "1": mutated += "0"
            else: mutated += "1"

    return mutated

# uniform crossover
def u_crossover(dna_1, dna_2):
    c_dna_1 = ""
    c_dna_2 = ""

    for i in range(len(dna_1)):

        if r.random() < c.ga['p_xover']:
            c_dna_1 += dna_1[i]
            c_dna_2 += dna_2[i]
        else:
            c_dna_1 += dna_2[i]
            c_dna_2 += dna_1[i]

    return c_dna_1, c_dna_2

# execute GA
def execute():
    population = init_population(c.game['n_agents'], c.l_dna)
    g = Game(population)

    b_fitness = -1
    b_gene = ""

    for _ in range(c.ga['n_gen']):
        g.game_loop()

        if g.agents[0].fitness > b_fitness:
            b_gene = g.agents[0].brain.dna
            b_fitness = g.agents[0].fitness

        children = []

        for __ in range(c.game['n_agents'] / 2):
            p_1 = t_selection(g.agents)
            p_2 = t_selection(g.agents)

            c_dna_1, c_dna_2 = u_crossover(g.agents[p_1].brain.dna,
                                            g.agents[p_2].brain.dna)

            children.append(mutation(c_dna_1))
            children.append(mutation(c_dna_2))

        g.gen += 1
        g.agents = [Agent(i, NNet(children[i]))
                    for i in range(c.game['n_agents'])]

        for t in g.targets:
            t.reset()

    g.agents = [Agent(0, NNet(b_gene))]
    g.game_loop()
    pygame.quit()


if __name__ == '__main__':
    execute()
