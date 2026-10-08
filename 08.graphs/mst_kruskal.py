# Question 1:
# Implement a basic Union-Find data structure.

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def union(self, first, second):
        root_first = self.find(first)
        root_second = self.find(second)

        if root_first == root_second:
            return False

        if self.rank[root_first] < self.rank[root_second]:
            self.parent[root_first] = root_second
        elif self.rank[root_first] > self.rank[root_second]:
            self.parent[root_second] = root_first
        else:
            self.parent[root_second] = root_first
            self.rank[root_first] += 1

        return True


uf = UnionFind(5)

uf.union(0, 1)
uf.union(1, 2)

print(uf.find(0))
print(uf.find(2))
print(uf.find(3))


# Question 2:
# Check whether two nodes belong to the same connected component.

uf = UnionFind(5)

uf.union(0, 1)
uf.union(1, 2)

print(uf.find(0) == uf.find(2))
print(uf.find(0) == uf.find(3))


# Question 3:
# Implement Kruskal's algorithm to find the Minimum Spanning Tree.
#
# Each edge is represented as:
# (weight, first_node, second_node)

def kruskal(n, edges):
    edges.sort()

    union_find = UnionFind(n)

    mst = []
    total_weight = 0

    for weight, first, second in edges:
        if union_find.union(first, second):
            mst.append((first, second, weight))
            total_weight += weight

            if len(mst) == n - 1:
                break

    if len(mst) != n - 1:
        return [], None

    return mst, total_weight


edges = [
    (2, 0, 1),
    (5, 0, 2),
    (3, 1, 2),
    (4, 1, 3),
    (1, 2, 3)
]

mst, total_weight = kruskal(4, edges)

print("MST:", mst)
print("Total weight:", total_weight)


# Question 4:
# Explain why Kruskal's algorithm skips an edge when union()
# returns False.
#
# Answer:
# union() returns False when both nodes already belong to the same
# connected component. Adding that edge would create a cycle.


# Question 5:
# Find the total weight of the Minimum Spanning Tree.

edges = [
    (10, 0, 1),
    (6, 0, 2),
    (5, 0, 3),
    (15, 1, 3),
    (4, 2, 3)
]

mst, total_weight = kruskal(4, edges)

print("MST:", mst)
print("Minimum total weight:", total_weight)


# Question 6:
# Return an empty MST when the graph is disconnected.

disconnected_edges = [
    (2, 0, 1),
    (3, 2, 3)
]

mst, total_weight = kruskal(4, disconnected_edges)

print("MST:", mst)
print("Total weight:", total_weight)