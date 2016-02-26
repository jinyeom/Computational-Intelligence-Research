import MultiCutGA as ga
import random
from copy import deepcopy as copy

testind1 = ga.Cut([[0,0,0,1,1],[1,1,1,0,0]])
testind2 = ga.Cut([[.1,.1,.1,.2,.2],[.3,.3,.3,.4,.4]])

print('--------MUTATION TEST--------')

for i in range(10):
    t = copy(testind2)
    result = ga.mutate(t,0,.05,.2,.5)
    print(result[0].cut_info)

print('--------CROSSOVER TEST--------')

cutpb = 0.2
indpb = 0.2

print "cutpb = %(c)1.1f, indpb = %(i)1.1f" % \
        {"c" : cutpb, "i" : indpb}

for i in range(10):
    t1 = copy(testind1)
    t2 = copy(testind2)
    result = ga.xover(t1,t2,cutpb,indpb)
    print(result[0].cut_info)
    print(result[1].cut_info)
    print('---------------')
