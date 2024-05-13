import heapq


def best_first_search(graph, start, goal):
    queue = [(0, start)]
    visited = set()


    while queue:
        priority, current_node = heapq.heappop(queue)


        if current_node == goal:
            return True


        if current_node not in visited:
            visited.add(current_node)


            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    heapq.heappush(queue, (graph[current_node][neighbor], neighbor))


    return False


# example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 5},
    'C': {'A': 4, 'D': 1},
    'D': {'B': 5, 'C': 1}
}


print(best_first_search(graph, 'A', 'D'))  # returns True
