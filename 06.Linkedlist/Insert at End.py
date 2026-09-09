# Insert a new node at the end of the linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

new_node = Node(40)

current = head

while current.next:
    current = current.next

current.next = new_node

current = head

while current:
    print(current.data)
    current = current.next