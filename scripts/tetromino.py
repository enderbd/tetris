import pygame

from .settings import (
    CELL_SIZE,
    MOVE_DOWN_CD,
    MOVE_SIDES_CD,
    ROTATE_CD,
    TETROMINOS,
    NUM_COLS,
    NUM_ROWS,
)


class Tetromino(pygame.sprite.Sprite):
    def __init__(self, shape, row, column):
        if hasattr(self, "containers"):
            super().__init__("containers")
        else:
            super().__init__()

        self.shape = TETROMINOS[shape]
        self.rotate = 0
        self.rotate_cd = 0

        self.position = pygame.Vector2(column, row)
        self.move_down_cd = 0
        self.move_down_pressed_cd = 0
        self.move_sides_cd = 0

    def draw(self, screen):
        for point in self.shape[self.rotate]:
            local_x = (self.position.x + point[0]) * CELL_SIZE
            local_y = (self.position.y + point[1]) * CELL_SIZE
            pygame.draw.rect(
                screen, "black", ((local_x, local_y), (CELL_SIZE, CELL_SIZE))
            )

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.rotate_cd -= dt
        self.move_down_cd -= dt
        self.move_sides_cd -= dt
        self.move_down_pressed_cd -= dt

        if keys[pygame.K_UP]:
            if self.rotate_cd <= 0:
                self.rotate_piece()
        elif keys[pygame.K_LEFT]:
            if self.move_sides_cd <= 0:
                self.move_left()
        elif keys[pygame.K_RIGHT]:
            if self.move_sides_cd <= 0:
                self.move_right()
        elif keys[pygame.K_DOWN]:
            if self.move_down_pressed_cd <= 0:
                self.move_down(down_pressed=True)
        if self.move_down_cd <= 0:
            self.move_down()

    def rotate_piece(self):
        self.rotate_cd = ROTATE_CD
        if self.rotate + 90 == 360:
            self.rotate = 0
        else:
            self.rotate += 90

    def move_down(self, down_pressed=False):
        self.move_down_cd = MOVE_DOWN_CD
        self.move_down_pressed_cd = MOVE_SIDES_CD
        if self.get_top_edge() < NUM_ROWS - 1:
            self.position.y += 1

    def move_left(self):
        self.move_sides_cd = MOVE_SIDES_CD
        if self.get_left_edge() > 0:
            self.position.x -= 1

    def move_right(self):
        self.move_sides_cd = MOVE_SIDES_CD
        if self.get_right_edge() < NUM_COLS - 1:
            self.position.x += 1

    def get_left_edge(self):
        return self.position.x + min([point[0] for point in self.shape[self.rotate]])

    def get_right_edge(self):
        return self.position.x + max([point[0] for point in self.shape[self.rotate]])

    def get_width(self):
        return 1 + self.get_right_edge() - self.get_left_edge()

    def get_bottom_edge(self):
        return self.position.y + min([point[1] for point in self.shape[self.rotate]])

    def get_top_edge(self):
        return self.position.y + max([point[1] for point in self.shape[self.rotate]])

    def get_height(self):
        return 1 + self.get_top_edge() - self.get_bottom_edge()
