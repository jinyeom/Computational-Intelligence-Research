import pygame
import math
import random
from agent import Agent
from target import Target

class Game:
    def __init__(self):
        self.agents = [Agent(NNet()) for _ in range(config.game['n_agents'])]
        self.targets = [Target() for _ in range(config.game['n_targets'])]

    def game_loop(self):
