def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))
    print()

def is_safe(board, row, col):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, col):
    # If all queens are placed
    if col >= len(board):
        return True

    # Try placing the queen in all rows one by one
    for i in range(len(board)):
        if is_safe(board, i, col):
            # Place the queen
            board[i][col] = 1

            # Recur to place the rest of the queens
            if solve_nqueens(board, col + 1):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove the queen
            board[i][col] = 0

    # If the queen can't be placed in any row in this column
    return False

def solve_8_queens():
    # Initialize an 8x8 chessboard with all zeros
    board = [[0] * 8 for _ in range(8)]

    if solve_nqueens(board, 0):
        print("Solution found:")
        print_board(board)
    else:
        print("No solution found.")

# Solve the 8 Queens problem
solve_8_queens()
