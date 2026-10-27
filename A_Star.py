from queue import PriorityQueue

def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def astar(grid, start, goal):
    open_set = PriorityQueue()
    open_set.put((heuristic(start, goal), start))

    came_from = {}
    g_cost = {start: 0}

    while not open_set.empty():
        _, current = open_set.get()

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        x, y = current
        neighbors = [
            (x-1, y),
            (x+1, y),
            (x, y-1),
            (x, y+1)
        ]

        for neighbor in neighbors:
            nx, ny = neighbor

            if (0 <= nx < len(grid) and
                0 <= ny < len(grid[0]) and
                grid[nx][ny] == 0):

                new_g = g_cost[current] + 1

                if neighbor not in g_cost or new_g < g_cost[neighbor]:
                    g_cost[neighbor] = new_g
                    f = new_g + heuristic(neighbor, goal)
                    open_set.put((f, neighbor))
                    came_from[neighbor] = current

    return None

grid = [
    [0,0,0,0,0],
    [0,1,1,0,0],
    [0,0,0,1,0],
    [0,1,0,0,0],
    [0,0,0,1,0]
]

start = (0,0)
goal = (4,4)

path = astar(grid, start, goal)
print("Path Found:")
print(path)
