from collections import deque

def is_goal(state):
    return state[1] == 2

def get_next_states(x, y):
    states = []
    max_x, max_y = 3, 4

    states.append((max_x, y))
    states.append((x, max_y))
    states.append((0, y))
    states.append((x, 0))

    transfer = min(x, max_y - y)
    states.append((x - transfer, y + transfer))

    transfer = min(y, max_x - x)
    states.append((x + transfer, y - transfer))

    return states

def dfs(state, visited):
    if state in visited:
        return False

    visited.add(state)
    print("DFS visiting:", state)

    if is_goal(state):
        print("Goal reached:", state)
        return True

    for next_state in get_next_states(*state):
        if next_state not in visited:
            if dfs(next_state, visited):
                return True

    return False

def run_dfs():
    visited = set()
    dfs((0, 0), visited)

run_dfs()
