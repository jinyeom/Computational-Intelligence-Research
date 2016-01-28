import math
from ga import GA

n_gen = 500
n_pop = 10
p_mut = 0.3
p_xover = 0.3
p_weight = 7
l_dna = 32

def f1(x):
    return (6 * x - 2) ** 2 * math.sin(12 * x - 4)

def f2(x1, x2):
    return (1. * (x2 - (5.1 / (4. * math.pi ** 2)) * x1 ** 2 +
            (5. / math.pi) * x1 - 6.) ** 2 + 10. * (1 - 1 / (8 * math.pi)) *
             math.cos(x1) + 10.)

def f3()


# TEST NUM. 1 -- f1(x)
g = GA(10, 10, p_mut, p_xover, l_dna)

b_gene = ""
b_fitness = 999999

g.init_population()

for _ in range(g.n_gen):

    decimals = [g.in_context(-2., 2., g.to_decimal(g.population[i]), l_dna)
                for i in range(g.n_pop)]

    scores = [f1(x) for x in decimals]

    for i, gene in enumerate(g.population):

        if scores[i] < b_fitness:
            b_fitness = scores[i]
            b_gene = gene

    children = []

    for i in range(g.n_pop / 2):
        p1 = g.t_selection(scores)
        p2 = g.t_selection(scores)

        ch1, ch2 = g.u_crossover(g.population[p1], g.population[p1])

        children.append(g.mutation(ch1))
        children.append(g.mutation(ch2))

    g.population = children

print "f1(x) = %f" % b_fitness



# TEST NUM. 2 -- f2(x1, x2)
g = GA(n_gen, n_pop, p_mut, p_xover, l_dna * 2)

b_gene = ""
b_fitness = 999999

g.init_population()

for _ in range(g.n_gen):

    decimals = []
    for gene in g.population:
        pair = []

        pair.append(g.in_context(-5., 10.,
                    g.to_decimal(gene[0:l_dna]), l_dna))
        pair.append(g.in_context(0., 15.,
                    g.to_decimal(gene[l_dna:l_dna * 2]), l_dna))

        decimals.append(pair)

    scores = [f2(pair[0], pair[1]) for pair in decimals]

    for i, gene in enumerate(g.population):

        if scores[i] < b_fitness:
            b_fitness = scores[i]
            b_gene = gene

    children = []

    for i in range(g.n_pop / 2):
        p1 = g.t_selection(scores)
        p2 = g.t_selection(scores)

        ch1, ch2 = g.u_crossover(g.population[p1], g.population[p1])

        children.append(g.mutation(ch1))
        children.append(g.mutation(ch2))

    g.population = children

print "f2(x) = %f" % b_fitness
