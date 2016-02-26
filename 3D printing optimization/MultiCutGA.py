'''
Created on Dec 5, 2015

@author: ericyu
'''
import random
import pickle
import subprocess
import math
import numpy

from scoop import futures

import os
import sys
from deap import algorithms
from deap import base
from deap import creator
from deap import tools
from copy import deepcopy


OBJECT_FILE = sys.argv[1]

def get_bounds(object_file):
    f = open(object_file)
    min_x, max_x = float("inf"), float("-inf")
    min_y, max_y = float("inf"), float("-inf")
    min_z, max_z = float("inf"), float("-inf")
    for line in f:
        parts = line.split(" ")
        if(parts[0] == 'v'):
            x = float(parts[1])
            y = float(parts[2])
            z = float(parts[3])

            min_x = min(x, min_x)
            max_x = max(x, max_x)
            min_y = min(y, min_y)
            max_y = max(y, max_y)
            min_z = min(z, min_z)
            max_z = max(z, max_z)
    return min_x, max_x, min_y, max_y, min_z, max_z

MIN_X, MAX_X, MIN_Y, MAX_Y, MIN_Z, MAX_Z = get_bounds(OBJECT_FILE)

CXPB = .5
MUTPB = .5
NGEN = 1000
POP_SIZE = 100
BACKUP_INTERVAL = 100
LAMBDA = POP_SIZE

class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def dot_prod(vec1, vec2):
    result = 0
    for i in range(len(vec1)):
        result += (vec1[i]*vec2[i])
    return result

def difference(vec1,vec2):
    result = []
    for i in range(len(vec1)):
        result.append(vec1[i]-vec2[i])
    return result

def rel_to_point(rel):
    point = []
    point.append(rel[0] * (MAX_X - MIN_X) + MIN_X)
    point.append(rel[1]* (MAX_Y - MIN_Y) + MIN_Y)
    point.append(rel[2] * (MAX_Z - MIN_Z) + MIN_Z)
    return point

def angles_to_vec(angles):
    norm = []
    norm.append(math.cos(angles[1]* math.pi) * math.cos(angles[0] * math.pi))
    norm.append(math.cos(angles[1] * math.pi) * math.sin(angles[0] * math.pi))
    norm.append(math.sin(angles[1] * math.pi))
    return norm

# is the point on the left or right?
# negative left, positive right
def plane_side(plane_point, plane_norm, point):
    point_vec = difference(point, plane_point)
    return dot_prod(point_vec, plane_norm)

class Cut(object):
    def __init__(self, cut_array):
        self.cut_info = cut_array

    def getNumCuts(self):
        cuts = list(self.cut_info)
        return len(cuts)

    def toTree(self):
        cuts = list(self.cut_info)
        tree = Node(cuts[0], None, None)
        index = 1
        while(index<len(cuts)):
            cut = cuts[index]
            node = tree
            while(True):
                val = node.val
                if plane_side(rel_to_point(val[:3]), angles_to_vec(val[-2:]), rel_to_point(cut[:3]))<0:
                    if node.left == None:
                        node.left = Node(cut,None,None)
                        break
                    else:
                        node = node.left
                else:
                    if node.right == None:
                        node.right = Node(cut,None,None)
                        break
                    else:
                        node = node.right

            index = index+1
        return tree

    def toString(self):
        result = ""
        tree = self.toTree()
        queue = [tree]
        count = 1
        while(len(queue)>0):
            node = queue.pop()
            l_count, r_count = (0,0)
            if node.left is not None:
                count += 1
                l_count = count
                queue.insert(0, node.left)
            if node.right is not None:
                count += 1
                r_count = count
                queue.insert(0, node.right)
            result += str(l_count) + ', '+ str(r_count)+ ', '+ ', '.join(str(x) for x in rel_to_point(node.val[:3]))+', '\
                +', '.join(str(x) for x in angles_to_vec(node.val[-2:])) +'\n'
        return result

def generate_random_cut():
    return [[random.random() for i in range(5)] for x in range(random.randint(1,6))]


creator.create("Fitness", base.Fitness, weights=(-1.0, -1.0))
creator.create("Individual", Cut, fitness=creator.Fitness)

toolbox = base.Toolbox()
toolbox.register("map", futures.map)
toolbox.register("individual", tools.initIterate, creator.Individual, generate_random_cut)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)


def evalSlice(individual):
    cut_info = individual.toString()
    slice_file = 'slice_info'+ str(hash(cut_info)+random.randint(0, 10**20))
    f = open(slice_file, 'w')
    f.write(cut_info)
    f.close()
    result = float(subprocess.check_output(['./slicing', OBJECT_FILE, slice_file]))
    os.remove(slice_file)
    return result, individual.getNumCuts()

toolbox.register("evaluate", evalSlice)

'''def checkBounds(min, max):
    def decorator(func):
        def wrapper(*args, **kargs):
            offspring = func(*args, **kargs)
            for child in offspring:
                for i in range(len(child)):
                    if child[i] > max:
                        child[i] = max
                    elif child[i] < min:
                        child[i] = min
            return offspring
        return wrapper
    return decorator'''

def cross(ind1, ind2, cutpb, indpb):
    min_size = min(ind1.getNumCuts(),ind2.getNumCuts())
    # 1 point cross over of cuts
    if random.random()<cutpb and min_size>1:
        print("cut")
        cxpoint1 = random.randint(1, ind1.getNumCuts()-1)
        cxpoint2 = random.randint(1, ind2.getNumCuts()-1)

        ind1.cut_info[cxpoint1:], ind2.cut_info[cxpoint2:] \
            = ind2.cut_info[cxpoint2:], ind1.cut_info[cxpoint1:]
    else:
        print("ind")
        num_swaps = max(1, sum([1 for i in range(min_size) if random.random()<indpb]))
        for x in range(num_swaps):
            i = random.randint(0,ind1.getNumCuts()-1)
            j = random.randint(0,ind2.getNumCuts()-1)
            if random.random()<.5:
                ind1.cut_info[i][:3], ind2.cut_info[j][:3] \
                    = ind2.cut_info[j][:3], ind1.cut_info[i][:3]
            else:
                ind1.cut_info[i][-2:], ind2.cut_info[j][-2:] \
                    = ind2.cut_info[i][-2:], ind1.cut_info[i][-2:]
    return ind1, ind2

toolbox.register("mate", cross, cutpb=.2, indpb=.25)

def mutate(ind, mu, sigma, shufflepb, indpb):
    if random.random()<shufflepb and ind.getNumCuts>1:
        old = deepcopy(ind.cut_info)
        while(old == ind.cut_info):
            random.shuffle(ind.cut_info)
    else:
        num_cuts = ind.getNumCuts()
        num_vals = num_cuts*5
        num_mutations = max(1,sum([1 for i in range(num_vals) if random.random()<indpb]))
        for x in range(num_mutations):
            i = random.randint(0,num_cuts-1)
            j = random.randint(0,4)
            val = ind.cut_info[i][j]+random.gauss(mu, sigma)
            ind.cut_info[i][j] = max(min(val,.98),.02)
    return ind

toolbox.register("mutate", mutate, mu=0, sigma=.05, shufflepb=.5,indpb =.3)
toolbox.register("select", tools.selNSGA2)

def main():
    pop = toolbox.population(POP_SIZE)
    hof = tools.HallOfFame(10)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean, axis=0)
    stats.register("std", numpy.std, axis=0)
    stats.register("min", numpy.min, axis=0)
    stats.register("max", numpy.max, axis=0)


    logbook = tools.Logbook()
    logbook.header = ['gen', 'nevals'] + stats.fields

    # Evaluate the individuals with an invalid fitness
    invalid_ind = [ind for ind in pop if not ind.fitness.valid]
    fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
    for ind, fit in zip(invalid_ind, fitnesses):
        ind.fitness.values = fit

    hof.update(pop)

    record = stats.compile(pop)
    logbook.record(gen=0, nevals=len(invalid_ind), **record)
    print logbook.stream

    # Begin the generational process
    for gen in range(1, NGEN + 1):
        # Vary the population
        offspring = algorithms.varOr(pop, toolbox, LAMBDA, CXPB, MUTPB)

        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        # Update the hall of fame with the generated individuals
        hof.update(offspring)

        # Select the next generation population
        pop[:] = toolbox.select(pop + offspring, POP_SIZE)

        # Update the statistics with the new population
        record = stats.compile(pop)
        logbook.record(gen=gen, nevals=len(invalid_ind), **record)
        print logbook.stream

        if(gen%BACKUP_INTERVAL==0):
            f = open("gen"+str(gen)+".pkl","wb")
            pickle.dump(pop, f)
            f.close()

    print("Hall of Fame")
    for i in range(len(hof)):
        print("--------------")
        print(hof[i].toString())

    print("Last Population")
    for ind in pop:
        print("--------------")
        print(ind.toString())
        print(ind.fitness)
        print("")

    '''test = Cut(generate_random_cut())
    print(test.toString())'''

if __name__ == "__main__":
    main()
