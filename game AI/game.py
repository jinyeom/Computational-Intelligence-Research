import pygame
import math
import random
from agent import Agent
from target import Target

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

    def game_loop(self, display=False):
        for i in range(config.game['g_time']):

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break

            self.game_logic()
            self.update_terminal()

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

    def process_graphic(self):
        for t in self.targets:
            t_img = pygame.transform.rotate(
                pygame.image.load(config.image['agent']).convert_alpha(),
                a.rotation * -180 / math.pi)
            self.display.blit(t_img, (self.a.position[0], self.a.position[1]))

        for a in self.agents:
            a_img = pygame.transform.rotate(
                pygame.image.load(config.image['agent']).convert_alpha(),
                a.rotation * -180 / math.pi)
            self.display.blit(a_img, (self.a.position[0], self.a.position[1]))

        pygame.display.update()

    def update_terminal(self):


if __name__ == '__main__':
    g = Game()
    g.game_loop()
