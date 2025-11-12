import random

import pygame

from scripts.score_board import ScoreBoard
from scripts.next_tetros_board import NextTetroBoard
from .grid import Grid
from .settings import CELL_SIZE, NUM_COLS, NUM_ROWS, TETROMINOS
from .tetromino import Tetromino


class Board:
    def __init__(self, offset, leveled_event):
        self.rows = NUM_ROWS
        self.columns = NUM_COLS
        self.cell_size = CELL_SIZE
        self.width = self.columns * self.cell_size
        self.height = self.rows * self.cell_size
        self.offset = pygame.Vector2(offset)
        self.board_surface = pygame.Surface(
            (self.width, self.height), pygame.SRCALPHA)
        self.board_color = (100, 100, 100, 200)
        self.line_color = (255, 255, 255, 100)

        self.letters = [k for k in TETROMINOS]
        self.moving_tetromino = self.get_random_tetromino()
        self.next_tetromimos = []
        self.generate_tetros_list()
        self.temp_current_shape = 0

        self.grid = Grid(NUM_ROWS, NUM_COLS, CELL_SIZE)
        self.next_tetros_board = NextTetroBoard(offset=(340, 200))
        self.score_board = ScoreBoard(
            offset=(340, 20), leveled_event=leveled_event)

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

    def run(self, dt, screen):
        self.draw(screen)

    def draw(self, screen):
        self.board_surface.fill(self.board_color)
        self.moving_tetromino.draw(self.board_surface)
        self.grid.draw(self.board_surface)
        self.draw_border(self.board_surface)
        self.draw_cells(self.board_surface)

        self.score_board.draw(screen)
        self.next_tetros_board.draw(screen, self.next_tetromimos)
        screen.blit(self.board_surface, self.offset)

    def move_left(self):
        if not self.next_move_collides(0, -1):
            self.moving_tetromino.move_left()

    def move_right(self):
        if not self.next_move_collides(0, 1):
            self.moving_tetromino.move_right()

    def move_down(self):
        if not self.next_move_collides(1, 0) and not self.moving_tetromino.landed:
            self.moving_tetromino.move_down()
        else:
            self.tetromino_landed()

    def tetromino_landed(self):
        self.grid.add_tetromino(self.moving_tetromino)
        self.moving_tetromino = self.get_next_tetromino()
        cleared_rows = self.grid.get_completed_rows()
        # print(self.grid)
        if cleared_rows > 0:
            self.score_board.update(cleared_rows)

    def next_move_collides(self, row_offset, column_offset):
        # print(f"top_edge {self.moving_tetromino.get_bottom_edge()} ")
        temp_blocks = [block for block in self.moving_tetromino.blocks[:]]
        for block in temp_blocks:
            next_y = block.pos.y + row_offset
            next_x = block.pos.x + column_offset
            # print(f"next x :{self.moving_tetromino.letter} {next_x}")
            if next_y < self.rows and 0 <= next_x < self.columns:
                if self.grid.is_colliding(int(next_y), int(next_x)):
                    # print(f"block with pos {block.pos} is colliding")
                    return True
        return False

    def rotate(self):
        self.moving_tetromino.rotate_piece()

    def generate_tetros_list(self):
        for i in range(3):
            self.next_tetromimos.append(self.get_random_tetromino())

    def get_next_tetromino(self):
        tetro = self.next_tetromimos.pop(0)
        self.next_tetromimos.append(self.get_random_tetromino())
        return tetro

    def get_random_tetromino(self):
        if len(self.letters) == 0:
            self.letters = [k for k in TETROMINOS]
        random_shape = random.choice(self.letters)
        self.letters.remove(random_shape)
        return Tetromino(shape=random_shape)
