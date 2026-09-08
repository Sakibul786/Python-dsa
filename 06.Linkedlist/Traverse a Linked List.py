
# Traverse the linked list and print every node value.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

current = head

while current:
    print(current.data)
    current = current.next