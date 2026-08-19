import pygame
import sys
import numpy as np

from hand_tracking import get_hand_data

# Initialize pygame
pygame.init()

# Constants
ROWS = 6
COLS = 7
CELL_SIZE = 100

WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE

# Colors
BACKGROUND = (15, 15, 25)
BOARD_BLUE = (40, 90, 180)

BLACK = (0, 0, 0)
RED = (255, 70, 70)
YELLOW = (255, 220, 50)

WHITE = (255, 255, 255)
LIGHT_WHITE = (255, 255, 255, 80)

# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gesture Connect 4")

# FPS control
clock = pygame.time.Clock()

# Board
board = np.zeros((ROWS, COLS))

# Fonts
title_font = pygame.font.SysFont(None, 70)
turn_font = pygame.font.SysFont(None, 40)

# Game state
turn = 0
game_over = False
winner = None

# Smoothing
smooth_x = 0

# Prevent repeated drops
pinch_cooldown = False


def reset_game():

    global board
    global turn
    global game_over
    global winner

    board = np.zeros((ROWS, COLS))

    turn = 0
    game_over = False
    winner = None


def draw_board(selected_col):

    screen.fill(BACKGROUND)

    for row in range(ROWS):
        for col in range(COLS):

            # Board cells
            pygame.draw.rect(
                screen,
                BOARD_BLUE,
                (
                    col * CELL_SIZE,
                    row * CELL_SIZE,
                    CELL_SIZE,
                    CELL_SIZE
                ),
                border_radius=12
            )

            # Transparent selector
            if col == selected_col and not game_over:

                overlay = pygame.Surface(
                    (CELL_SIZE, CELL_SIZE),
                    pygame.SRCALPHA
                )

                overlay.fill(LIGHT_WHITE)

                screen.blit(
                    overlay,
                    (
                        col * CELL_SIZE,
                        row * CELL_SIZE
                    )
                )

            # Piece colors
            color = BLACK

            if board[row][col] == 1:
                color = RED

            elif board[row][col] == 2:
                color = YELLOW

            # Draw discs
            pygame.draw.circle(
                screen,
                color,
                (
                    col * CELL_SIZE + CELL_SIZE // 2,
                    row * CELL_SIZE + CELL_SIZE // 2
                ),
                40
            )

    # Turn indicator
    if not game_over:

        if turn == 0:
            turn_text = turn_font.render(
                "RED TURN",
                True,
                RED
            )

        else:
            turn_text = turn_font.render(
                "YELLOW TURN",
                True,
                YELLOW
            )

        screen.blit(turn_text, (20, 20))

    # Winner screen
    if game_over:

        if winner == 1:
            text = title_font.render(
                "RED WINS!",
                True,
                RED
            )

        else:
            text = title_font.render(
                "YELLOW WINS!",
                True,
                YELLOW
            )

        restart_text = turn_font.render(
            "Press R to Restart",
            True,
            WHITE
        )

        screen.blit(text, (160, 230))
        screen.blit(restart_text, (220, 320))

    pygame.display.update()


def drop_piece(col, player):

    for row in range(ROWS - 1, -1, -1):

        if board[row][col] == 0:

            board[row][col] = player
            return True

    return False


def check_winner(player):

    # Horizontal
    for row in range(ROWS):
        for col in range(COLS - 3):

            if (
                board[row][col] == player and
                board[row][col + 1] == player and
                board[row][col + 2] == player and
                board[row][col + 3] == player
            ):
                return True

    # Vertical
    for row in range(ROWS - 3):
        for col in range(COLS):

            if (
                board[row][col] == player and
                board[row + 1][col] == player and
                board[row + 2][col] == player and
                board[row + 3][col] == player
            ):
                return True

    # Diagonal down-right
    for row in range(ROWS - 3):
        for col in range(COLS - 3):

            if (
                board[row][col] == player and
                board[row + 1][col + 1] == player and
                board[row + 2][col + 2] == player and
                board[row + 3][col + 3] == player
            ):
                return True

    # Diagonal up-right
    for row in range(3, ROWS):
        for col in range(COLS - 3):

            if (
                board[row][col] == player and
                board[row - 1][col + 1] == player and
                board[row - 2][col + 2] == player and
                board[row - 3][col + 3] == player
            ):
                return True

    return False


# Main loop
running = True

while running:

    clock.tick(60)

    result = get_hand_data()

    selected_col = 0

    if result is not None and not game_over:

        finger_x, frame_width, pinch = result

        # Smooth movement
        smooth_x = smooth_x + (finger_x - smooth_x) * 0.2

        # Convert hand position to column
        selected_col = int((smooth_x / frame_width) * COLS)

        selected_col = max(0, min(COLS - 1, selected_col))

        # Drop disc
        if pinch and not pinch_cooldown:

            if turn == 0:

                if drop_piece(selected_col, 1):

                    if check_winner(1):

                        winner = 1
                        game_over = True

                    turn = 1

            else:

                if drop_piece(selected_col, 2):

                    if check_winner(2):

                        winner = 2
                        game_over = True

                    turn = 0

            pinch_cooldown = True

        # Reset pinch
        if not pinch:
            pinch_cooldown = False

    draw_board(selected_col)

    # Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # Restart game
            if event.key == pygame.K_r:
                reset_game()

pygame.quit()
sys.exit()