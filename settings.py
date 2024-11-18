import pygame


class Settings:
    """A class to store all settings for Tic Tac Toe Graphical."""

    def __init__(self):
        """Initialize the game's static settings."""

        # Set the dimensions of the window
        self.width, self.height = 600, 600

        # Create the window
        self.window = pygame.display.set_mode((self.width, self.height))

        # Grid state: 3x3 matrix to track Xs and Os
        self.board = [[None for _ in range(3)] for _ in range(3)]

        # Set the color of the lines
        self.colors = {
            'blue': (0, 0, 255),
            'red': (255, 0, 0),
            'white': (255, 255, 255)
        }

        # Create a font for the text
        self.font = pygame.font.SysFont(None, 200)

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
