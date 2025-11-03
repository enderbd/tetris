import pygame
from constants import *


class TetrisGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Tetris project")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            self.screen.fill("grey")

            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                self.running = False

            self.clock.tick(FPS)


if __name__ == "__main__":
    TetrisGame().run()
