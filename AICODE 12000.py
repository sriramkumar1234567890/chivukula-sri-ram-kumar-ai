def display_board(board):
    """Display the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board, player):
    """Check if the player has won."""
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_draw(board):
    """Check if the game is a draw."""
    return all(board[i][j] != " " for i in range(3) for j in range(3))


def tic_tac_toe():
    """Main function to play Tic Tac Toe."""
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Welcome to Tic Tac Toe!")
    display_board(board)

    while True:
        print(f"Player {players[current_player]}'s turn:")
        try:
            row, col = map(int, input("Enter row and column (0-2, space-separated): ").split())
            if board[row][col] == " ":
                board[row][col] = players[current_player]
                display_board(board)

                if check_winner(board, players[current_player]):
                    print(f"Player {players[current_player]} wins!")
                    break

                if is_draw(board):
                    print("It's a draw!")
                    break

                current_player = 1 - current_player  # Switch players
            else:
                print("Cell already occupied! Choose a different cell.")
        except (ValueError, IndexError):
            print("Invalid input! Enter row and column as two numbers (0-2).")


if __name__ == "__main__":
    tic_tac_toe()
