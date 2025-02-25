def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

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

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    for _ in range(9):
        print_board(board)
        row = int(input(f"Player {player}, enter row (0-2): "))
        col = int(input(f"Player {player}, enter col (0-2): "))
        if board[row][col] == ' ':
            board[row][col] = player
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                return
            player = 'O' if player == 'X' else 'X'
        else:
            print("Cell already occupied, try again.")
    print_board(board)
    print("It's a draw!")

tic_tac_toe()

