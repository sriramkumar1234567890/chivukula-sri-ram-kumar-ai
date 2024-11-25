import heapq

# Helper function to calculate Manhattan distance (heuristic)
def manhattan_distance(start, goal):
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

# A* Algorithm Implementation
def a_star(start, goal, grid):
    # Priority Queue for open set (min-heap)
    open_set = []
    heapq.heappush(open_set, (0 + manhattan_distance(start, goal), 0, start))  # (f(n), g(n), position)
    
    # Dictionaries for tracking g(n) and f(n)
    g_costs = {start: 0}
    f_costs = {start: manhattan_distance(start, goal)}
    
    # Parents dictionary to reconstruct the path
    came_from = {}
    
    # Directions for moving in the grid (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # (dy, dx)

    while open_set:
        # Pop the node with the lowest f(n) value
        _, current_g, current_node = heapq.heappop(open_set)

        # If we have reached the goal, reconstruct the path
        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            path.reverse()
            return path, g_costs[goal]

        # Explore neighbors
        for direction in directions:
            neighbor = (current_node[0] + direction[0], current_node[1] + direction[1])

            # Check if the neighbor is within bounds and not a wall
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                tentative_g_cost = current_g + 1  # Assume cost of 1 per move

                # If this path to the neighbor is better, update g and f costs
                if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                    g_costs[neighbor] = tentative_g_cost
                    f_costs[neighbor] = tentative_g_cost + manhattan_distance(neighbor, goal)
                    heapq.heappush(open_set, (f_costs[neighbor], tentative_g_cost, neighbor))
                    came_from[neighbor] = current_node
    
    # If there's no path, return None
    return None, float('inf')

# Example grid (0 = open space, 1 = wall)
grid = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0]
]

# Start and Goal positions
start = (0, 0)  # (row, col)
goal = (5, 5)   # (row, col)

# Run A* algorithm
path, cost = a_star(start, goal, grid)

if path:
    print("Path found:", path)
    print("Cost:", cost)
else:
    print("No path found.")
