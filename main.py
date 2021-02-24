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

from tkinter import Tk, messagebox
Tk().withdraw()
import pygame
import tensorflow as tf

from cell import Cell
from constants import *
from identifier import get_num


# Window Management
WINDOW = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Identify Num")


def draw_window(win, canvas):
    win.fill(WHITE)
    for row in canvas:
        for cell in row:
            cell.draw(win)


def create_canvas(res):
    canvas = []
    width = WIDTH//res
    for i in range(res):
        canvas.append([])
        for j in range(res):
            canvas[i].append(Cell(i, j, width))

    return canvas


def get_vals(canvas):
    values = []

    for i in range(len(canvas)):
        values.append([])
        for j in range(len(canvas)):
            values[i].append(canvas[j][i].value)

    return tf.convert_to_tensor([values])


def main(win, width):
    clock = pygame.time.Clock()
    res = RESOLUTION
    canvas = create_canvas(res)
    pygame.mouse.set_visible(False)
    radius = 30

    while True:
        clock.tick(FPS)
        draw_window(win, canvas)
        pygame.draw.circle(win, BLACK, pygame.mouse.get_pos(), radius, 3)

        if pygame.mouse.get_pressed()[0]:
            for row in canvas:
                for cell in row:
                    cell.fill(radius, *pygame.mouse.get_pos())

        if pygame.mouse.get_pressed()[2]:
            for row in canvas:
                for cell in row:
                    cell.erase(radius, *pygame.mouse.get_pos())

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    radius -= 3
                    radius = max(radius, 5)
                if event.button == 5:
                    radius += 3
                    radius = min(radius, 600)

            if event.type == pygame.KEYDOWN:
                messagebox.showinfo("Prediction", f"The computer predicted {get_num(get_vals(canvas))}")

        pygame.display.update()


if __name__ == "__main__":
    main(WINDOW, WIDTH)
