
# Question 1:
# Select the maximum number of non-overlapping activities.

def activity_selection(activities):
    activities = sorted(activities, key=lambda x: x[1])

    selected = []
    last_finish = float("-inf")

    for start, finish in activities:
        if start >= last_finish:
            selected.append((start, finish))
            last_finish = finish

    return selected


print("Activities:", activity_selection([
    (1, 3), (2, 5), (4, 6), (6, 7)
]))


# Question 2:
# Maximize value in Fractional Knapsack.

def fractional_knapsack(items, capacity):
    items = sorted(
        items,
        key=lambda x: x[1] / x[0],
        reverse=True
    )

    total_value = 0.0

    for weight, value in items:
        if capacity <= 0:
            break

        taken = min(weight, capacity)
        total_value += taken * value / weight
        capacity -= taken

    return total_value


print("Fractional knapsack:", fractional_knapsack(
    [(10, 60), (20, 100), (30, 120)], 50
))


# Question 3:
# Schedule jobs to maximize total profit.
# Each job takes one time slot.

def job_sequencing(jobs):
    jobs = sorted(jobs, key=lambda x: x[2], reverse=True)

    max_deadline = max((job[1] for job in jobs), default=0)
    slots = [None] * (max_deadline + 1)
    total_profit = 0

    for job_id, deadline, profit in jobs:
        for slot in range(min(deadline, max_deadline), 0, -1):
            if slots[slot] is None:
                slots[slot] = job_id
                total_profit += profit
                break

    schedule = [job for job in slots[1:] if job is not None]
    return schedule, total_profit


print("Job schedule:", job_sequencing([
    ("A", 2, 100),
    ("B", 1, 19),
    ("C", 2, 27),
    ("D", 1, 25),
    ("E", 3, 15)
]))


# Question 4:
# Merge all overlapping intervals.

def merge_intervals(intervals):
    if not intervals:
        return []

    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0][:]]

    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    return merged


print("Merged intervals:", merge_intervals([
    [1, 3], [2, 6], [8, 10], [9, 12]
]))


# Question 5:
# Explain Greedy versus Dynamic Programming.
#
# Answer:
# Greedy makes a locally optimal choice at each step.
# Dynamic Programming compares and combines subproblem results.
# Greedy is appropriate only when its choice strategy is proven
# to produce an optimal solution for the given problem.


# Question 6:
# State the time complexities.
#
# Answer:
# Activity Selection: O(n log n)
# Fractional Knapsack: O(n log n)
# Job Sequencing: O(n log n + nD)
# Merge Intervals: O(n log n)
#
# D is the maximum job deadline.
