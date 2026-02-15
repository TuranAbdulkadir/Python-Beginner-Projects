# Todo List with Priority
todos = []
while True:
    action = input("\n(a)dd, (v)iew, (c)omplete, (q)uit: ").lower()
    if action == "a":
        task = input("Task: ")
        priority = input("Priority (high/med/low): ").lower()
        todos.append({"task": task, "priority": priority, "done": False})
        print("Added!")
    elif action == "v":
        order = {"high": 0, "med": 1, "low": 2}
        for i, t in enumerate(sorted(todos, key=lambda x: order.get(x['priority'], 3)), 1):
            status = "✅" if t['done'] else "⬜"
            print(f"  {status} [{t['priority'].upper()}] {t['task']}")
    elif action == "c":
        idx = int(input("Task number: ")) - 1
        if 0 <= idx < len(todos):
            todos[idx]['done'] = True
            print("Completed!")
    elif action == "q": break
