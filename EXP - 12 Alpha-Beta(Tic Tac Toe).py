import math

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def alpha_beta_pruning(board, depth, alpha, beta, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    elif all(cell != ' ' for row in board for cell in row):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = alpha_beta_pruning(board, depth + 1, alpha, beta, False)
                    board[i][j] = ' '
                    best_score = max(best_score, score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = alpha_beta_pruning(board, depth + 1, alpha, beta, True)
                    board[i][j] = ' '
                    best_score = min(best_score, score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score

def find_best_move_alpha_beta(board):
    best_score = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                score = alpha_beta_pruning(board, 0, -math.inf, math.inf, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

board = [['X', 'O', 'X'],
         ['O', ' ', ' '],
         ['X', ' ', 'O']]
best_move = find_best_move_alpha_beta(board)
print("Optimal move for X with Alpha-Beta Pruning:", best_move)
