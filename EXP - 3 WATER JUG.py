from collections import deque
def water_jug_bfs(jug1, jug2, target):
    visited = set()
    queue = deque([(0, 0, [])])

    while queue:
        x, y, path = queue.popleft()
        if x == target or y == target:
            path.append((x, y))
            return path
        if (x, y) in visited:
            continue
        visited.add((x, y))
        new_states = [
            (jug1, y, path + [(x, y)]),  
            (x, jug2, path + [(x, y)]),  
            (0, y, path + [(x, y)]),     
            (x, 0, path + [(x, y)]),     
        ]
        pour1_to_2 = min(x, jug2 - y)
        new_states.append((x - pour1_to_2, y + pour1_to_2, path + [(x, y)]))
        pour2_to_1 = min(y, jug1 - x)
        new_states.append((x + pour2_to_1, y - pour2_to_1, path + [(x, y)]))
        for state in new_states:
            queue.append(state)
    return "No solution"
jug1_capacity = 4
jug2_capacity = 3
target_amount = 2
solution = water_jug_bfs(jug1_capacity, jug2_capacity, target_amount)
if solution != "No solution":
    print("Steps to solve the Water Jug Problem:")
    for step in solution:
        print(f"Jug1: {step[0]}, Jug2: {step[1]}")
else:
    print("No solution possible!")
