from collections import deque

def bfs(graph, start):
    visited = set()  
    queue = deque([start])  
    
    while queue:
        node = queue.popleft()  
        
        if node not in visited:
            print(node, end=' ') 
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)
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

print("BFS Traversal starting from node A:")
bfs(graph, 'A')
