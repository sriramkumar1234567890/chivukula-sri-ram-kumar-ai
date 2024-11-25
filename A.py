import heapq
def a_star(graph, start, goal, h):
    open_set = []
    heapq.heappush(open_set, (0, start))  
    g = {start: 0}
    came_from = {}
    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1], g[goal]
        for neighbor, cost in graph[current]:
            tentative_g = g[current] + cost
            if neighbor not in g or tentative_g < g[neighbor]:
                g[neighbor] = tentative_g
                f_score = tentative_g + h(neighbor)
                heapq.heappush(open_set, (f_score, neighbor))
                came_from[neighbor] = current
    return None, float('inf')
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}
def heuristic(node):
    h_values = {'A': 7, 'B': 6, 'C': 2, 'D': 0}  
    return h_values.get(node, float('inf'))
start_node = 'A'
goal_node = 'D'
path, cost = a_star(graph, start_node, goal_node, heuristic)
print("Shortest Path:", path)
print("Path Cost:", cost)
