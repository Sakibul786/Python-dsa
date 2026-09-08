
# Reverse the linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

previous = None
current = head

while current:
    next_node = current.next
    current.next = previous

    previous = current
    current = next_node

head = previous

current = head

while current:
    print(current.data)
    current = current.next