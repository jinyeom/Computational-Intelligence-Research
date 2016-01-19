import math
import random
import config

class Agent:
    def __init__(self, nnet):
        self.brain = nnet
        self.fitness = 0
        self.speed = [0, 0]
        self.position = [random.randrange(config.game['width']),
                        random.randrange(config.game['height'])]

    def update(self, input):
