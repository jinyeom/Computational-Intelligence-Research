import MultiCutGA
import subprocess
from MultiCutGA import Cut 
import xover
import random
from copy import deepcopy as copy
import sys

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

t_ind_1 = MultiCutGA.Cut([[0.5, 0.5, 0.5, 0, 0], [0.5, 0.7, 0.3, 0.5, 0]])
t_ind_2 = MultiCutGA.Cut([[0.7, 0.7, 0.7, 0.7, 0], [0.3, 0.3, 0.3, 0.2, 0]])

F_PATH = sys.argv[1]
obj = open(F_PATH) 

c_1 = t_ind_1.toString()    # Individual 1 cut
c_2 = t_ind_2.toString()    # Individual 2 cut

f_1 = open("ind_1.txt", "w+")
f_2 = open("ind_2.txt", "w+")

f_1.write(c_1)
f_2.write(c_2)

f_1.close()
f_2.close()

process_1 = subprocess.Popen(["./slicing", F_PATH, "ind_1.txt"], stdout = subprocess.PIPE)
out, err = process_1.communicate()

subprocess.call(["mv", "./piece-0.obj", "./piece-0-1-" + ".obj"])
subprocess.call(["mv", "./piece-1.obj", "./piece-1-1-" + ".obj"])
subprocess.call(["mv", "./piece-2.obj", "./piece-2-1-" + ".obj"])

process_2 = subprocess.Popen(["./slicing", F_PATH, "ind_2.txt"], stdout = subprocess.PIPE)
out, err = process_2.communicate()

subprocess.call(["mv", "./piece-0.obj", "./piece-0-2" + ".obj"])
subprocess.call(["mv", "./piece-1.obj", "./piece-1-2" + ".obj"])
subprocess.call(["mv", "./piece-2.obj", "./peice-2-2" + ".obj"])

for i in range(5):
    t1 = copy(t_ind_1)
    t2 = copy(t_ind_2)

    result = MultiCutGA.xover(t1, t2, cutpb, indpb)
    
    c_info_1 = "c_info_" + str(i) + "_xover_1.txt"
    c_info_2 = "c_info_" + str(i) + "_xover_2.txt"

    cut_info_1 = result[0].toString()
    cut_info_2 = result[1].toString()

    f_1 = open(c_info_1, "w+")
    f_2 = open(c_info_2, "w+")

    f_1.write(cut_info_1)
    f_2.write(cut_info_2)

    f_1.close()
    f_2.close()

    process_1 = subprocess.Popen(["./slicing", F_PATH, c_info_1], stdout = subprocess.PIPE)
    out, err = process_1.communicate()

    subprocess.call(["mv", "./piece-0.obj", "./result/c_1_piece-0-1-" + str(i) + ".obj"])
    subprocess.call(["mv", "./piece-1.obj", "./result/c_1_piece-1-1-" + str(i) + ".obj"])
    subprocess.call(["mv", "./piece-2.obj", "./result/c_1_piece-2-1-" + str(i) + ".obj"])

    process_2 = subprocess.Popen(["./slicing", F_PATH, c_info_2], stdout = subprocess.PIPE)
    out, err = process_2.communicate()

    subprocess.call(["mv", "./piece-0.obj", "./result/c_2_piece-0-2-" + str(i) + ".obj"])
    subprocess.call(["mv", "./piece-1.obj", "./result/c_2_piece-1-2-" + str(i) + ".obj"])
    subprocess.call(["mv", "./piece-2.obj", "./result/c_2_piece-2-2-" + str(i) + ".obj"])
