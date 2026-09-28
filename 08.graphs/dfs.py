from collections import deque


# Question 1:
# Perform DFS traversal recursively starting from vertex 1.

graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2],
    6: [3]
}


def dfs_recursive(graph, current, visited, result):
    visited.add(current)
    result.append(current)

    for neighbor in graph[current]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, result)


visited = set()
result = []

dfs_recursive(graph, 1, visited, result)

print("Question 1 Answer:", result)



# Question 2:
# Search for a target vertex using recursive DFS.

def dfs_search(graph, current, target, visited):
    if current == target:
        return True

    visited.add(current)

    for neighbor in graph[current]:
        if neighbor not in visited:
            if dfs_search(graph, neighbor, target, visited):
                return True

    return False


target = 5

visited = set()

print("Question 2 Answer:", dfs_search(graph, 1, target, visited))



# Question 3:
# Perform DFS iteratively using a stack.

def dfs_iterative(graph, start):
    stack = [start]
    visited = {start}
    result = []

    while stack:
        current = stack.pop()
        result.append(current)

        for neighbor in reversed(graph[current]):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return result


print("Question 3 Answer:", dfs_iterative(graph, 1))



# Question 4:
# Count the number of vertices reachable from vertex 1 using DFS.

def count_reachable(graph, start):
    visited = set()

    def dfs(current):
        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)

    return len(visited)


print("Question 4 Answer:", count_reachable(graph, 1))



# Question 5:
# Count the number of connected components in an undirected graph.

graph = {
    1: [2],
    2: [1],
    3: [4],
    4: [3],
    5: []
}


def count_components(graph):
    visited = set()
    components = 0

    def dfs(current):
        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                dfs(neighbor)

    for vertex in graph:
        if vertex not in visited:
            components += 1
            dfs(vertex)

    return components


print("Question 5 Answer:", count_components(graph))
