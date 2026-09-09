# Remove the first node from the linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

head = head.next

current = head

while current:
    print(current.data)
    current = current.next