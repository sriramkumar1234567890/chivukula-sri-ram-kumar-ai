import itertools

# Function to calculate the total distance of a route
def calculate_total_distance(route, distance_matrix):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i]][route[i + 1]]
    total_distance += distance_matrix[route[-1]][route[0]]  # Return to the starting city
    return total_distance

# Function to solve TSP using brute force
def tsp_bruteforce(distance_matrix):
    n = len(distance_matrix)
    # Generate all possible routes (permutations)
    cities = list(range(n))  # List of city indices [0, 1, 2, ..., n-1]
    min_distance = float('inf')  # Initialize minimum distance to a large number
    best_route = None  # To store the best route

    # Try every permutation of cities (excluding the start city)
    for route in itertools.permutations(cities):
        current_distance = calculate_total_distance(route, distance_matrix)
        
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = route

    return best_route, min_distance

# Example distance matrix (symmetric, i.e., distance[i][j] == distance[j][i])
# For example: 0 -> A, 1 -> B, 2 -> C, 3 -> D, etc.
distance_matrix = [
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 30],
    [15, 35, 0, 30, 5],
    [20, 25, 30, 0, 15],
    [25, 30, 5, 15, 0]
]

# Solve TSP using brute force
best_route, min_distance = tsp_bruteforce(distance_matrix)

# Convert the city indices to a more readable format
city_names = ['A', 'B', 'C', 'D', 'E']
best_route_names = [city_names[i] for i in best_route]

# Print the results
print("Best route:", " -> ".join(best_route_names))
print("Minimum distance:", min_distance)
