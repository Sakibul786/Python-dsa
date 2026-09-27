# Question 1:
# Create an undirected graph using an adjacency list.

graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 4],
    4: [2, 3]
}

print("Question 1 Answer:")
print(graph)


# Question 2:
# Add a new vertex to the graph.

graph[5] = []

print("\nQuestion 2 Answer:")
print(graph)


# Question 3:
# Add an undirected edge between vertices 4 and 5.

graph[4].append(5)
graph[5].append(4)

print("\nQuestion 3 Answer:")
print(graph)


# Question 4:
# Check whether an edge exists between vertices 1 and 3.

source = 1
target = 3

if target in graph[source]:
    print("\nQuestion 4 Answer: Edge exists")
else:
    print("\nQuestion 4 Answer: Edge does not exist")


# Question 5:
# Create an adjacency matrix for the following graph:
#
# 1 -- 2
# |    |
# 3 -- 4

vertices = [1, 2, 3, 4]

matrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]

print("\nQuestion 5 Answer:")

for row in matrix:
    print(row)