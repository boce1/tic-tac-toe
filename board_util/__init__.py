import pygame as pg
from constants import *

pg.font.init()

font = pg.font.SysFont("Consolas", GAP // 2)
player_o = font.render(PLAYER, True, GREEN)
computer_x = font.render(COMPUTER, True, RED)
player_o_width = player_o.get_width()
player_o_height = player_o.get_height()
computer_x_widht = computer_x.get_width()
computer_x_height = computer_x.get_height()

def board_init():
    output = []
    for i in range(3):
        output.append([EMPTY for _ in range(3)])
    return output

def set_board(board, pos_table):
    if pos_table:
        row = pos_table[0]
        col = pos_table[1]
        if board[row][col] == EMPTY:
            board[row][col] = PLAYER
        

def draw_board(win, board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == PLAYER:
                x = j * GAP + (GAP - player_o_width) // 2
                y = i * GAP + (GAP - player_o_height) // 2
                win.blit(player_o, (x, y))

            elif board[i][j] == COMPUTER:
                x = j * GAP + (GAP - computer_x_widht) // 2
                y = i * GAP + (GAP - computer_x_height) // 2
                win.blit(computer_x, (x, y))


def is_win(board, sign):
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == sign:
            return True
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == sign:
            return True

    return False


def is_board_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True


def transverse(board):
    output = board_init()
    for i in range(3):
        for j in range(3):
            output[j][i] = board[i][j]
    return output