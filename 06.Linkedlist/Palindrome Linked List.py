
# Check whether the linked list is a palindrome.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(1)

values = []

current = head

while current:
    values.append(current.data)
    current = current.next

print(values == values[::-1])