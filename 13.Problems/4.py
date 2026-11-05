"""
PROBLEM:
You are given a weighted, undirected graph with V vertices
and E edges.

Each edge is represented as:
(source, destination, weight)

Find the shortest distance from a given source vertex
to every other vertex.

If a vertex cannot be reached, its distance should be infinity.

EXAMPLE:
V = 5

edges = [
    (0, 1, 4),
    (0, 2, 1),
    (2, 1, 2),
    (1, 3, 1),
    (2, 3, 5),
    (3, 4, 3)
]

source = 0

Expected Output:
[0, 3, 1, 4, 7]

APPROACH:
Use Dijkstra's Algorithm.

1. Initialize all distances as infinity.
2. Set the source distance to zero.
3. Use a min-heap to process the nearest vertex.
4. Check all neighboring vertices.
5. Update a distance if a shorter path is found.
6. Continue until the heap becomes empty.

Dijkstra's algorithm works with non-negative edge weights.
"""

import heapq


def dijkstra(vertices, edges, source):
    graph = [[] for _ in range(vertices)]

    for u, v, weight in edges:
        if weight < 0:
            raise ValueError("Edge weights must be non-negative.")

        graph[u].append((v, weight))
        graph[v].append((u, weight))

    distances = [float("inf")] * vertices
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
                heapq.heappush(
                    min_heap,
                    (new_distance, neighbor)
                )

    return distances


# Test Case 1
V = 5
edges = [
    (0, 1, 4),
    (0, 2, 1),
    (2, 1, 2),
    (1, 3, 1),
    (2, 3, 5),
    (3, 4, 3)
]

print(dijkstra(V, edges, 0))




V = 4
edges = [
    (0, 1, 5),
    (2, 3, 2)
]

print(dijkstra(V, edges, 0))




print(dijkstra(1, [], 0))




V = 4
edges = [
    (0, 1, 10),
    (0, 2, 3),
    (2, 1, 2),
    (1, 3, 1),
    (2, 3, 8)
]

print(dijkstra(V, edges, 0))



"""
EXPLANATION:

Consider the first example.

Starting vertex = 0

Initial distances:
[0, inf, inf, inf, inf]

Step 1:
From vertex 0:
- Distance to vertex 1 = 4
- Distance to vertex 2 = 1

Distances:
[0, 4, 1, inf, inf]

Step 2:
Vertex 2 has the smallest distance.
- New distance to vertex 1 = 1 + 2 = 3
- New distance to vertex 3 = 1 + 5 = 6

Distances:
[0, 3, 1, 6, inf]

Step 3:
Vertex 1 has the smallest unprocessed distance.
- New distance to vertex 3 = 3 + 1 = 4

Distances:
[0, 3, 1, 4, inf]

Step 4:
From vertex 3:
- New distance to vertex 4 = 4 + 3 = 7

Final distances:
[0, 3, 1, 4, 7]

WHY USE A MIN-HEAP?
A min-heap allows us to process the vertex with the
smallest known distance efficiently.

WHY CHECK current_distance > distances[node]?
The heap can contain outdated entries.
This condition skips entries that are no longer useful.

COMPLEXITY:
Time: O((V + E) log V)
Space: O(V + E)

V = Number of vertices
E = Number of edges

IMPORTANT:
Dijkstra's algorithm does not work correctly with
negative edge weights.
"""