import pygame as pg
import board_util
from constants import *
from random import choice
import minimax
pg.init()
pg.font.init()

window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Tic-Tac-Toe")

font = pg.font.SysFont("Consolas", (HEIGHT - WIDTH) * 3 // 7)

ai_score = 0
player_score = 0
tie = 0
is_players_turn = False
board = board_util.board_init()

def computer_move(board):
    global is_players_turn
    #possible_moves = []
    #for i in range(len(board)):
    #    for j in range(len(board[0])):
    #        if board[i][j] == EMPTY:
    #            possible_moves.append((i, j))
#
    #if len(possible_moves) == 9:
    #    r, c = choice(possible_moves)
    #else:
    #    r, c = minimax.find_best_move(board)
    r, c = minimax.find_best_move(board)

    board[r][c] = COMPUTER
    is_players_turn = True


def get_players_pos(x, y, is_players_turn):
    if 0 < x < WIDTH and 0 < y < WIDTH and is_players_turn:
        col = x // GAP
        row = y // GAP
        return row, col
    return None

def draw_score(win):
    ai = font.render(f"x : {ai_score}", True, RED)
    player = font.render(f"o : {player_score}", True, GREEN)
    tie_msg = font.render(f"tie : {tie}", True, BLACK)
    space = GAP // 5
    win.blit(ai, (space, WIDTH + (HEIGHT - WIDTH) // 2 - ai.get_height() // 2))
    win.blit(player, (WIDTH - space - player.get_width(), WIDTH + (HEIGHT - WIDTH) // 2 - player.get_height() // 2))
    win.blit(tie_msg, (WIDTH // 2 - tie_msg.get_width() // 2, WIDTH + (HEIGHT - WIDTH) // 2 - tie_msg.get_height() // 2))


def draw_grid(win):
    for i in range(3):
        pg.draw.line(win, BLACK, (0, (i + 1) * GAP), (WIDTH, (i + 1) * GAP), width = 3)
        pg.draw.line(win, BLACK, ((i + 1) * GAP, 0), ((i + 1) * GAP, WIDTH), width = 3)

def draw_line_after_winning(win, board):
    n = len(board)
    for i in range(n):
        if board[i][0] == board[i][1] == board[i][2] == PLAYER:
            pg.draw.line(win, BLACK, (GAP // 4, i * GAP + GAP // 2), (WIDTH - GAP // 4, i * GAP + GAP // 2), 3)
            return
    for i in range(n):
        if board[0][i] == board[1][i] == board[2][i] == PLAYER:
            pg.draw.line(win, BLACK, (i * GAP + GAP // 2, GAP // 4), (i * GAP + GAP // 2, WIDTH - GAP // 4), 3)
            return
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] == PLAYER:
        pg.draw.line(win, BLACK, (GAP // 4, GAP // 4), (WIDTH - GAP // 4, WIDTH - GAP // 4), 3)
        return
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] == PLAYER:
        pg.draw.line(win, BLACK, (WIDTH - GAP // 4, GAP // 4), (GAP // 4, WIDTH - GAP // 4), 3)
        return
    
    for i in range(n):
        if board[i][0] == board[i][1] == board[i][2] == COMPUTER:
            pg.draw.line(win, BLACK, (GAP // 4, i * GAP + GAP // 2), (WIDTH - GAP // 4, i * GAP + GAP // 2), 3)
            return
    for i in range(n):
        if board[0][i] == board[1][i] == board[2][i] == COMPUTER:
            pg.draw.line(win, BLACK, (i * GAP + GAP // 2, GAP // 4), (i * GAP + GAP // 2, WIDTH - GAP // 4), 3)
            return
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] == COMPUTER:
        pg.draw.line(win, BLACK, (GAP // 4, GAP // 4), (WIDTH - GAP // 4, WIDTH - GAP // 4), 3)
        return
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] == COMPUTER:
        pg.draw.line(win, BLACK, (WIDTH - GAP // 4, GAP // 4), (GAP // 4, WIDTH - GAP // 4), 3)
        return

def draw(win, board):
    win.fill(WHITE)
    pg.draw.rect(win, BLACK, (0,0, WIDTH, WIDTH), 3)
    draw_grid(win)
    board_util.draw_board(win, board)
    draw_line_after_winning(win, board)
    draw_score(win)
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
        player_score += 1

    elif board_util.is_win(board, COMPUTER):
        pg.time.wait(1000)
        board = board_util.board_init()
        is_players_turn = False
        ai_score += 1
        
    elif board_util.is_board_full(board):
        pg.time.wait(1000)
        board = board_util.board_init()
        is_players_turn = False
        tie += 1

pg.quit()