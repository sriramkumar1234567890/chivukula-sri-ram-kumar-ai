N = 8

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_queens(board, row):
    if row == N:
        return [board[:]]
    solutions = []
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solutions += solve_queens(board, row + 1)
    return solutions

def print_board(solution):
    for i in solution:
        board = [["." for _ in range(N)] for _ in range(N)]
        for row, col in enumerate(i):
            board[row][col] = "Q"
        for line in board:
            print(" ".join(line))
        print("\n")

board = [-1] * N
solutions = solve_queens(board, 0)
print(f"Number of solutions: {len(solutions)}\n")
print("One of the solutions:\n")
print_board([solutions[0]])
