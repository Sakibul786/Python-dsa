
# Search for a target value in the linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

target = 30

current = head
found = False

while current:
    if current.data == target:
        found = True
        break

    current = current.next

print(found)