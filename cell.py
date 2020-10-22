import pygame


class Cell:
    def __init__(self, row, col, width):
        self.row, self.col = row, col
        self.x, self.y = self.row*width, self.col*width
        self.width = width
        self.value = 0
        self.color = (255, )*3
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def _col_from_val(self):
        self.color = ((-self.value + 1)*255, )*3

    def fill(self, radius, x, y):
        dist = (abs(self.x + self.width/2 - x)**2 + abs(self.y + self.width/2 - y)**2)**0.5
        if dist <= radius:
            dist = -dist + radius
            self.value += (dist / (radius*5)) * self.vel

        self.value = min(1, self.value)
        self._col_from_val()

    def erase(self, radius, x, y):
        dist = (abs(self.x + self.width / 2 - x) ** 2 + abs(self.y + self.width / 2 - y) ** 2) ** 0.5
        if dist <= radius:
            dist = -dist + radius
            self.value -= (dist / (radius*5)) * self.vel

        self.value = max(0, self.value)
        self._col_from_val()
