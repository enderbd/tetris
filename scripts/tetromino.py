import pygame
from .timer import Cooldown

from .settings import (
    CELL_SIZE,
    MOVE_DOWN_CD,
    MOVE_SIDES_CD,
    NUM_COLS,
    NUM_ROWS,
    ROTATE_CD,
    TETROMINOS,
)


class Tetromino:
    def __init__(self, shape):
        self.shape = TETROMINOS[shape]
        self.rotate = 0

        self.center = pygame.Vector2(NUM_COLS // 2, -1)
        # we need a lot of cooldowns due to how the pieces move in this game,
        self.move_down_auto_timer = Cooldown(500, repeat=True)
        self.move_down_auto_timer.activate()
        self.move_down_pressed_timer = Cooldown(50, repeat=True)
        self.move_down_pressed_timer.activate()
        self.move_sides_timer = Cooldown(50, repeat=True)
        self.move_sides_timer.activate()
        self.rotate_timer = Cooldown(150, repeat=True)
        self.rotate_timer.activate()

        self.blocks = [Block(pos + self.center) for pos in self.shape[self.rotate]]

    def draw(self, screen):
        for block in self.blocks:
            block.draw(screen)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            if not self.rotate_timer.is_active():
                self.rotate_piece()
        elif keys[pygame.K_LEFT]:
            if not self.move_sides_timer.is_active():
                self.move_left()
        elif keys[pygame.K_RIGHT]:
            if not self.move_sides_timer.is_active():
                self.move_right()
        elif keys[pygame.K_DOWN]:
            if not self.move_down_pressed_timer.is_active():
                self.move_down()
        if not self.move_down_auto_timer.is_active():
            self.move_down()

    def rotate_piece(self):
        if self.rotate + 90 == 360:
            self.check_and_adjust_center(0)
            self.rotate = 0
        else:
            self.check_and_adjust_center(self.rotate + 90)
            self.rotate += 90
        self.rotate_blocks()

    def rotate_blocks(self):
        for i, block in enumerate(self.blocks):
            block.pos = self.center + self.shape[self.rotate][i]

    def check_and_adjust_center(self, future_rotate):
        # check the future rotation when against left or right board edge
        # if by rotation the piece goes out, we push it back in
        temp_rotation = self.shape[future_rotate]
        left_edge = self.center.x + min([point[0] for point in temp_rotation])
        if left_edge < 0:
            self.center.x -= left_edge
            for block in self.blocks:
                block.pos.x -= left_edge
        right_edge = self.center.x + max([point[0] for point in temp_rotation])
        if right_edge > NUM_COLS - 1:
            self.center.x -= right_edge - NUM_COLS + 1
            for block in self.blocks:
                block.pos.x = self.center.x

    def move_down(self, down_pressed=False):
        if self.get_top_edge() < NUM_ROWS - 1:
            self.center.y += 1
            for block in self.blocks:
                block.pos.y += 1

    def move_left(self):
        if self.get_left_edge() > 0:
            self.center.x -= 1
            for block in self.blocks:
                block.pos.x -= 1

    def move_right(self):
        if self.get_right_edge() < NUM_COLS - 1:
            self.center.x += 1
            for block in self.blocks:
                block.pos.x += 1

    def get_left_edge(self):
        return self.center.x + min([point[0] for point in self.shape[self.rotate]])

    def get_right_edge(self):
        return self.center.x + max([point[0] for point in self.shape[self.rotate]])

    def get_width(self):
        return 1 + self.get_right_edge() - self.get_left_edge()

    def get_bottom_edge(self):
        return self.center.y + min([point[1] for point in self.shape[self.rotate]])

    def get_top_edge(self):
        return self.center.y + max([point[1] for point in self.shape[self.rotate]])

    def get_height(self):
        return 1 + self.get_top_edge() - self.get_bottom_edge()


class Block:
    def __init__(self, pos, color="black"):
        # we spawn the pieces middle top
        self.color = color
        self.pos = pygame.Vector2(pos)

    def draw(self, screen):
        pygame.draw.rect(
            screen, self.color, (self.pos * CELL_SIZE, (CELL_SIZE, CELL_SIZE))
        )

    def update(self):
        pass
        # self.block_rect.topleft = self.pos * CELL_SIZE
