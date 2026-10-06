from collections import deque
import heapq

# Question 1:
# Find the shortest distance from a source node to every reachable node
# in an unweighted graph using BFS.

def bfs_shortest_distance(graph, source):
    distance = {source: 0}
    queue = deque([source])

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if neighbor not in distance:
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)

    return distance


graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 4],
    4: [2, 3, 5],
    5: [4]
}

print(bfs_shortest_distance(graph, 1))


# Question 2:
# Find the shortest path from source to target in an unweighted graph.

def shortest_path(graph, source, target):
    queue = deque([source])
    parent = {source: None}

    while queue:
        node = queue.popleft()

        if node == target:
            break

        for neighbor in graph[node]:
            if neighbor not in parent:
                parent[neighbor] = node
                queue.append(neighbor)

    if target not in parent:
        return []

    path = []
    current = target

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path


print(shortest_path(graph, 1, 5))


# Question 3:
# Return both the shortest distance and the actual shortest path
# from source to target.

def shortest_distance_and_path(graph, source, target):
    queue = deque([source])
    distance = {source: 0}
    parent = {source: None}

    while queue:
        node = queue.popleft()

        if node == target:
            break

        for neighbor in graph[node]:
            if neighbor not in distance:
                distance[neighbor] = distance[node] + 1
                parent[neighbor] = node
                queue.append(neighbor)

    if target not in distance:
        return -1, []

    path = []
    current = target

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    return distance[target], path


distance, path = shortest_distance_and_path(graph, 1, 5)

print("Distance:", distance)
print("Path:", path)


# Question 4:
# Implement Dijkstra's algorithm for a weighted graph.
# Find the shortest distance from the source to every node.

weighted_graph = {
    1: [(2, 4), (3, 1)],
    2: [(1, 4), (3, 2), (4, 5)],
    3: [(1, 1), (2, 2), (4, 8)],
    4: [(2, 5), (3, 8)]
}


def dijkstra(graph, source):
    distances = {node: float("inf") for node in graph}
    distances[source] = 0

    min_heap = [(0, source)]

    while min_heap:
        current_distance, node = heapq.heappop(min_heap)

        if current_distance > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(min_heap, (new_distance, neighbor))

    return distances


print(dijkstra(weighted_graph, 1))


# Question 5:
# Find the shortest path between two nodes in a weighted graph
# using Dijkstra's algorithm.

def dijkstra_shortest_path(graph, source, target):
    distances = {node: float("inf") for node in graph}
    parent = {source: None}

    distances[source] = 0

    min_heap = [(0, source)]

    while min_heap:
        current_distance, node = heapq.heappop(min_heap)

        if current_distance > distances[node]:
            continue

        if node == target:
            break

        for neighbor, weight in graph[node]:
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                parent[neighbor] = node
                heapq.heappush(min_heap, (new_distance, neighbor))

    if distances[target] == float("inf"):
        return float("inf"), []

    path = []
    current = target

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    return distances[target], path


distance, path = dijkstra_shortest_path(weighted_graph, 1, 4)

print("Shortest distance:", distance)
print("Shortest path:", path)


# Question 6:
# Return an empty path when the target node is unreachable.

disconnected_graph = {
    1: [(2, 5)],
    2: [(1, 5)],
    3: [(4, 2)],
    4: [(3, 2)]
}

distance, path = dijkstra_shortest_path(disconnected_graph, 1, 4)

print("Distance:", distance)
print("Path:", path)