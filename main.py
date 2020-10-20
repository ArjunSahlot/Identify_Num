import pygame, os
from constants import *


# Window Management
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (screen_width//2-WIDTH//2, screen_height//2-HEIGHT//2)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Identify_Num, By: ArjunSahlot")


def draw_window(win):
    win.fill(WHITE)


def main(win, width, height):
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        draw_window(win)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
                # exit()
        pygame.display.update()


main(WINDOW, WIDTH, HEIGHT)
