from collections import deque

# Function to perform BFS traversal
def bfs(graph, start):
    # Create a queue for BFS and a set to keep track of visited nodes
    queue = deque([start])  # Start with the start node
    visited = set()         # Set to keep track of visited nodes

    visited.add(start)      # Mark the start node as visited

    while queue:
        node = queue.popleft()  # Dequeue a node
        print(node, end=" ")    # Process the node (print it)

        # Explore all neighbors of the current node
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)  # Mark neighbor as visited
                queue.append(neighbor)  # Enqueue the neighbor

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Start BFS traversal from node 'A'
print("BFS Traversal starting from node 'A':")
bfs(graph, 'A')
