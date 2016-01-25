# agent.py
import math
import random as r
import config as c

class Agent:
    def __init__(self, number, nnet):
        self.number         = number # agent number
        self.brain          = nnet # neural network
        self.fitness        = 0 # fitness
        self.t_closest      = 0 # index of the closest target
        self.speed          = 0.0 # movement speed
        self.track          = [0, 0] # [l_track, r_track]
        self.vision         = [0.0, 0.0] # [x, y] vision
        self.position       = [0, 0] # [x, y] position
        self.reset()

    def reset(self):
        self.fitness = 0
        self.rotation = r.random()
        self.position = [r.randrange(c.game['width']),
                        r.randrange(c.game['height'])]

    def update(self, targets):
        # get vector to closest mine
        closest = self.get_closest_target(targets)
        dist = math.sqrt(closest[0] * closest[0] + closest[1] * closest[1])

        normalized = [closest[0]/dist, closest[1]/dist]
        if dist == 0.0: normalized = [0.0, 0.0]

        # inputs for neural network
        inputs = []

        inputs.append(normalized[0])
        inputs.append(normalized[1])

        inputs.append(self.vision[0])
        inputs.append(self.vision[1])

        # outputs from neural network
        outputs = self.brain.update(inputs)
        self.track[0] = outputs[0]
        self.track[1] = outputs[1]

        # define rotation rate
        r_rotation = self.track[0] - self.track[1]
        if r_rotation < c.game['r_min']:
            r_rotation = c.game['r_min']
        elif r_rotation > c.game['r_max']:
            r_rotation = c.game['r_max']

        # update rotation
        self.rotation += r_rotation

        # update speed
        self.speed = self.track[0] + self.track[1]

        # update vision
        self.vision[0] = -math.sin(self.rotation)
        self.vision[1] = math.cos(self.rotation)

        # update position
        self.position[0] += self.vision[0] * self.speed
        self.position[1] += self.vision[1] * self.speed

        # wrap around window limits
        if self.position[0] > c.game['width']:
            self.position[0] = 0.0
        if self.position[0] < 0.0:
            self.position[0] = c.game['width']
        if self.position[1] > c.game['height']:
            self.position[1] = 0.0
        if self.position[1] < 0.0:
            self.position[1] = c.game['height']

    def get_closest_target(self, targets):
        closest = 99999.0
        closestVec = [0.0, 0.0]

        # search for the closest mine
        for index, t in enumerate(targets):
            diff = [self.position[0] - t.position[0],
                    self.position[1] - t.position[1]]
            dist = math.sqrt(diff[0] * diff[0] + diff[1] * diff[1])

            if dist < closest:
                closest = dist
                closestVec = diff
                self.t_closest = index

        return closestVec

    def check_collision(self, targets):
        closest = targets[self.t_closest]
        diff = [self.position[0] - closest.position[0],
                self.position[1] - closest.position[1]]
        dist = math.sqrt(diff[0] * diff[0] + diff[1] * diff[1])

        if dist < (c.game['s_target'] + c.game['s_agent']):
            return self.t_closest

        return -1
