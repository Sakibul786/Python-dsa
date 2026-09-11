
# Merge two sorted linked lists into one sorted linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


list1 = Node(1)
list1.next = Node(3)
list1.next.next = Node(5)

list2 = Node(2)
list2.next = Node(4)
list2.next.next = Node(6)

dummy = Node(0)
current = dummy

first = list1
second = list2

while first and second:
    if first.data <= second.data:
        current.next = first
        first = first.next
    else:
        current.next = second
        second = second.next

    current = current.next

if first:
    current.next = first
else:
    current.next = second

head = dummy.next

current = head

while current:
    print(current.data)
    current = current.next