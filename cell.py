#
#  Identify num
#  An AI that can recognize the number you draw. Made using pygame and tensorflow
#  Copyright Arjun Sahlot 2021
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

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
        dist = (abs(self.x + self.width/2 - x)**2 + abs(self.y + self.width/2 - y)**2)
        if dist <= radius**2:
            dist = -dist**0.5 + radius
            self.value += (dist / (radius*5)) * self.vel

        self.value = min(1, self.value)
        self._col_from_val()

    def erase(self, radius, x, y):
        dist = (abs(self.x + self.width / 2 - x) ** 2 + abs(self.y + self.width / 2 - y) ** 2)
        if dist <= radius**2:
            dist = -dist**0.5 + radius
            self.value -= (dist / (radius*5)) * self.vel

        self.value = max(0, self.value)
        self._col_from_val()
