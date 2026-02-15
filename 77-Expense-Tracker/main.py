# Expense Tracker
expenses = []
while True:
    action = input("\n(a)dd, (v)iew, (s)ummary, (q)uit: ").lower()
    if action == "a":
        cat = input("Category: ")
        amt = float(input("Amount: $"))
        expenses.append({"cat": cat, "amt": amt})
        print("Added!")
    elif action == "v":
        for i, e in enumerate(expenses, 1):
            print(f"  {i}. {e['cat']}: ${e['amt']:.2f}")
    elif action == "s":
        total = sum(e['amt'] for e in expenses)
        cats = {}
        for e in expenses:
            cats[e['cat']] = cats.get(e['cat'], 0) + e['amt']
        print(f"\nTotal: ${total:.2f}")
        for c, a in cats.items():
            print(f"  {c}: ${a:.2f}")
    elif action == "q": break
