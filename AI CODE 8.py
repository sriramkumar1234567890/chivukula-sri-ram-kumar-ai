# Function to perform DFS traversal (recursive approach)
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()  # Initialize the visited set

    # Mark the node as visited and process it
    visited.add(node)
    print(node, end=" ")

    # Recur for all the neighbors of the current node
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Start DFS traversal from node 'A'
print("DFS Traversal starting from node 'A':")
dfs(graph, 'A')
