import subprocess
import time
from time import gmtime, strftime

F_PATH = "./t.obj"
obj = open(F_PATH)

# x, y, z data
x = []
y = []
z = []

# collect data for x, y, and z
for line in obj:
    if line[0] == "v" and line[1] != "n":
        tokens = line.split()
        x.append(float(tokens[1]))
        y.append(float(tokens[2]))
        z.append(float(tokens[3]))

x_min = min(x)
x_max = max(x)
y_min = min(y)
y_max = max(y)
z_min = min(z)
z_max = max(z)

print "x min = " + str(x_min)
print "x max = " + str(x_max)
print "y min = " + str(y_min)
print "y max = " + str(y_max)
print "z min = " + str(z_min)
print "z max = " + str(z_max)

x_step = 0.01

x_cut = x_min
y_avg = (y_min + y_max)/2.0
z_avg = (z_min + z_max)/2.0

while x_cut <= x_max:
    c_info = open("c_info.txt", "w+")
    cut_info = [0., 0., x_cut, y_avg, z_avg, 1.0, 0.0, 0.0]
    ci_str = str(cut_info)
    c_info.write(ci_str[1:len(ci_str)-1])
    c_info.close()
    process = subprocess.Popen(["./slicing", F_PATH, "c_info.txt"], stdout=subprocess.PIPE)
    out, err = process.communicate()
    print out
    # **** GENETIC ALGORITHM HERE ****




    # rename the cut files
    subprocess.call(["mv", "./piece-0.obj", "./piece-0-"+str(x_cut)+".obj"])
    subprocess.call(["mv", "./piece-1.obj", "./piece-1-"+str(x_cut)+".obj"])

    x_cut += (x_max - x_min) * x_step

obj.close()
