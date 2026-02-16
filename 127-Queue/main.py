# Queue Implementation
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item): self.items.append(item)
    def dequeue(self): return self.items.pop(0) if self.items else None
    def front(self): return self.items[0] if self.items else None
    def size(self): return len(self.items)

queue = Queue()
while True:
    action = input("\n(e)nqueue, (d)equeue, (f)ront, (s)ize, (q)uit: ").lower()
    if action == "e":
        val = input("Value: ")
        queue.enqueue(val)
        print(f"Added: {val}")
    elif action == "d":
        val = queue.dequeue()
        print(f"Removed: {val}" if val else "Queue empty!")
    elif action == "f":
        val = queue.front()
        print(f"Front: {val}" if val else "Queue empty!")
    elif action == "s": print(f"Size: {queue.size()}")
    elif action == "q": break
