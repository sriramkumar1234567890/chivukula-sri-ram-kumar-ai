from collections import deque


def is_valid(state):
    M, C, B = state
    if M < 0 or C < 0 or M > 3 or C > 3:
        return False
    if M > 0 and M < C:
        return False
    if M < 3 and (3 - M) < (3 - C):
        return False
    return True


def get_successors(state):
    M, C, B = state
    successors = []
    if B == 0:
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        for move in moves:
            new_state = (M - move[0], C - move[1], 1)
            if is_valid(new_state):
                successors.append(new_state)
    else:
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        for move in moves:
            new_state = (M + move[0], C + move[1], 0)
            if is_valid(new_state):
                successors.append(new_state)
    return successors


def bfs(start_state, goal_state):
    queue = deque([(start_state, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()

        if current_state in visited:
            continue

        visited.add(current_state)

        if current_state == goal_state:
            return path + [current_state]

        for successor in get_successors(current_state):
            queue.append((successor, path + [current_state]))

    return None


# Define the initial and goal states
start_state = (3, 3, 0)
goal_state = (0, 0, 1)

solution = bfs(start_state, goal_state)

if solution:
    print("Solution found:")
    for state in solution:
        print(f"Missionaries: {state[0]}, Cannibals: {state[1]}, Boat: {'Left' if state[2] == 0 else 'Right'}")
else:
    print("No solution found.")
