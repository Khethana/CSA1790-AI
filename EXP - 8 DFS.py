from collections import deque

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    print(start, end=' ')
    visited.add(start)
    
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

print("DFS Traversal starting from node A:")
dfs(graph, 'A')
