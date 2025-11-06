import pygame

from .settings import CELL_SIZE, NUM_COLS, NUM_ROWS
from .tetromino import Tetromino


class Board:
    def __init__(self, offset):
        self.rows = NUM_ROWS
        self.columns = NUM_COLS
        self.cell_size = CELL_SIZE
        self.width = self.columns * self.cell_size
        self.height = self.rows * self.cell_size
        self.offset = pygame.Vector2(offset)
        self.board_rect = pygame.Rect(self.offset, (self.width, self.height))
        self.board_surface = pygame.Surface(self.board_rect.size, pygame.SRCALPHA)
        self.board_color = (100, 100, 100, 200)
        self.line_color = (255, 255, 255, 100)
        print(f"Board initialized: (w, h) = ({self.width}, {self.height})")
        self.rotate = 0
        self.rotate_timer = 0
        self.moving_tetromino = None

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

    def draw_cells(self, screen):
        for i in range(1, self.rows):
            pygame.draw.line(
                screen,
                self.line_color,
                (0, self.cell_size * i),
                (self.width, self.cell_size * i),
                1,
            )
        for i in range(1, self.columns):
            pygame.draw.line(
                screen,
                self.line_color,
                (self.cell_size * i, 0),
                (self.cell_size * i, self.height),
                1,
            )

    def draw(self, screen):
        self.board_surface.fill(self.board_color)
        if self.moving_tetromino:
            self.moving_tetromino.draw(self.board_surface)
        self.draw_border(self.board_surface)
        self.draw_cells(self.board_surface)
        screen.blit(self.board_surface, self.offset)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            self.spawn_tetromino()
        if self.moving_tetromino:
            self.moving_tetromino.update(dt)

    def spawn_tetromino(self):
        self.moving_tetromino = Tetromino(shape="T", row=0, column=5)
