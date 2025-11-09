import pygame


class Grid:
    def __init__(self, rows, columns, cell_size):
        self.rows = rows
        self.columns = columns
        self.cell_size = cell_size
        self.matrix = [[0 for i in range(columns)] for j in range(rows)]
        # self.matrix[self.rows - 1] = [1 for _ in range(self.columns)]

    def is_block_inside(self, block_row, block_column):
        if 0 <= block_row < self.rows and 0 <= block_column < self.columns:
            return True
        return False

    def draw(self, screen):
        for r in range(self.rows):
            for c in range(self.columns):
                if self.matrix[r][c] == 1:
                    top_left = pygame.Vector2(c, r) * self.cell_size
                    pygame.draw.rect(
                        screen,
                        "black",
                        (top_left, (self.cell_size, self.cell_size)),
                    )

    def add_tetromino(self, tetromino):
        for block in tetromino.blocks:
            self.matrix[int(block.pos.y)][int(block.pos.x)] = 1

    def is_colliding(self, row, col):
        # print(f"({row}, {col} :{self.matrix[row][col]} )")
        if 0 <= row < self.rows and 0 <= col < self.columns:
            if self.matrix[row][col] == 1:
                return True
        return False

    def __repr__(self):
        grid_string = ""
        for r in range(self.rows):
            for c in range(self.columns):
                grid_string += f"{self.matrix[r][c]} "
            grid_string += "\n"
        return grid_string
