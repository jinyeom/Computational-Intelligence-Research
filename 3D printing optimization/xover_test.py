import xover
import random
from copy import deepcopy as copy

testind1 = xover.Cut([[0, 0, 0, 1, 1], [1, 1, 1, 0, 0], [.2, .3, .4, 1, 1]])
testind2 = xover.Cut([[.1,.1,.1,.2,.2], [.3,.3,.3,.4,.4]])

print('--------CROSSOVER TEST--------')

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
