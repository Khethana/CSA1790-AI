import itertools

# Sample distance matrix (symmetric)
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def calculate_distance(path, distance_matrix):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distance_matrix[path[i]][path[i + 1]]
    # Return to the starting city
    total_distance += distance_matrix[path[-1]][path[0]]
    return total_distance

def tsp_brute_force(distance_matrix):
    n = len(distance_matrix)
    cities = list(range(n))
    min_distance = float("inf")
    best_path = None

    for perm in itertools.permutations(cities):
        distance = calculate_distance(perm, distance_matrix)
        if distance < min_distance:
            min_distance = distance
            best_path = perm

    return best_path, min_distance

# Solve TSP using brute force
best_path, min_distance = tsp_brute_force(distance_matrix)
print(f"Best path: {best_path}, Minimum distance: {min_distance}")
