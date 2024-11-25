def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
def check_win(board, player):
    return any(
        all(cell == player for cell in row) for row in board
    ) or any(
        all(row[i] == player for row in board) for i in range(3)
    ) or all(
        board[i][i] == player for i in range(3)
    ) or all(
        board[i][2 - i] == player for i in range(3)
    )
def check_draw(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board, current_player = [[" "] * 3 for _ in range(3)], "X"
    while True:
        print_board(board)
        row, col = map(int, input(f"Player {current_player}, enter your move (row and column): ").split())
        if board[row][col] != " ":
            print("Invalid move. Try again.")
            continue
        board[row][col] = current_player
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        current_player = "O" if current_player == "X" else "X"

if _name_ == "_main_":
    tic_tac_toe()
