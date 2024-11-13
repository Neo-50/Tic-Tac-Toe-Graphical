import pygame


class Settings:
    """A class to store all settings for Rotating Right Triangle."""

    def __init__(self):
        """Initialize the game's static settings."""

        # Set the dimensions of the window
        self.width, self.height = 600, 600

        # Create the window
        self.window = pygame.display.set_mode((self.width, self.height))

        # Set the color of the lines
        self.colors = {
            'black': (0, 0, 0),
            'green': (0, 255, 0),
            'blue': (0, 0, 255),
            'red': (255, 0, 0),
            'white': (255, 255, 255)
        }

        # Vertical lines
        self.line1_start_x, self.line1_start_y = self.width // 3, 0
        self.line1_end_x, self.line1_end_y = self.width // 3, self.height

        self.line2_start_x, self.line2_start_y = 2 * self.width // 3, 0
        self.line2_end_x, self.line2_end_y = 2 * self.width // 3, self.height

        # Horizontal lines
        self.line3_start_x, self.line3_start_y = 0, self.height // 3
        self.line3_end_x, self.line3_end_y = self.width, self.height // 3

        self.line4_start_x, self.line4_start_y = 0, 2 * self.height // 3
        self.line4_end_x, self.line4_end_y = self.width, 2 * self.height // 3
