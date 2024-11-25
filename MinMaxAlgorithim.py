import math

def display_board(board):
    """Display the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Check if a player has won the game."""
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_draw(board):
    """Check if the game is a draw."""
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def minimax(board, depth, is_maximizing):
    """Implement the Minimax algorithm."""
    winner = check_winner(board)
    if winner == "X":
        return 10 - depth
    if winner == "O":
        return depth - 10
    if is_draw(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    """Find the best move for the maximizer (X)."""
    best_val = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                move_val = minimax(board, 0, False)
                board[i][j] = " "
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)
    return move

def tic_tac_toe():
    """Play Tic Tac Toe with the Minimax algorithm."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    display_board(board)

    for turn in range(9):
        if turn % 2 == 0:
            print("Player X's turn:")
            move = best_move(board)
            board[move[0]][move[1]] = "X"
        else:
            print("Player O's turn:")
            row, col = map(int, input("Enter row and column (0-2, space-separated): ").split())
            if board[row][col] == " ":
                board[row][col] = "O"
            else:
                print("Invalid move! Try again.")
                continue

        display_board(board)

        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins!")
            return
        if is_draw(board):
            print("It's a draw!")
            return

if __name__ == "__main__":
    tic_tac_toe()
