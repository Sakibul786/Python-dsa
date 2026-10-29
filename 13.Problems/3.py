"""
PROBLEM:
You are given a directed graph with n nodes labeled from 0 to n - 1
and a list of directed edges.

Determine whether the graph contains a cycle.

A cycle exists if you can start from a node and follow directed
edges to return to that same node.

EXAMPLE:
Input:
n = 4
edges = [
    (0, 1),
    (1, 2),
    (2, 0),
    (2, 3)
]

Expected Output:
True

APPROACH:
Use Depth-First Search (DFS) with three states:
0 = Unvisited
1 = Currently visiting
2 = Fully processed

If DFS reaches a node that is currently being visited,
a directed cycle exists.
"""

def has_directed_cycle(n, edges):
    graph = [[] for _ in range(n)]

    for source, destination in edges:
        graph[source].append(destination)

    state = [0] * n

    def dfs(node):
        state[node] = 1

        for neighbor in graph[node]:
            if state[neighbor] == 1:
                return True

            if state[neighbor] == 0:
                if dfs(neighbor):
                    return True

        state[node] = 2
        return False

    for node in range(n):
        if state[node] == 0:
            if dfs(node):
                return True

    return False


# Test Case 1: A cycle exists
n = 4
edges = [(0, 1), (1, 2), (2, 0), (2, 3)]
print(has_directed_cycle(n, edges))
# Expected Output: True


# Test Case 2: No cycle exists
n = 4
edges = [(0, 1), (1, 2), (2, 3)]
print(has_directed_cycle(n, edges))
# Expected Output: False


# Test Case 3: A disconnected component contains a cycle
n = 5
edges = [(0, 1), (2, 3), (3, 4), (4, 2)]
print(has_directed_cycle(n, edges))
# Expected Output: True


# Test Case 4: An empty graph
n = 3
edges = []
print(has_directed_cycle(n, edges))
# Expected Output: False


"""
EXPLANATION:
In Test Case 1:
1. DFS starts at node 0.
2. It visits node 1, then node 2.
3. Node 2 has an edge back to node 0.
4. Node 0 is still in the visiting state.
5. Therefore, a directed cycle exists.

Why use three states?
- Unvisited: The node has not been explored.
- Visiting: The node is part of the current DFS path.
- Processed: All outgoing edges have been explored.

An edge to a visiting node indicates a cycle.
An edge to a processed node does not necessarily indicate a cycle.

COMPLEXITY:
Time: O(V + E)
Space: O(V + E)

V = Number of vertices
E = Number of directed edges

NOTE:
This recursive solution may reach Python's recursion limit on
very deep graphs. An iterative DFS can be used for large inputs.
"""