import board_util
from constants import EMPTY, PLAYER, COMPUTER, DEPTH   

def evaluate(board):
    if board_util.is_win(board, COMPUTER):
        return 10
    if board_util.is_win(board, PLAYER):
        return -10
    
    for row in board:
        if row[0] == row[2] == COMPUTER:
            return 5
        if row[0] == row[2] == PLAYER:
            return -5

    temp_board = board_util.transverse(board)
    for col in temp_board:
        if col[0] == col[2] == COMPUTER:
            return 5
        if col[0] == col[2] == PLAYER:
            return -5

    for row in board:
        if row.count(COMPUTER) == 2:
            return 3
        if row.count(PLAYER) == 2:
            return -3
    
    for col in temp_board:
        if col.count(COMPUTER) == 2:
            return 3
        if col.count(PLAYER) == 2:
            return -3

    return 0

def Minimax(board, depth, isMaximizing):
    score = evaluate(board)
    
    if board_util.is_win(board, COMPUTER) or board_util.is_win(board, PLAYER) or board_util.is_board_full(board) or depth > DEPTH:
        return score
    
    if isMaximizing:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = COMPUTER
                    best = max(best, Minimax(board, depth + 1, False))
                    board[i][j] = EMPTY
        return best

    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER
                    best = min(best, Minimax(board, depth + 1, True))
                    board[i][j] = EMPTY

        return best

def find_best_move(board):
    best_val = -1000
    move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = COMPUTER
                val = Minimax(board, 0, False)
                board[i][j] = EMPTY

                if val > best_val:
                    best_val = val
                    move = (i, j)
                    #print(best_val, move)

    return move