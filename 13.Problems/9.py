
"""
Problem: Course Schedule

Description:
There are num_courses courses numbered from 0 to num_courses - 1.

You are given prerequisites where:
prerequisites[i] = [a, b]

This means you must complete course b before taking course a.

Determine whether it is possible to finish all courses.

Example 1:
Input:
num_courses = 2
prerequisites = [[1, 0]]

Output:
True

Explanation:
Course 0 must be completed before course 1.
So, both courses can be completed.

Example 2:
Input:
num_courses = 2
prerequisites = [[1, 0], [0, 1]]

Output:
False

Explanation:
Course 1 requires course 0, and course 0 requires course 1.
This creates a cycle, so completing all courses is impossible.

Approach: Topological Sorting (Kahn's Algorithm)

1. Build a directed graph.
2. Calculate the in-degree of every course.
   In-degree means the number of prerequisites for a course.
3. Add all courses with in-degree 0 to a queue.
4. Process courses from the queue:
   - Mark the course as completed.
   - Reduce the in-degree of its dependent courses.
   - If a dependent course reaches in-degree 0, add it to the queue.
5. If all courses are processed, return True.
   Otherwise, a cycle exists and return False.

Solution:
"""

from collections import deque


def can_finish(num_courses, prerequisites):
    graph = [[] for _ in range(num_courses)]
    in_degree = [0] * num_courses

    # Build the graph and calculate in-degrees.
    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)
        in_degree[course] += 1

    # Add courses that have no prerequisites.
    queue = deque()

    for course in range(num_courses):
        if in_degree[course] == 0:
            queue.append(course)

    completed = 0

    # Process courses using BFS.
    while queue:
        current = queue.popleft()
        completed += 1

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1

            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return completed == num_courses


"""
Dry Run:

num_courses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]

Graph:
0 -> 1
0 -> 2
1 -> 3
2 -> 3

Initial in-degree:
Course 0: 0
Course 1: 1
Course 2: 1
Course 3: 2

Queue: [0]

Step 1:
Process course 0.
Courses 1 and 2 become ready.
Queue: [1, 2]

Step 2:
Process course 1.
Course 3 has in-degree 1.
Queue: [2]

Step 3:
Process course 2.
Course 3 has in-degree 0.
Queue: [3]

Step 4:
Process course 3.

Completed courses = 4
Total courses = 4

Result: True

Test Cases:
"""

test_cases = [
    (2, [[1, 0]], True),
    (2, [[1, 0], [0, 1]], False),
    (4, [[1, 0], [2, 0], [3, 1], [3, 2]], True),
    (3, [], True),
    (3, [[1, 0], [2, 1], [0, 2]], False),
    (1, [], True),
    (4, [[1, 0], [2, 0], [3, 2]], True)
]

for num_courses, prerequisites, expected in test_cases:
    result = can_finish(num_courses, prerequisites)

    print("Courses:", num_courses)
    print("Prerequisites:", prerequisites)
    print("Output:", result)
    print("Expected:", expected)
    print("Passed:", result == expected)
    print()


"""
Expected Outputs:

True
False
True
True
False
True
True

Time Complexity: O(V + E)
Space Complexity: O(V + E)

Where:
V = Number of courses
E = Number of prerequisite relationships

Interview Follow-up:
Can you return the actual valid course order instead of only True or False?

Hint:
Modify Kahn's Algorithm to store each processed course in a list.
If the list contains all courses, return that list.
Otherwise, a cycle exists.
"""
