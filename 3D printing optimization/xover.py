import random
from copy import deepcopy

class Cut(object):
    def __init__(self, cut_array):
        self.cut_info = cut_array

    def getNumCuts(self):
        cuts = list(self.cut_info)
        return len(cuts)

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

# Jin's implementation of Crossover
def xover(ind_1, ind_2, cutpb, indpb):
    t_ind_1 = deepcopy(ind_1)

    n_cuts_1 = ind_1.getNumCuts()
    n_cuts_2 = ind_2.getNumCuts()

    min_size = min(n_cuts_1, n_cuts_2)

    if random.random() < cutpb and min_size > 1:
        print("MACRO-XOVER")

        xp_1 = random.randint(1, n_cuts_1 - 1)
        xp_2 = random.randint(1, n_cuts_2 - 1)

        ind_1.cut_info[xp_1:], ind_2.cut_info[xp_2:] \
            = ind_2.cut_info[xp_2:], ind_1.cut_info[xp_1:]
    else:
        print("MICRO-XOVER")

        num_swaps = max(1, sum([1 for i in range(min_size)
                                if random.random() < indpb]))

        for x in range(num_swaps):
            i = random.randint(0, n_cuts_1 - 1)
            j = random.randint(0, n_cuts_2 - 1)

            if random.random() < .5:
                ind_1.cut_info[i][:3], ind_2.cut_info[j][:3] \
                    = ind_2.cut_info[j][:3], ind_1.cut_info[i][:3]
            else:
                ind_1.cut_info[i][-2:], ind_2.cut_info[j][-2:] \
                    = ind_2.cut_info[j][-2:], ind_1.cut_info[i][-2:]

    # mutate the children if they are the same as the parents
    if t_ind_1.cut_info == ind_1.cut_info:
        print "XOVER_FAILED: MUTATION"
        return mutate(ind_1, 0, .05, .2, .5), mutate(ind_2, 0, .05, .2, .5)

    return duplicate_free(ind_1), duplicate_free(ind_2)

# check for duplicates in an individual
def duplicate_free(ind):
    new_cut_info = []

    for cut in ind.cut_info:
        if cut not in new_cut_info:
            new_cut_info.append(cut)

    return Cut(new_cut_info)
