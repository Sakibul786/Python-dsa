"""
PROBLEM:
Given a 2D grid containing "1" (land) and "0" (water),
count the number of islands.

An island consists of connected land cells.
Only horizontal and vertical connections are allowed.

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
1. Visit every cell in the grid.
2. When an unvisited land cell is found, increment the island count.
3. Use BFS to visit all connected land cells.
4. Continue until every cell has been checked.

SOLUTION:
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


# TEST CASE
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

# ANSWER
print("Number of islands:", count_islands(grid))




"""
EXPLANATION:
- The first four connected land cells form Island 1.
- The land cell at row 2, column 2 forms Island 2.
- The last two connected land cells form Island 3.
- Therefore, the total number of islands is 3.

COMPLEXITY:
Time: O(R * C)
Space: O(R * C)

R = Number of rows
C = Number of columns
"""