# Delete the first node containing the target value.

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

while current and current.next:
    if current.next.data == target:
        current.next = current.next.next
        break

    current = current.next

current = head

while current:
    print(current.data)
    current = current.next