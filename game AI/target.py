import math
import random
import config

class Target:
    def __init__(self):
        self.position = [0, 0]
        self.reset()

    def reset(self):
        self.position = [random.randrange(config.game['width']),
                        random.randrange(config.game['height'])]
