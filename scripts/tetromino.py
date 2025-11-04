import pygame

from .settings import CELL_SIZE, MOVE_DOWN_CD, ROTATE_CD, TETROMINOS


class Tetromino(pygame.sprite.Sprite):
    def __init__(self, shape, row, column):
        if hasattr(self, "containers"):
            super().__init__("containers")
        else:
            super().__init__()

        self.shape = TETROMINOS[shape]
        self.rotate = 0
        self.rotate_timer = 0
        self.position = pygame.Vector2(row * CELL_SIZE, column * CELL_SIZE)
        self.move_down_cd = 0

    def draw(self, screen):
        for point in self.shape[self.rotate]:
            local_x = self.position.x + point[0] * CELL_SIZE
            local_y = self.position.y + point[1] * CELL_SIZE
            pygame.draw.rect(
                screen, "black", ((local_x, local_y), (CELL_SIZE, CELL_SIZE))
            )

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.rotate_timer -= dt
        self.move_down_cd -= dt
        if keys[pygame.K_UP]:
            if self.rotate_timer <= 0:
                self.rotate_piece()
        if self.move_down_cd <= 0:
            self.move(dt)

    def rotate_piece(self):
        self.rotate_timer = ROTATE_CD
        if self.rotate + 90 == 360:
            self.rotate = 0
        else:
            self.rotate += 90

    def move(self, dt):
        self.move_down_cd = MOVE_DOWN_CD
        self.position.y += CELL_SIZE
