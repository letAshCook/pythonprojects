import pygame
import sys
import numpy as np



# initializing the pygame module
pygame.init()

WIDTH = 800
HEIGHT = WIDTH  # For flexible dimensions
# the width of the graph
Lines_Width = 15
board_rows = 3
board_cols = 3
square_size = WIDTH//board_cols  # For flexible dimensions

# the size of the circle
Circle_radius = square_size//3  # flixible fiqure sizes
Circle_Width = 15

# the x
CrossWidth = 25
# the space between the cross and the corners #flexible figure sizes
space = square_size//4

bg_color = (20, 204, 245)
# the color of the graph line
LineColor = (23, 160, 202)

# to display the screen
Window = pygame.display.set_mode((WIDTH, HEIGHT))
# the title of the screen
pygame.display.set_caption("Tic-Tac-Toe")
# the bg-color of the screen
Window.fill(bg_color)

# board
board = np.zeros((board_rows, board_cols))
# print(board) #for debugging


def draw_lines():
    # drawing the graph
    # 1st horizontal line
    pygame.draw.line(Window, LineColor, (0, square_size),
                     (WIDTH, square_size), Lines_Width)
    # 2nd horizontal line
    pygame.draw.line(Window, LineColor, (0, 2*square_size),
                     (WIDTH, 2*square_size), Lines_Width)

    # 1st verticle line
    pygame.draw.line(Window, LineColor, (square_size, 0),
                     (square_size, HEIGHT), Lines_Width)
    # 2nd verticle line
    pygame.draw.line(Window, LineColor, (2*square_size, 0),
                     (2*square_size, HEIGHT), Lines_Width)


# console board
# fill the figures in the respective clicked coordinated for each player
def drawFigure():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 1:
                pygame.draw.circle(Window, "white", (int(
                    col*square_size+square_size//2), int(row*square_size+square_size//2)), Circle_radius, Circle_Width)
            elif board[row][col] == 2:
                pygame.draw.line(Window, "black", (col * square_size + space, row * square_size + square_size - space),
                                 (col * square_size + square_size - space, row * square_size + space), CrossWidth)
                pygame.draw.line(Window, "black", (col * square_size + space, row * square_size + space),
                                 (col * square_size + square_size - space, row * square_size + square_size - space), CrossWidth)

# let respective player mark the square


def Square_marker(rows, cols, player):
    board[rows][cols] = player


def availableSquares(rows, cols):
    # to check for an empty box in each rows and columns
    if board[rows][cols] == 0:
        return True
    else:
        return False

# to check if the bord is full
# if yes it will enter true else flase


def isBoardFull():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 0:
                return False
    return True


def checkWin(player):
    # verticle win checking
    for col in range(board_cols):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            drawVerticleline(col, player)
            return True

    # Horizontal win checking
    for row in range(board_rows):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            drawHorizontalline(row, player)
            return True

    # asc diagonal line win checking
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        drawAscDiagonalLine(player)
        return True

    # dsc diagonal line win checking
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        drawDcsDiagonalLine(player)
        return True

    return False


def drawVerticleline(col, player):
    posX = col * square_size + square_size//2

    if player == 1:
        color = "white"
    elif player == 2:
        color = "black"

    pygame.draw.line(Window, color, (posX, 15), (posX, HEIGHT - 15), 15)


def drawHorizontalline(row, player):
    posY = row * square_size + square_size//2

    if player == 1:
        color = "white"
    elif player == 2:
        color = "black"

    pygame.draw.line(Window, color, (15, posY), (WIDTH-15, posY), 15)


def drawAscDiagonalLine(player):
    if player == 1:
        color = "white"
    elif player == 2:
        color = "black"

    pygame.draw.line(Window, color, (15, HEIGHT-15), (WIDTH-15, 15), 15)


def drawDcsDiagonalLine(player):
    if player == 1:
        color = "white"
    elif player == 2:
        color = "black"

    pygame.draw.line(Window, color, (15, 15), (WIDTH-15, HEIGHT-15), 15)


def restart():
    Window.fill(bg_color)
    draw_lines()
    player = 1
    for row in range(board_rows):
        for col in range(board_rows):
            board[row][col] = 0


draw_lines()

if __name__ == "__main__":
    print('This part of the program wont be included in the the TicTacToe program')
