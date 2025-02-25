import heapq
import itertools

def get_neighbors(state):
    neighbors = []
    zero_pos = state.index(0)
    row, col = divmod(zero_pos, 3)
    moves = {"up": -3, "down": 3, "left": -1, "right": 1}
    
    for move, pos_change in moves.items():
        new_pos = zero_pos + pos_change
        if move == "left" and col == 0 or move == "right" and col == 2:
            continue
        if 0 <= new_pos < 9:
            new_state = list(state)
            new_state[zero_pos], new_state[new_pos] = new_state[new_pos], new_state[zero_pos]
            neighbors.append(tuple(new_state))
    
    return neighbors

def heuristic(state, goal):
    return sum(abs(s % 3 - g % 3) + abs(s // 3 - g // 3) for s, g in zip(state, goal) if s)

def a_star_8_puzzle(start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    steps = 0
    
    while open_set:
        steps += 1
        _, current = heapq.heappop(open_set)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1], steps
        
        for neighbor in get_neighbors(current):
            tentative_g_score = g_score[current] + 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None, steps

start_state = (1, 2, 3, 4, 5, 0, 7, 8, 6)  # 0 represents the empty tile
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

solution_path, step_count = a_star_8_puzzle(start_state, goal_state)
print(f"Solution found in {step_count} steps:")
for step in solution_path:
    print(step[:3])
    print(step[3:6])
    print(step[6:])
    print()
