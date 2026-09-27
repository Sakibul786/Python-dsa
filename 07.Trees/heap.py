import heapq


# Question 1:
# Find the 3 largest elements from the list.

numbers = [10, 5, 20, 8, 15, 30]
k = 3

heap = []

for number in numbers:
    heapq.heappush(heap, number)

    if len(heap) > k:
        heapq.heappop(heap)

print("Question 1 Answer:", heap)
# Answer: [15, 30, 20]



# Find the 3 smallest elements from the list.

numbers = [10, 5, 20, 8, 15, 30]
k = 3

heapq.heapify(numbers)

result = []

for _ in range(k):
    result.append(heapq.heappop(numbers))

print("Question 2 Answer:", result)



# Question 3:
# Find the 2nd largest element from the list.

numbers = [10, 5, 20, 8, 15, 30]
k = 2

heap = []

for number in numbers:
    heapq.heappush(heap, number)

    if len(heap) > k:
        heapq.heappop(heap)

print("Question 3 Answer:", heap[0])



# Question 4:
# Find the 2nd smallest element from the list.

numbers = [10, 5, 20, 8, 15, 30]
k = 2

heapq.heapify(numbers)

for _ in range(k - 1):
    heapq.heappop(numbers)

print("Question 4 Answer:", heapq.heappop(numbers))



# Question 5:
# Sort the list using a Min Heap.

numbers = [40, 10, 30, 20, 50]

heapq.heapify(numbers)

sorted_numbers = []

while numbers:
    sorted_numbers.append(heapq.heappop(numbers))

print("Question 5 Answer:", sorted_numbers)
