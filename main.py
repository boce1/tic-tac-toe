import pygame as pg
import board_util
from constants import *
from random import choice
import minimax
pg.init()


window = pg.display.set_mode((WIDTH, WIDTH))
pg.display.set_caption("Tic-Tac-Toe")

is_players_turn = False
board = board_util.board_init()

def computer_move(board):
    global is_players_turn
    possible_moves = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                possible_moves.append((i, j))
#
    if len(possible_moves) == 9:
        r, c = choice(possible_moves)
    else:
        r, c = minimax.find_best_move(board)

    board[r][c] = COMPUTER
    is_players_turn = True


def get_players_pos(x, y, is_players_turn):
    if is_players_turn:
        col = x // GAP
        row = y // GAP
        return row, col
    return None

def draw_grid(win):
    for i in range(3):
        pg.draw.line(win, BLACK, (0, (i + 1) * GAP), (WIDTH, (i + 1) * GAP), width = 3)
        pg.draw.line(win, BLACK, ((i + 1) * GAP, 0), ((i + 1) * GAP, HEIGHT), width = 3)

def draw_line_after_winning(win, board):
    n = len(board)
    for i in range(n):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] in (COMPUTER, PLAYER):
            pg.draw.line(win, BLACK, (GAP // 4, i * GAP + GAP // 2), (WIDTH - GAP // 4, i * GAP + GAP // 2), 3)
            return
    for i in range(n):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] in (COMPUTER, PLAYER):
            pg.draw.line(win, BLACK, (i * GAP + GAP // 2, GAP // 4), (i * GAP + GAP // 2, WIDTH - GAP // 4), 3)
            return
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] in (COMPUTER, PLAYER):
        pg.draw.line(win, BLACK, (GAP // 4, GAP // 4), (WIDTH - GAP // 4, WIDTH - GAP // 4), 3)
        return
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] in (COMPUTER, PLAYER):
        pg.draw.line(win, BLACK, (WIDTH - GAP // 4, GAP // 4), (GAP // 4, WIDTH - GAP // 4), 3)
        return

def draw(win, board):
    win.fill(WHITE)
    pg.draw.rect(win, BLACK, (0,0, WIDTH, HEIGHT), 3)
    draw_grid(win)
    board_util.draw_board(win, board)
    draw_line_after_winning(win, board)
    pg.display.update()

run = True
while run:
    mouse_x, mouse_y = pg.mouse.get_pos()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                table_pos = get_players_pos(mouse_x, mouse_y, is_players_turn)
                if table_pos and board[table_pos[0]][table_pos[1]] == EMPTY:
                    board_util.set_board(board, table_pos)
                    is_players_turn = False
    

    if not is_players_turn:
        computer_move(board)

    draw(window, board)

    if board_util.is_win(board, PLAYER):
        pg.time.wait(1000)
        board = board_util.board_init()
        is_players_turn = False
        #print("O has won!")
    elif board_util.is_win(board, COMPUTER):
        pg.time.wait(1000)
        board = board_util.board_init()
        is_players_turn = False
        #print("X has won!")
    elif board_util.is_tie(board):
        pg.time.wait(1000)
        board = board_util.board_init()
        is_players_turn = False
        #print("its tie")


pg.quit()