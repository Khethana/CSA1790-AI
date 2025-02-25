def is_valid(graph, colors, node, color):
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True

def color_map(graph, colors, node, color_options):
    if node == len(graph):
        return True

    for color in color_options:
        if is_valid(graph, colors, node, color):
            colors[node] = color
            if color_map(graph, colors, node + 1, color_options):
                return True
            colors[node] = None
    return False

graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}
color_options = ['Red', 'Green', 'Blue']
colors = [None] * len(graph)

if color_map(graph, colors, 0, color_options):
    print("Color Assignment:", colors)
else:
    print("No solution found.")
