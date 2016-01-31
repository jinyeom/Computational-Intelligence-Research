# target.py
import math
import random as r
import config as c

class Target:
    def __init__(self):
        self.position = [0, 0]
        self.reset()

    def reset(self):
        self.position = [r.randrange(c.game['width']),
                        r.randrange(c.game['height'])]
