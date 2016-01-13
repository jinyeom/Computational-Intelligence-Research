import math
import random
import time

GAME_TIME = 10000               # game duration
DELAY = 20                      # terminal update frequency
WIDTH = 400.                    # display width
HEIGHT = 400.                   # display height

# neural network constants
N_INS = 4
N_OUTS = 2
N_HLS = 2
N_HLNS = 5

# turn rate constants
R_MAX = 0.3                     # max turn rate
R_MIN = -0.3                    # min turn rate

# color constants
WHITE = (0xff, 0xff, 0xff)
RED = (0xff, 0x00, 0x00)
BLACK = (0x00, 0x00, 0x00)

# size constants
TANK_NUM = 20                   # maintained number of tanks
MINE_NUM = 40                   # maintained number of mines

# define a minesweeper
class MSweeper:
    # Constructor
    def __init__(self, nnet):
        # minesweeper setup
        self.Brain = nnet
        self.Rotation = 0.0
        self.LTrack = 0.16
        self.RTrack = 0.16
        self.Fitness = 0
        self.ClosestMine = 0
        self.Speed = 0.0
        self.Position = [0.0, 0.0]
        self.Vision = [0.0, 0.0]
        self.reset()

    # Resets the sweeper's position, fitness and rotation
    def reset(self):
        self.Position = [random.randrange(WIDTH), random.randrange(HEIGHT)]
        self.Fitness = 0
        self.Rotation = random.random()

    # update the sweeper's status
    def update(self, mines):
        # get vector to closest mine
        closest = self.getClosestMine(mines)
        dist = math.sqrt(closest[0] * closest[0] + closest[1] * closest[1])
        normalVec = [closest[0]/dist, closest[1]/dist]

        # inputs for neural network
        inputs = []

        inputs.append(normalVec[0])
        inputs.append(normalVec[1])

        inputs.append(self.Vision[0])
        inputs.append(self.Vision[1])

        # outputs from neural network
        outputs = self.Brain.update(inputs)
        self.LTrack = outputs[0]
        self.RTrack = outputs[1]

        # define rotation
        rotation = self.LTrack - self.RTrack
        if rotation < R_MIN:
            rotation = R_MIN
        elif rotation > R_MAX:
            rotation = R_MAX

        # update msweeper's rotation, speed, and position
        self.Rotation += rotation
        self.Speed = self.LTrack + self.RTrack

        self.Vision[0] = -math.sin(self.Rotation)
        self.Vision[1] = math.cos(self.Rotation)

        self.Position[0] += self.Vision[0] * self.Speed
        self.Position[1] += self.Vision[1] * self.Speed

        # wrap around window limits
        if self.Position[0] > WIDTH:
            self.Position[0] = 0.0
        if self.Position[0] < 0.0:
            self.Position[0] = WIDTH
        if self.Position[1] > HEIGHT:
            self.Position[1] = 0.0
        if self.Position[1] < 0.0:
            self.Position[1] = HEIGHT

    # get the closest mine
    def getClosestMine(self, mines):
        closest = 99999.0
        closestVec = [0.0, 0.0]

        # search for the closest mine
        for i in range(len(mines)):
            diff = [self.Position[0] - mines[i].Position[0],
                    self.Position[1] - mines[i].Position[1]]
            dist = math.sqrt(diff[0] * diff[0] + diff[1] * diff[1])
            if dist < closest:
                closest = dist
                closestVec = diff
                self.ClosestMine = i
        return closestVec

    # check collision with the closest mine
    def checkCollision(self, mines, size):
        closestMine = mines[self.ClosestMine]
        diff = [self.Position[0] - closestMine.Position[0],
                self.Position[1] - closestMine.Position[1]]
        dist = math.sqrt(diff[0] * diff[0] + diff[1] * diff[1])
        if dist < (size + 5.0):
            return self.ClosestMine
        return -1

# define a mine
class Mine:
    # Constructor
    def __init__(self):
        self.Position = [0.0, 0.0]
        self.reset()

    # every time there is a collision with a tank, reposition the mine
    def reset(self):
        self.Position[0] = random.randrange(WIDTH)
        self.Position[1] = random.randrange(HEIGHT)

# sort tanks by their fitness
def sortTanks(tanks):
    if len(tanks) == 0:
        return tanks
    pivot = tanks[0]
    rest = tanks[1:len(tanks)]
    bigger = [t for t in rest if t.Fitness > pivot.Fitness]
    equal = [t for t in rest if t.Fitness == pivot.Fitness]
    smaller = [t for t in rest if t.Fitness < pivot.Fitness]
    return sortTanks(bigger) + sortTanks(equal) + sortTanks(smaller)

# print each tank's status
def updateTerminal(mines, tanks):
    print "\033[2J\033[H"
    print "\t------------------- MINESWEEPER ----------------------\n"

    for i, tank in enumerate(tanks):
        print "TANK " + repr(i).rjust(2) + ": ",
        print "X: " + repr(tank.Position[0]).rjust(20),
        print "Y: " + repr(tank.Position[1]).rjust(20),
        print "FITN.:" + repr(tank.Fitness).rjust(4)

# game loop
def gameLoop():
    # generate <MINE_NUM> mines with random positions
    mines = [Mine() for i in range(MINE_NUM)]

    # generate <TANK_NUM> tanks with random positions
    tanks = [MSweeper(NNetwork(N_INS, N_OUTS, N_HLS, N_HLNS))
            for i in range(TANK_NUM)]

    # game loop
    print "\033[?47h"
    for i in range(GAME_TIME):
        # move all the tanks
        for tank in tanks:
            tank.update(mines)
            # check collision with a mine
            if tank.checkCollision(mines, 2) != -1:
                mines[tank.ClosestMine].reset()
                tank.Fitness += 1
        # update the terminal screen given the delay frequency
        if i % DELAY == 0:
            updateTerminal(mines, tanks)
    # return the tanks
    return tanks

# play the game
if __name__ == '__main__':
    # from neural_network import NNetwork
    # start1 = time.time()
    # result = gameLoop()
    # end1 = time.time()

    from neural_network_simplified import NNetwork
    start2 = time.time()
    result = gameLoop()
    end2 = time.time()

    # print "NNET: " + str(end1 - start1)
    print "NNET_SIM: " + str(end2 - start2)
