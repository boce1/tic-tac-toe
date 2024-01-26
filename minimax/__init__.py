import board_util
from constants import EMPTY, PLAYER, COMPUTER, DEPTH   

def evaluate(board):
    for row in range(3) :      
        if (board[row][0] == board[row][1] == board[row][2]) :         
            if (board[row][0] == COMPUTER) : 
                return 1
            elif (board[row][0] == PLAYER) : 
                return -1
  
    for col in range(3): 
        if (board[0][col] == board[1][col] == board[2][col]): 
          
            if (board[0][col] == COMPUTER) :  
                return 1
            elif (board[0][col] == PLAYER) : 
                return -1

    if (board[0][0] == board[1][1] == board[2][2]) : 
        if (board[0][0] == COMPUTER) : 
            return 1
        elif (board[0][0] == PLAYER) : 
            return -1
  
    if (board[0][2] == board[1][1] == board[2][0]): 
        if (board[0][2] == COMPUTER) : 
            return 1
        elif (board[0][2] == PLAYER) : 
            return -1
    return 0

def Minimax(board, depth, isMaximazing):
    score = evaluate(board)

    if score == 1 or score == -1:
        return score
    
    #if depth >= DEPTH:
    #    return score
    
    if isMaximazing:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = COMPUTER
                    best = max(best, Minimax(board, depth + 1, not isMaximazing))
                    board[i][j] = EMPTY
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER
                    best = min(best, Minimax(board, depth + 1, not isMaximazing))
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