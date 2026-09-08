
# Insert a new node at the beginning of the linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

new_node = Node(5)

new_node.next = head
head = new_node

current = head

while current:
    print(current.data)
    current = current.next