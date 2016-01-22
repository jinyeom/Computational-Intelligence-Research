import math
import random
import config as c

class Target:
    def __init__(self):
        self.position = [0, 0]
        self.reset()

    def reset(self):
        self.position = [random.randrange(c.game['width']),
                        random.randrange(c.game['height'])]
