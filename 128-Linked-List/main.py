# Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        node = Node(data)
        if not self.head: self.head = node; return
        curr = self.head
        while curr.next: curr = curr.next
        curr.next = node
    def display(self):
        curr = self.head
        items = []
        while curr:
            items.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(items) + " -> None")
    def length(self):
        count, curr = 0, self.head
        while curr: count += 1; curr = curr.next
        return count

ll = LinkedList()
for x in [10, 20, 30, 40, 50]:
    ll.append(x)
print("Linked List:")
ll.display()
print(f"Length: {ll.length()}")
