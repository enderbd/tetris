import pygame
from .tetromino import Tetromino


class NextTetroBoard:
    def __init__(self, offset):
        self.next_tetros = []
        self.offset = offset
        self.width = 200
        self.height = 420
        self.board_surface = pygame.Surface(
            (self.width, self.height), pygame.SRCALPHA)
        self.board_color = (100, 100, 100, 200)
        self.line_color = (255, 255, 255, 100)

    def draw_border(self, screen):
        pygame.draw.line(
            self.board_surface, self.line_color, (0, 0), (self.width, 0), 2
        )
        pygame.draw.line(
            self.board_surface,
            self.line_color,
            (self.width - 2, 0),
            (self.width - 2, self.height),
            2,
        )
        pygame.draw.line(
            self.board_surface,
            self.line_color,
            (self.width - 2, self.height - 2),
            (0, self.height - 2),
            2,
        )
        pygame.draw.line(
            self.board_surface, self.line_color, (0, self.height), (0, 0), 2
        )

    def draw(self, screen, tetrominos):
        self.draw_border(screen)
        self.board_surface.fill(self.board_color)
        prev_y = 3
        for i, t in enumerate(tetrominos[:]):
            local_tetro = Tetromino(shape=t.letter)
            local_tetro.move_left(2)
            local_tetro.move_down(prev_y)
            prev_y = local_tetro.center.y + 4
            local_tetro.draw(self.board_surface)

        screen.blit(self.board_surface, self.offset)

    def update(self, cleared_rows):
        for row in range(cleared_rows):
            self.score += 100
        self.total_lines += cleared_rows
        if self.total_lines % self.lines_to_level == 0:
            print("Should level up!")
            self.level += 1
