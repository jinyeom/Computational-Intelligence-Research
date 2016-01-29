# game.py
import pygame
import math
import time
import util
import config as c
from agent import Agent as A
from target import Target as T
from neural_network import NNetwork as NNet

class Game:
    def __init__(self, p=["0000"], manual=True):
        # pygame setup
        pygame.init()
        pygame.display.set_caption(c.game['g_name'])

        self.clock      = pygame.time.Clock()
        self.display    = pygame.display.set_mode(
                            (c.game['width'], c.game['height']))

        # game setup
        if manual:
            self.agents = [A(0, NNet(p[0]))]

        else:
            self.agents = [A(i, NNet(p[i])) for i in range(c.game['n_agents'])]

        self.targets    = [T() for _ in range(c.game['n_targets'])]
        self.generation = 0

        # save terminal
        print "\033[?47h"

    def game_loop(self, display=True, manual=True):
        for i in range(c.game['g_time']):

            self.game_logic(manual)

            if i % c.game['delay'] == 0: self.update_terminal()
            if display: self.process_graphic()

        return [a.fitness for a in self.agents]

    def game_test(self):
        self.agents = [A(0, NNet("0000"))]
        self.agents[0].position = [c.game['width']/2, 0]
        self.agents[0].track = [0, 0]
        self.agents[0].rotation = 0.0

        for i in range(c.game['t_time'] / 10):
            self.agents[0].track = [1., 1.]
            self.game_logic(True)

            if i % c.game['delay'] == 0: self.update_terminal()
            self.process_graphic()

        for i in range(c.game['t_time'] / 10):
            self.agents[0].track = [1.01, 0.99]
            self.game_logic(True)

            if i % c.game['delay'] == 0: self.update_terminal()
            self.process_graphic()

        for i in range(c.game['t_time'] / 10):
            self.agents[0].track = [1.02, 0.98]
            self.game_logic(True)

            if i % c.game['delay'] == 0: self.update_terminal()
            self.process_graphic()

        for i in range(c.game['t_time'] / 10):
            self.agents[0].track = [1.03, 0.97]
            self.game_logic(True)

            if i % c.game['delay'] == 0: self.update_terminal()
            self.process_graphic()

        for i in range(c.game['t_time'] / 10):
            self.agents[0].track = [1.04, 0.96]
            self.game_logic(True)

            if i % c.game['delay'] == 0: self.update_terminal()
            self.process_graphic()

        for i in range(c.game['t_time'] / 10):
            self.agents[0].track = [0.99, 1.01]
            self.game_logic(True)

            if i % c.game['delay'] == 0: self.update_terminal()
            self.process_graphic()

        for i in range(c.game['t_time'] / 10):
            self.agents[0].track = [0.98, 1.02]
            self.game_logic(True)

            if i % c.game['delay'] == 0: self.update_terminal()
            self.process_graphic()

        for i in range(c.game['t_time'] / 10):
            self.agents[0].track = [0.97, 1.03]
            self.game_logic(True)

            if i % c.game['delay'] == 0: self.update_terminal()
            self.process_graphic()

        for i in range(c.game['t_time'] / 10):
            self.agents[0].track = [0.96, 1.04]
            self.game_logic(True)

            if i % c.game['delay'] == 0: self.update_terminal()
            self.process_graphic()

    def game_logic(self, manual):
        for a in self.agents:

            if manual: a.control()
            else: a.update(self.targets)

            if a.check_collision(self.targets) != -1:
                self.targets[a.t_closest].reset()
                a.fitness += 1

        self.agents = util.quicksort(self.agents)

    def process_graphic(self):
        self.display.fill((0xff, 0xff, 0xff))

        for t in self.targets:
            t_img = pygame.image.load(c.image['target']).convert_alpha()
            self.display.blit(t_img, (t.position[0], t.position[1]))

        if len(self.agents) == c.game['n_agents']:
            for i in range(c.game['n_best']):
                a_img = pygame.transform.rotate(
                    pygame.image.load(c.image['best']).convert_alpha(),
                    self.agents[i].rotation * -180 / math.pi)
                self.display.blit(a_img, (self.agents[i].position[0],
                                        self.agents[i].position[1]))

            for i in range(c.game['n_best'], c.game['n_agents']):
                a_img = pygame.transform.rotate(
                    pygame.image.load(c.image['agent']).convert_alpha(),
                    self.agents[i].rotation * -180 / math.pi)
                self.display.blit(a_img, (self.agents[i].position[0],
                                        self.agents[i].position[1]))
        else:
            for a in self.agents:
                a_img = pygame.transform.rotate(
                    pygame.image.load(c.image['best']).convert_alpha(),
                                    a.rotation * -180 / math.pi)
                self.display.blit(a_img, (a.position[0], a.position[1]))

        pygame.display.update()
        self.clock.tick(c.game['fps'])

    def update_terminal(self):
        print "\033[2J\033[H",
        print c.game['g_name'],
        print "\tGEN.: " + str(self.generation),
        print "\tTIME: " + str(time.clock()) + '\n'

        for a in self.agents:
            print "AGENT " + repr(a.number).rjust(2) + ": ",
            print "X: " + repr(a.position[0]).rjust(20),
            print "Y: " + repr(a.position[1]).rjust(20),
            print "FITN.:" + repr(a.fitness).rjust(5)

if __name__ == '__main__':
    g = Game()
    g.game_test()
    g.game_loop()
    pygame.quit()
