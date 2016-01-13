import math
import random
import time

GAME_TIME = 10000               # game duration
DELAY = 10                      # terminal update frequency
D_WIDTH = 400.                  # display width
D_HEIGHT = 400.                 # display height

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
        self.Rotation = random.random()
        self.LTrack = 0.16
        self.RTrack = 0.16
        self.Fitness = 0
        self.ClosestMine = 0
        self.Speed = 0.0
        self.XCoord = random.randrange(D_WIDTH)
        self.YCoord = random.randrange(D_HEIGHT)
        self.XLookAt = 0.0
        self.YLookAt = 0.0

    # Resets the sweeper's position, fitness and rotation
    def reset(self):
        self.XCoord = random.randrange(D_WIDTH)
        self.YCoord = random.randrange(D_HEIGHT)
        self.Fitness = 0
        self.Rotation = random.random()

    # update the sweeper's status
    def update(self, mines):
        # get vector to closest mine
        closestMVec = self.getClosestMine(mines)
        normalVec = closestMVec.vecNormalize()

        # inputs for neural network
        inputs = []

        inputs.append(normalVec.x)
        inputs.append(normalVec.y)

        inputs.append(self.XLookAt)
        inputs.append(self.YLookAt)

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

        self.XLookAt = -math.sin(self.Rotation)
        self.YLookAt = math.cos(self.Rotation)

        self.XCoord += self.XLookAt * self.Speed
        self.YCoord += self.YLookAt * self.Speed

        # wrap around window limits
        if self.XCoord > D_WIDTH:
            self.XCoord = 0.0
        if self.XCoord < 0.0:
            self.XCoord = D_WIDTH
        if self.YCoord > D_HEIGHT:
            self.YCoord = 0.0
        if self.YCoord < 0.0:
            self.YCoord = D_HEIGHT

    # get the closest mine
    def getClosestMine(self, mines):
        closest = 99999.0
        closestVec = Vector2D(0.0, 0.0)
        msVec = Vector2D(self.XCoord, self.YCoord)

        # search for the closest mine
        for i in range(len(mines)):
            mVec = Vector2D(mines[i].XCoord, mines[i].YCoord)
            diffVec = msVec.vecDiff(mVec)
            dist = diffVec.vecLength()
            if dist < closest:
                closest = dist
                closestVec = diffVec
                self.ClosestMine = i
        return closestVec

    # check collision with the closest mine
    def checkCollision(self, mines, size):
        msVec = Vector2D(self.XCoord, self.YCoord)
        closestMine = mines[self.ClosestMine]
        mVec = Vector2D(closestMine.XCoord, closestMine.YCoord)
        dist = msVec.vecDiff(mVec).vecLength()
        if dist < (size + 5.0):
            return self.ClosestMine
        return -1

# define a mine
class Mine:
    # Constructor
    def __init__(self):
        self.XCoord = random.randrange(D_WIDTH)
        self.YCoord = random.randrange(D_HEIGHT)

    # every time there is a collision with a tank, reposition the mine
    def reposition(self):
        self.XCoord = random.randrange(D_WIDTH)
        self.YCoord = random.randrange(D_HEIGHT)

# define a 2D vector
class Vector2D:
    # Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # distance from this vector and another
    def vecLength(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    # vector difference of this vector and another
    def vecDiff(self, vec):
        vDiff = Vector2D(self.x, self.y)
        vDiff.x -= vec.x
        vDiff.y -= vec.y
        return vDiff

    def vecNormalize(self):
        normalized = Vector2D(self.x, self.y)
        normalized.x = self.x / self.vecLength()
        normalized.y = self.y / self.vecLength()
        return normalized

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
        print "X: " + repr(tank.XCoord).rjust(20),
        print "Y: " + repr(tank.YCoord).rjust(20),
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
                mines[tank.ClosestMine].reposition()
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
