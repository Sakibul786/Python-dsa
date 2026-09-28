from collections import deque


# Question 1:
# Perform BFS traversal starting from vertex 1.

graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2],
    6: [3]
}

queue = deque([1])
visited = {1}

bfs_result = []

while queue:
    current = queue.popleft()
    bfs_result.append(current)

    for neighbor in graph[current]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

print("Question 1 Answer:", bfs_result)


# Question 2:
# Search for a target vertex using BFS.

graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2],
    6: [3]
}

start = 1
target = 5

queue = deque([start])
visited = {start}

found = False

while queue:
    current = queue.popleft()

    if current == target:
        found = True
        break

    for neighbor in graph[current]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

print("Question 2 Answer:", found)


# Question 3:
# Count the number of vertices reachable from vertex 1.

graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2],
    6: [3],
    7: [8],
    8: [7]
}

start = 1

queue = deque([start])
visited = {start}

while queue:
    current = queue.popleft()

    for neighbor in graph[current]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

print("Question 3 Answer:", len(visited))


# Question 4:
# Find the shortest distance from vertex 1 to vertex 6
# in an unweighted graph.

graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2],
    6: [3]
}

start = 1
target = 6

queue = deque([(start, 0)])
visited = {start}

distance = -1

while queue:
    current, current_distance = queue.popleft()

    if current == target:
        distance = current_distance
        break

    for neighbor in graph[current]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append((neighbor, current_distance + 1))

print("Question 4 Answer:", distance)



# Question 5:
# Perform BFS traversal using a separate function.

def bfs(graph, start):
    queue = deque([start])
    visited = {start}
    result = []

    while queue:
        current = queue.popleft()
        result.append(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5],
    4: [2],
    5: [3]
}

print("Question 5 Answer:", bfs(graph, 1))