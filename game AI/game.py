import pygame
import math
import time
import util
import config
from agent import Agent
from target import Target
from neural_network import NNet

class Game:
    def __init__(self):
        # pygame setup
        pygame.init()
        pygame.display.set_caption(config.game['g_name'])
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode(
                (config.game['width'], config.game['height']))

        # game setup
        self.agents = [Agent(NNet()) for _ in range(config.game['n_agents'])]
        self.targets = [Target() for _ in range(config.game['n_targets'])]

        # save terminal
        print "\033[?47h"

    def game_loop(self, display=False):
        for i in range(config.game['g_time']):

            for event in pygame.event.get():
                if event.type == pygame.QUIT: break

            self.game_logic()

            if i % config.game['delay'] == 0: self.update_terminal()
            if display: self.process_graphic()

            self.clock.tick(config.game['fps'])

        pygame.quit()
        return [a.fitness for a in self.agents]

    def game_logic(self):
        for a in self.agents:
            a.update(self.targets)

            if a.check_collision(self.targets) != -1:
                self.targets[a.t_closest].reset()
                a.fitness += 1

        self.agents = util.quicksort(self.agents)

    def process_graphic(self):
        self.display.fill((0xff, 0xff, 0xff))

        for t in self.targets:
            t_img = pygame.image.load(config.image['target']).convert_alpha()
            self.display.blit(t_img, (t.position[0], t.position[1]))

        for a in self.agents:
            a_img = pygame.transform.rotate(
                pygame.image.load(config.image['agent']).convert_alpha(),
                a.rotation * -180 / math.pi)
            self.display.blit(a_img, (a.position[0], a.position[1]))

        pygame.display.update()

    def update_terminal(self):
        print "\033[2J\033[H"
        print "\t" + config.game['g_name'],
        print "\tTIME: " + str(time.clock()) + '\n'

        for i, a in enumerate(self.agents):
            print "AGENT " + repr(i).rjust(2) + ": ",
            print "X: " + repr(a.position[0]).rjust(20),
            print "Y: " + repr(a.position[1]).rjust(20),
            print "FITN.:" + repr(a.fitness).rjust(4)

if __name__ == '__main__':
    g = Game()
    g.game_loop()
