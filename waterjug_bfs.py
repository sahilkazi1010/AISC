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

def bfs():
    visited = set()
    queue = deque()
    queue.append((0, 0))

    while queue:
        state = queue.popleft()

        if state in visited:
            continue

        visited.add(state)
        print("BFS visiting:", state)

        if is_goal(state):
            print("Goal reached:", state)
            return

        for next_state in get_next_states(*state):
            if next_state not in visited:
                queue.append(next_state)

bfs()
