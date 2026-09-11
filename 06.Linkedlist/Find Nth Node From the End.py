
# Find the nth node from the end of the linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

n = 2

first = head
second = head

for _ in range(n):
    if first is None:
        break
    first = first.next

while first:
    first = first.next
    second = second.next

print("Nth node from end:", second.data)