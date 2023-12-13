import pygame
import sys
import numpy as np
from TicTacToemodule import *
from button import Button



class TicTacToe(object):
    player = 1
    game_over = False

# main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # to exit the window
                sys.exit()
        # connecting the console board to the window
        # to get the imput from the user ('o' or 'x')
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

                mouseX = event.pos[0]  # x
                mouseY = event.pos[1]  # y

                clicked_Row = int(mouseY // square_size)
                clicked_Col = int(mouseX // square_size)

                if availableSquares(clicked_Row, clicked_Col):
                    Square_marker(clicked_Row, clicked_Col, player)
                    if checkWin(player):
                        game_over = True
                    player = player % 2 + 1

                    drawFigure()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart()
                    game_over = False
        pygame.display.update()  # get the color from Window.fill()
