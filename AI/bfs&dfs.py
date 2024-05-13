# Graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


# DFS Implementation
def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph, n, visited)
    return visited


visited = dfs(graph, 'A', [])
print("DFS:", visited)


# BFS Implementation
def bfs(graph, node):
    visited = []
    queue = [node]


    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            queue.extend(graph[n])
    return visited


visited = bfs(graph, 'A')
print("BFS:", visited)
