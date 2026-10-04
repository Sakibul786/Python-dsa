
# Question 1:
# Determine whether an undirected graph contains a cycle using DFS.

def has_cycle_undirected(graph):
    visited = set()

    def dfs(current, parent):
        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                if dfs(neighbor, current):
                    return True

            elif neighbor != parent:
                return True

        return False

    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex, None):
                return True

    return False


graph = {
    1: [2],
    2: [1, 3],
    3: [2, 4],
    4: [3]
}

print("Question 1 Answer:", has_cycle_undirected(graph))



# Question 2:
# Determine whether an undirected graph contains a cycle.

graph = {
    1: [2, 4],
    2: [1, 3],
    3: [2, 4],
    4: [1, 3]
}

print("Question 2 Answer:", has_cycle_undirected(graph))


# Question 3:
# Detect a cycle in a directed graph using DFS.

def has_cycle_directed(graph):
    visited = set()
    recursion_stack = set()

    def dfs(current):
        visited.add(current)
        recursion_stack.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True

            elif neighbor in recursion_stack:
                return True

        recursion_stack.remove(current)

        return False

    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex):
                return True

    return False


graph = {
    1: [2],
    2: [3],
    3: [],
    4: [5],
    5: []
}

print("Question 3 Answer:", has_cycle_directed(graph))


# Question 4:
# Detect a cycle in a directed graph.

graph = {
    1: [2],
    2: [3],
    3: [1]
}

print("Question 4 Answer:", has_cycle_directed(graph))



# Question 5:
# Check whether an undirected graph is cyclic or acyclic.

graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2]
}

if has_cycle_undirected(graph):
    print("Question 5 Answer: Graph contains a cycle")
else:
    print("Question 5 Answer: Graph is acyclic")
