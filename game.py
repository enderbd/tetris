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

        # custom timers
        self.move_down_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.move_down_timer, 1000)
        self.move_sides_timer = pygame.USEREVENT + 2
        pygame.time.set_timer(self.move_sides_timer, 50)
        self.rotate_timer = pygame.USEREVENT + 3
        pygame.time.set_timer(self.rotate_timer, 200)
        # timer based conditionals
        self.can_move_down = True
        self.can_move_sides = True
        self.can_rotate = True

        self.game_board = Board(offset=(20, 20))

    def run(self):
        dt = 0
        while self.running:
            self.process_events()
            self.process_keys()

            self.screen.fill("black")
            self.game_board.run(dt, self.screen)

            pygame.display.flip()
            dt = self.clock.tick(FPS) / 1000

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(1)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    pygame.time.set_timer(self.move_down_timer, 50)
                if event.key == pygame.K_n:
                    self.game_board.spawn_tetromino()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    pygame.time.set_timer(self.move_down_timer, 300)
            if event.type == self.move_down_timer:
                self.can_move_down = True
                self.game_board.move_down()
            if event.type == self.move_sides_timer:
                self.can_move_sides = True
            if event.type == self.rotate_timer:
                self.can_rotate = True

    def process_keys(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_q]:
            self.running = False

        if keys[pygame.K_DOWN]:
            if self.can_move_down:
                self.game_board.move_down()
                self.can_move_down = False
        elif keys[pygame.K_UP]:
            if self.can_rotate:
                self.game_board.rotate()
                self.can_rotate = False
        if self.can_move_sides:
            self.can_move_sides = False
            if keys[pygame.K_LEFT]:
                self.game_board.move_left()
            elif keys[pygame.K_RIGHT]:
                self.game_board.move_right()


if __name__ == "__main__":
    TetrisGame().run()
