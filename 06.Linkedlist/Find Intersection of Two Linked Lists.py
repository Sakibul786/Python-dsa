# Find the intersection node of two linked lists.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


common1 = Node(8)
common2 = Node(9)

common1.next = common2

head_a = Node(1)
head_a.next = Node(2)
head_a.next.next = common1

head_b = Node(5)
head_b.next = Node(6)
head_b.next.next = common1

pointer_a = head_a
pointer_b = head_b

while pointer_a != pointer_b:
    if pointer_a:
        pointer_a = pointer_a.next
    else:
        pointer_a = head_b

    if pointer_b:
        pointer_b = pointer_b.next
    else:
        pointer_b = head_a

if pointer_a:
    print("Intersection:", pointer_a.data)
else:
    print("No intersection")