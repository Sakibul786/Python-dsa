import heapq


# Question 1:
# Implement Prim's algorithm and return the MST edges and total weight.

def prim(graph, start):
    visited = {start}
    min_heap = []

    for neighbor, weight in graph[start]:
        heapq.heappush(min_heap, (weight, start, neighbor))

    mst = []
    total_weight = 0

    while min_heap and len(visited) < len(graph):
        weight, first, second = heapq.heappop(min_heap)

        if second in visited:
            continue

        visited.add(second)
        mst.append((first, second, weight))
        total_weight += weight

        for neighbor, edge_weight in graph[second]:
            if neighbor not in visited:
                heapq.heappush(
                    min_heap,
                    (edge_weight, second, neighbor)
                )

    if len(visited) != len(graph):
        return [], None

    return mst, total_weight


graph = {
    0: [(1, 2), (2, 5)],
    1: [(0, 2), (2, 3), (3, 4)],
    2: [(0, 5), (1, 3), (3, 1)],
    3: [(1, 4), (2, 1)]
}

mst, total_weight = prim(graph, 0)

print("MST edges:", mst)
print("Total weight:", total_weight)


# Question 2:
# Find the MST total weight when starting from node 2.

mst, total_weight = prim(graph, 2)

print("MST edges:", mst)
print("Total weight:", total_weight)


# Question 3:
# Handle a disconnected graph.

disconnected_graph = {
    0: [(1, 2)],
    1: [(0, 2)],
    2: [(3, 1)],
    3: [(2, 1)]
}

mst, total_weight = prim(disconnected_graph, 0)

print("MST edges:", mst)
print("Total weight:", total_weight)


# Question 4:
# Explain why Prim skips an edge whose destination is already visited.
#
# Answer:
# The destination is already part of the MST. Adding the edge would
# not introduce a new vertex and could create a cycle.


# Question 5:
# State the main difference between Prim's and Kruskal's algorithms.
#
# Answer:
# Prim grows one tree by choosing the cheapest edge from the current
# tree to an unvisited vertex.
# Kruskal sorts all edges and adds an edge if it does not create a cycle.


# Question 6:
# What is the time complexity of Prim's algorithm with an adjacency
# list and a binary min-heap?
#
# Answer:
# O((V + E) log V)