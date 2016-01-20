import math
import random
import config

class Agent:
    def __init__(self, nnet):
        self.brain = nnet
        self.fitness = 0
        self.speed = [0, 0]
        self.position = [0, 0]
        self.reset()

    def reset(self):
        self.fitness = 0
        self.position = [random.randrange(config.game['width']),
                        random.randrange(config.game['height'])]

    def update(self, targets):
        t_closest = self.get_closest_target(targets)


    def get_closest_target(self, targets):
        for t in targets:
            
