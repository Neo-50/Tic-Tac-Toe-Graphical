import pygame


def draw_objects(window, colors, lineonetop_x, lineonetop_y, lineonebottom_x,
                 lineonebottom_y):
    # Draw the first line
    pygame.draw.line(window, colors['white'], (lineonetop_x, lineonetop_y),
                     (lineonebottom_x, lineonebottom_y))
