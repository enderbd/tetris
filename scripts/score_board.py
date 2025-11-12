import pygame


class ScoreBoard:
    def __init__(self, offset, leveled_event):
        self.offset = offset
        self.score_font = pygame.font.SysFont("jetbrainsmononerdfont", 20)
        self.level_font = pygame.font.SysFont("jetbrainsmononerdfont", 20)
        self.total_lines_font = pygame.font.SysFont(
            "jetbrainsmononerdfont", 20)
        self.level = 0
        self.score = 0
        self.lines_to_level = 10
        self.total_lines = 0
        self.leveled_event = leveled_event
        self.width = 200
        self.height = 140
        self.score_board_surface = pygame.Surface(
            (self.width, self.height), pygame.SRCALPHA
        )
        self.board_color = (100, 100, 100, 200)
        self.line_color = (255, 255, 255, 100)

    def draw_border(self, screen):
        pygame.draw.line(
            self.score_board_surface, self.line_color, (
                0, 0), (self.width, 0), 2
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
            self.score_board_surface, self.line_color, (
                0, self.height), (0, 0), 2
        )

    def draw(self, screen):
        self.draw_border(screen)
        self.score_board_surface.fill(self.board_color)

        level_text = self.level_font.render(f"Level: {self.level}", 1, "black")
        score_text = self.score_font.render(f"Score: {self.score}", 1, "black")
        total_lines_text = self.score_font.render(
            f"Lines: {self.total_lines}", 1, "black"
        )
        self.score_board_surface.blit(
            level_text, ((self.width - level_text.get_width()) // 2, 10)
        )
        self.score_board_surface.blit(
            score_text, ((self.width - score_text.get_width()) // 2, 50)
        )
        self.score_board_surface.blit(
            total_lines_text, ((
                self.width - total_lines_text.get_width()) // 2, 90)
        )

        screen.blit(self.score_board_surface, self.offset)

    def update(self, cleared_rows):
        for row in range(cleared_rows):
            self.score += 100
        self.total_lines += cleared_rows
        if self.total_lines % self.lines_to_level == 0:
            print("Should level up!")
            self.level += 1
            pygame.event.post(pygame.event.Event(self.leveled_event))
