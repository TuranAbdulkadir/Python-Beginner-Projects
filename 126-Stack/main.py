# Stack Implementation
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item): self.items.append(item)
    def pop(self): return self.items.pop() if self.items else None
    def peek(self): return self.items[-1] if self.items else None
    def size(self): return len(self.items)
    def is_empty(self): return len(self.items) == 0

stack = Stack()
while True:
    action = input("\n(p)ush, (o)pop, (k)peek, (s)ize, (q)uit: ").lower()
    if action == "p":
        val = input("Value: ")
        stack.push(val)
        print(f"Pushed: {val}")
    elif action == "o":
        val = stack.pop()
        print(f"Popped: {val}" if val else "Stack empty!")
    elif action == "k":
        val = stack.peek()
        print(f"Top: {val}" if val else "Stack empty!")
    elif action == "s":
        print(f"Size: {stack.size()}")
    elif action == "q": break
