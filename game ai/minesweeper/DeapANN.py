import random
import math
import game
from ANN import ANN
from copy import deepcopy

from deap import base
from deap import creator
from deap import tools
from deap import algorithms

num_inputs = 2
num_hidden_nodes = 10
num_outputs = 1

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("attr_real", random.uniform, -10, 10)

#inputs->hidden_layer->outputs

toolbox.register("individual", tools.initRepeat, creator.Individual,
    toolbox.attr_real, num_hidden_nodes*(num_inputs+1)+ (num_hidden_nodes+1)*num_outputs)


toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalANN(individual):
    #return game.getFitness(individual),


toolbox.register("evaluate", evalANN)
toolbox.register("mate", tools.cxBlend, alpha = .05)
toolbox.register("mutate", tools.mutGaussian, mu = 0, sigma = .1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=2)

def main():

    # new game
    g = game.Game()

    random.seed(64)
    NGEN = 200

    pop = toolbox.population(n=100)

    ind_to_ann = dict()
    for ind in pop:
        ann = ANN(num_inputs, num_hidden_nodes, num_outputs,ind)
        g.add_agent(ann)
    f = g.game_loop

    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    for g in range(NGEN):
        offspring = toolbox.select(pop, len(pop))
        offspring = algorithms.varAnd(offspring, toolbox, cxpb=.5, mutpb=.5)

        ind_to_ann = dict()
        for ind in pop:
            ann = ANN(num_inputs, num_hidden_nodes, num_outputs,ind)
            g.add_agent(ann)
        f = g.game_loop()

        fitnesses = toolbox.map(toolbox.evaluate, offspring)
        for ind, fit in zip(offspring, fitnesses):
            ind.fitness.values = fit

        pop[:] = offspring


if __name__ == "__main__":
    main()
