import heapq


def astar(graph, start, goal):
    frontier = [(0, start)]  # Priority queue: (f-score, node)
    came_from = {}
    cost_so_far = {start: 0}


    while frontier:
        _, current = heapq.heappop(frontier)


        if current == goal:
            break


        for next_node in graph[current]:
            new_cost = cost_so_far[current] + graph[current][next_node]
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + heuristic(next_node, goal)
                heapq.heappush(frontier, (priority, next_node))
                came_from[next_node] = current


    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()


    return path


def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


if __name__ == "__main__":
    graph = {
        (0, 0): {(0, 1): 1, (1, 0): 1},
        (0, 1): {(0, 0): 1, (0, 2): 1},
        (0, 2): {(0, 1): 1, (1, 2): 1},
        (1, 0): {(0, 0): 1, (1, 1): 1},
        (1, 1): {(1, 0): 1, (1, 2): 1},
        (1, 2): {(0, 2): 1, (1, 1): 1}
    }
    start = (0, 0)
    goal = (1, 2)
    path = astar(graph, start, goal)
    print("Path found by A* Search:")
    print(path)
