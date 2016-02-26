import xover
import random
from copy import deepcopy as copy

# -------- TEST 1 ----------

testind1 = xover.Cut([[0, 0, 0, 1, 1], [1, 1, 1, 0, 0], [.2, .3, .4, 1, 1]])
testind2 = xover.Cut([[.1,.1,.1,.2,.2], [.3,.3,.3,.4,.4]])

print('--------CROSSOVER TEST 1--------')

cutpb = 0.2
indpb = 0.2

print "cutpb = %(c)1.1f, indpb = %(i)1.1f\n" % \
        {"c" : cutpb, "i" : indpb}

for i in range(100):
    t1 = copy(testind1)
    t2 = copy(testind2)

    result = xover.xover(t1, t2, cutpb, indpb)

    print(result[0].cut_info)
    print(result[1].cut_info)
    print('---------------------------------------------')

# ---------- TEST 2 ----------

print('--------CROSSOVER TEST 2--------')

t_ind_1 = xover.Cut([[15, 15, 15, 0, 0], [15, 15, 15, 0.5, 0]])
t_ind_2 = xover.Cut([[20, 10, 40, .7, 0], [20, 10, 40, .2, 0]])

for i in range(10):
    t1 = copy(t_ind_1)
    t2 = copy(t_ind_2)

    result = xover.xover(t1, t2, cutpb, indpb)

    print(result[0].cut_info)
    print(result[1].cut_info)
    print('---------------------------------------------')
