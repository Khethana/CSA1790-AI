from functools import lru_cache

def tsp_held_karp(graph):
    n = len(graph)
    
    @lru_cache(None)
    def dp(mask, pos):
        if mask == (1 << n) - 1:  # All cities visited
            return graph[pos][0]  # Return to the starting city
        
        min_cost = float('inf')
        for city in range(n):
            if not (mask & (1 << city)):  # If city is not visited
                new_cost = graph[pos][city] + dp(mask | (1 << city), city)
                min_cost = min(min_cost, new_cost)
        
        return min_cost
    
    return dp(1, 0)  # Start from city 0 with only city 0 visited

# Example graph
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

min_cost = tsp_held_karp(graph)
print(f"Minimum Cost: {min_cost}")
