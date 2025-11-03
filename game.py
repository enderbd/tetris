import pygame

from scripts.board import Board
from scripts.settings import FPS, SCREEN_HEIGHT, SCREEN_WIDTH


class TetrisGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Tetris project")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        Board.containers = (self.updatable, self.drawable)

        self.game_board = Board(offset=(20, 20))

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            self.screen.fill("black")
            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                self.running = False

            for s in self.drawable:
                s.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(FPS)


if __name__ == "__main__":
    TetrisGame().run()
