import pygame
from settings import Settings
import functions as gf


def run_game():
    # Initialize pygame and settings
    pygame.init()
    tset = Settings()

    # Set the title of the window
    pygame.display.set_caption("Tic Tac Toe")

    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the window with black color
        tset.window.fill((0, 0, 0))

        # Draw the first line for the game grid
        gf.draw_objects(tset.window, tset.colors, tset.line1_start_x,
                        tset.line1_start_y, tset.line1_end_x,
                        tset.line1_end_y)

        # Draw the second line for the game grid
        gf.draw_objects(tset.window, tset.colors, tset.line2_start_x,
                        tset.line2_start_y, tset.line2_end_x,
                        tset.line2_end_y)

        # Draw the third line for the game grid
        gf.draw_objects(tset.window, tset.colors, tset.line3_start_x,
                        tset.line3_start_y, tset.line3_end_x,
                        tset.line3_end_y)

        # Draw the fourth line for the game grid
        gf.draw_objects(tset.window, tset.colors, tset.line4_start_x,
                        tset.line4_start_y, tset.line4_end_x, tset.line4_end_y)

        # Update the display
        pygame.display.flip()

        # Set the framerate
        pygame.time.Clock().tick(30)

run_game()
