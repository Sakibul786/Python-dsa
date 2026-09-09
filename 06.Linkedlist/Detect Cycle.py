# Detect whether the linked list contains a cycle.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

head.next = node2
node2.next = node3
node3.next = node4

# Create a cycle.
node4.next = node2

slow = head
fast = head

has_cycle = False

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        has_cycle = True
        break

print(has_cycle)