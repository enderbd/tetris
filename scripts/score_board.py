import pygame


class ScoreBoard:
    def __init__(self, offset, leveled_event):
        self.offset = offset
        self.score_font = pygame.font.SysFont("jetbrainsmononerdfont", 20)
        self.score = 0
        self.level_font = pygame.font.SysFont("jetbrainsmononerdfont", 20)
        self.level = 0
        self.level_incease_lines = 7
        self.total_lines = 0
        self.leveled_event = leveled_event
        self.width = 200
        self.height = 100
        self.score_board_surface = pygame.Surface((self.width, self.height))
        self.board_color = (100, 100, 100, 200)
        self.line_color = (255, 255, 255, 100)

    def draw_border(self, screen):
        pygame.draw.line(
            self.score_board_surface, self.line_color, (0, 0), (self.width, 0), 2
        )
        pygame.draw.line(
            self.score_board_surface,
            self.line_color,
            (self.width - 2, 0),
            (self.width - 2, self.height),
            2,
        )
        pygame.draw.line(
            self.score_board_surface,
            self.line_color,
            (self.width - 2, self.height - 2),
            (0, self.height - 2),
            2,
        )
        pygame.draw.line(
            self.score_board_surface, self.line_color, (0, self.height), (0, 0), 2
        )

    def draw(self, screen):
        self.draw_border(screen)
        self.score_board_surface.fill(self.board_color)

        level_text = self.level_font.render(f"Level: {self.level}", 1, "black")
        score_text = self.score_font.render(f"Score: {self.score}", 1, "black")
        self.score_board_surface.blit(
            level_text, ((self.width - level_text.get_width()) // 2, 20)
        )
        self.score_board_surface.blit(
            score_text, ((self.width - score_text.get_width()) // 2, 50)
        )

        screen.blit(self.score_board_surface, self.offset)

    def update(self, cleared_rows):
        for row in range(cleared_rows):
            self.score += 100
        self.total_lines += cleared_rows
        if self.total_lines > self.level_incease_lines:
            self.level += 1
            pygame.event.post(pygame.event.Event(self.leveled_event))
