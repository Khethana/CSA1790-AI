def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens(n, row=0, board=None, solutions=None):
    if board is None:
        board = []
    if solutions is None:
        solutions = []
    
    if row == n:
        solutions.append(board[:]) 
        return
    
    for col in range(n):
        if is_safe(board, row, col):
            board.append(col)
            solve_n_queens(n, row + 1, board, solutions)
            board.pop()
    
    return solutions

def print_solutions(solutions, n, limit=5):
    count = 0
    for sol in solutions:
        for row in sol:
            print("." * row + "Q" + "." * (n - row - 1))
        print("\n")
        count += 1
        if count >= limit:
            break  
n = 8
solutions = solve_n_queens(n)
print("Total solutions:", len(solutions))
print_solutions(solutions, n, limit=5)
