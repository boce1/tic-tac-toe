import board_util
from constants import EMPTY, PLAYER, COMPUTER, DEPTH   

def evaluate(board):
    if board_util.is_win(board, COMPUTER):
        return 1
    elif board_util.is_win(board, PLAYER):
        return -1
    elif board_util.is_board_full(board):
        return 0
    return 0

def Minimax(board, depth, isMaximizing):
    score = evaluate(board)
    
    if board_util.is_board_full(board) or depth >= DEPTH:
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

    return move