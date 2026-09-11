
# Remove duplicate values from a sorted linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)
head.next = Node(20)
head.next.next = Node(20)
head.next.next.next = Node(30)
head.next.next.next.next = Node(30)
head.next.next.next.next.next = Node(40)

current = head

while current and current.next:
    if current.data == current.next.data:
        current.next = current.next.next
    else:
        current = current.next

current = head

while current:
    print(current.data)
    current = current.next