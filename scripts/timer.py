from pygame.time import get_ticks


class Cooldown:
    def __init__(self, duration, repeat=False):
        self.duration = duration
        self.active = False
        self.start_time = 0
        self.repeat = repeat

    def activate(self):
        self.active = True
        self.start_time = get_ticks()

    def is_active(self):
        if get_ticks() - self.start_time >= self.duration:
            self.active = False
            self.start_time = 0
            if self.repeat:
                self.activate()
            return False
        return True
