import pygame


class Board(pygame.sprite.Sprite):
    def __init__(self, rows, columns, cell_size, position):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.rows = rows
        self.columns = columns
        self.cell_size = cell_size
        self.width = columns * cell_size
        self.height = rows * cell_size
        self.position = pygame.Vector2(position)
        self.board_rect = pygame.Rect(self.position, (self.width, self.height))
        self.line_color = (255, 255, 255, 50)
        print(f"Board initialized: (w, h) = ({self.width}, {self.height})")

    def draw_border(self, screen):
        x = self.position.x
        y = self.position.y
        pygame.draw.line(screen, self.line_color, (x, y), (x + self.width, y), 2)
        pygame.draw.line(
            screen,
            self.line_color,
            (x + self.width, y),
            (x + self.width, y + self.height),
            2,
        )
        pygame.draw.line(
            screen,
            self.line_color,
            (x + self.width, y + self.height),
            (x, y + self.height),
            2,
        )
        pygame.draw.line(screen, self.line_color, (x, y + self.height), (x, y), 2)

    def draw_cells(self, screen):
        for i in range(1, self.rows):
            pygame.draw.line(
                screen,
                self.line_color,
                (self.position.x, self.position.y + self.cell_size * i),
                (self.position.x + self.width, self.position.y + self.cell_size * i),
                1,
            )
        for i in range(1, self.columns):
            pygame.draw.line(
                screen,
                self.line_color,
                (self.position.x + self.cell_size * i, self.position.y),
                (self.position.x + self.cell_size * i, self.position.y + self.height),
                1,
            )

    def draw(self, screen):
        # board_surf = pygame.Surface(self.board_rect.size, pygame.SRCALPHA)

        self.draw_border(screen)
        self.draw_cells(screen)
        # screen.blit(board_surf, self.board_rect)

    def update(self, screen):
        pass
