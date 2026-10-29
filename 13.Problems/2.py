"""
PROBLEM:
You are given a grid of 0s and 1s.
A 1 represents land, and a 0 represents water.
An island consists of land cells connected horizontally
or vertically.

Return the number of islands in the grid.

EXAMPLE:
Input:
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

Expected Output:
3

APPROACH:
1. Traverse every cell in the grid.
2. When an unvisited land cell is found, count a new island.
3. Use BFS to visit all connected land cells.
4. Continue until every cell has been checked.
"""

from collections import deque


def count_islands(grid):
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    island_count = 0

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "1" and (row, col) not in visited:
                island_count += 1

                queue = deque([(row, col)])
                visited.add((row, col))

                while queue:
                    current_row, current_col = queue.popleft()

                    for dr, dc in directions:
                        next_row = current_row + dr
                        next_col = current_col + dc

                        if (
                            0 <= next_row < rows
                            and 0 <= next_col < cols
                            and grid[next_row][next_col] == "1"
                            and (next_row, next_col) not in visited
                        ):
                            visited.add((next_row, next_col))
                            queue.append((next_row, next_col))

    return island_count


# Test Case 1
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(count_islands(grid))



# Test Case 2
print(count_islands([["1", "1"], ["1", "1"]]))



# Test Case 3
print(count_islands([["0", "0"], ["0", "0"]]))



# Test Case 4
print(count_islands([["1", "0"], ["0", "1"]]))



"""
EXPLANATION:
- Each time an unvisited land cell is found, a new island is counted.
- BFS visits all horizontally and vertically connected land cells.
- The visited set prevents counting the same cell more than once.
- Diagonal connections do not form a single island.

DRY RUN:
The first four connected cells form island 1.
The cell at row 2, column 2 forms island 2.
The last two connected cells form island 3.
Therefore, the answer is 3.

COMPLEXITY:
Time: O(R * C)
Space: O(R * C)

R = Number of rows
C = Number of columns
"""