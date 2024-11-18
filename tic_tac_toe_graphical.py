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
    player_turn = True

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif player_turn:  # Only process player moves during their turn
                if gf.player_move(tset.board, tset.width, tset.height, event):
                    player_turn = False  # Switch to AI's turn if a move was made

        # AI's turn
        if not player_turn:  # Process AI logic only once per frame
            gf.ai_move(tset.board)
            player_turn = True  # Switch back to player's turn

        # Check for a winner or tie
        if gf.victory(tset.board):
            print("Game Over! Winner detected.")
            running = False
        elif all(all(cell is not None for cell in row) for row in tset.board):  # Check for tie
            print("Game Over! It's a tie.")
            running = False

        # Draw the board and game state
        tset.window.fill((0, 0, 0))
        gf.draw_lines(tset.window, tset.colors, tset.line1_start_x, tset.line1_start_y, tset.line1_end_x, tset.line1_end_y)
        gf.draw_lines(tset.window, tset.colors, tset.line2_start_x, tset.line2_start_y, tset.line2_end_x, tset.line2_end_y)
        gf.draw_lines(tset.window, tset.colors, tset.line3_start_x, tset.line3_start_y, tset.line3_end_x, tset.line3_end_y)
        gf.draw_lines(tset.window, tset.colors, tset.line4_start_x, tset.line4_start_y, tset.line4_end_x, tset.line4_end_y)

        for row in range(3):
            for col in range(3):
                if tset.board[row][col] == 'x':
                    gf.draw_x(tset.window, row, col, tset.width, tset.height, tset.colors)
                elif tset.board[row][col] == 'o':
                    gf.draw_o(tset.window, row, col, tset.width, tset.height, tset.colors)

        # Update the display
        pygame.display.flip()

        # Set the framerate
        pygame.time.Clock().tick(10)


run_game()
