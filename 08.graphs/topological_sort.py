from collections import deque


# Question 1:
# Implement DFS-based topological sorting for a DAG.

def topological_sort_dfs(graph):
    visited = set()
    order = []

    def dfs(node):
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

        order.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    order.reverse()
    return order


dag = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": []
}

print("DFS order:", topological_sort_dfs(dag))


# Question 2:
# Implement Kahn's algorithm using indegrees and a queue.
# Return an empty list if the graph contains a directed cycle.

def topological_sort_kahn(graph):
    indegree = {node: 0 for node in graph}

    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    queue = deque(
        node for node in graph if indegree[node] == 0
    )

    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) != len(graph):
        return []

    return order


print("Kahn order:", topological_sort_kahn(dag))


# Question 3:
# Detect whether a directed graph contains a cycle using Kahn's algorithm.

def has_directed_cycle(graph):
    indegree = {node: 0 for node in graph}

    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    queue = deque(
        node for node in graph if indegree[node] == 0
    )

    processed = 0

    while queue:
        node = queue.popleft()
        processed += 1

        for neighbor in graph[node]:
            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return processed != len(graph)


print("DAG has cycle:", has_directed_cycle(dag))

cyclic_graph = {
    "A": ["B"],
    "B": ["C"],
    "C": ["A"]
}

print("Cyclic graph has cycle:", has_directed_cycle(cyclic_graph))


# Question 4:
# Find a valid order for tasks with dependencies.
# Each edge A -> B means task A must finish before task B.

tasks = {
    "Design": ["Develop"],
    "Develop": ["Test"],
    "Test": ["Deploy"],
    "Deploy": []
}

print("Task order:", topological_sort_kahn(tasks))


# Question 5:
# Explain why DFS adds a node to the order after visiting its neighbors.
#
# Answer:
# A node is added after its outgoing dependencies have been explored.
# Reversing the finishing order places prerequisite nodes before
# their dependent nodes.


# Question 6:
# Explain why Kahn's algorithm detects a cycle when fewer than V nodes
# are processed.
#
# Answer:
# A directed cycle prevents its nodes from reaching indegree zero.
# Therefore, some nodes remain unprocessed.


# Question 7:
# State the time and space complexity of topological sorting.
#
# Answer:
# Time complexity: O(V + E)
# Auxiliary space: O(V), excluding the graph representation.