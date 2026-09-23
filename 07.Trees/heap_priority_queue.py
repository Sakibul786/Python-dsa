# Question 1: Remove and return the smallest value from a Min Heap.

import heapq

heap = [10, 20, 30, 40, 50]

heapq.heapify(heap)

smallest = heapq.heappop(heap)

print("Removed:", smallest)
print("Heap:", heap)

# Question 2: Find the smallest value without removing it.

import heapq

heap = [30, 10, 20, 50, 40]

heapq.heapify(heap)

print("Minimum:", heap[0])


# Question 3: Convert a list into a Min Heap.

import heapq

numbers = [50, 20, 40, 10, 30]

heapq.heapify(numbers)

print("Min Heap:", numbers)
print("Minimum:", numbers[0])

# Question 4: Implement a Max Heap using heapq.

import heapq

heap = []

heapq.heappush(heap, -50)
heapq.heappush(heap, -30)
heapq.heappush(heap, -40)
heapq.heappush(heap, -10)

maximum = -heapq.heappop(heap)

print("Maximum:", maximum)



# Question 5: Implement a priority queue using heapq.

import heapq

priority_queue = []

heapq.heappush(priority_queue, (3, "Task A"))
heapq.heappush(priority_queue, (1, "Task B"))
heapq.heappush(priority_queue, (2, "Task C"))

while priority_queue:
    priority, task = heapq.heappop(priority_queue)
    print(priority, task)

