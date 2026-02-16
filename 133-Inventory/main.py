# Inventory System
inventory = {}
while True:
    action = input("\n(a)dd, (r)emove, (u)pdate, (v)iew, (q)uit: ").lower()
    if action == "a":
        item = input("Item: ")
        qty = int(input("Quantity: "))
        price = float(input("Price: $"))
        inventory[item] = {"qty": qty, "price": price}
        print(f"Added {item}")
    elif action == "r":
        item = input("Item: ")
        if item in inventory: del inventory[item]; print("Removed!")
        else: print("Not found!")
    elif action == "u":
        item = input("Item: ")
        if item in inventory:
            qty = int(input("New quantity: "))
            inventory[item]["qty"] = qty
            print("Updated!")
    elif action == "v":
        total = 0
        for item, info in inventory.items():
            val = info["qty"] * info["price"]
            total += val
            print(f"  {item}: {info['qty']}x ${info['price']:.2f} = ${val:.2f}")
        print(f"  Total value: ${total:.2f}")
    elif action == "q": break
