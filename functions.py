import pygame


def draw_lines(window, colors, lineonetop_x, lineonetop_y, lineonebottom_x,
                        lineonebottom_y):
    # Draw the lines
    pygame.draw.line(window, colors['white'], (lineonetop_x, lineonetop_y),
                     (lineonebottom_x, lineonebottom_y))


def draw_x(window, row, col, width, height, colors):
    # Draw an X in the specified grid cell
    cell_width = width // 3
    cell_height = height // 3
    start_x = col * cell_width
    start_y = row * cell_height
    pygame.draw.line(window, colors['red'], (start_x + 10, start_y + 10),
        (start_x + cell_width - 10, start_y + cell_height - 10), 5)
    pygame.draw.line(window, colors['red'], (start_x + cell_width - 10, start_y + 10),
        (start_x + 10, start_y + cell_height - 10), 5)


def draw_o(window, row, col, width, height, colors):
    # Draw an O in the specified grid cell
    cell_width = width // 3
    cell_height = height // 3
    center_x = col * cell_width + cell_width // 2
    center_y = row * cell_height + cell_height // 2
    radius = min(cell_width, cell_height) // 3
    pygame.draw.circle(window, colors['blue'], (center_x, center_y), radius, 5)


def player_move(board, width, height, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        # Get mouse position
        mouse_x, mouse_y = event.pos
        # Determine which cell was clicked
        cell_x = mouse_x // (width // 3)
        cell_y = mouse_y // (height // 3)
        # Place the move if the cell is empty
        if board[cell_y][cell_x] is None:
            board[cell_y][cell_x] = 'x'  # Example: Player places 'X'
            return True
    return False


def ai_move(board):
    if all(all(cell is not None for cell in row) for row in board):
        return  # Do nothing if the board is full
    # Check for a winning move
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                board[i][j] = 'o'
                if victory(board):
                    return  # Winning move found, so AI plays it
                board[i][j] = None  # Undo move if it does not result in a win

    # Block the opponent's winning move
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                board[i][j] = 'x'
                if victory(board):
                    board[i][j] = 'o'  # Block opponent's winning move
                    return
                board[i][j] = None  # Undo move if it does not block a win

    # Take the center if available
    if board[1][1] is None:
        board[1][1] = 'o'
        return

    # Take one of the corners if available
    for i, j in [(0, 0), (0, 2), (2, 0), (2, 2)]:
        if board[i][j] is None:
            board[i][j] = 'o'
            return

    # Take any remaining side if available
    for i, j in [(0, 1), (1, 0), (1, 2), (2, 1)]:
        if board[i][j] is None:
            board[i][j] = 'o'
            return


def victory(board):
    # Check rows for a winner
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return True

    # Check columns for a winner
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return True

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return True

    return False

