# Shopping List Manager
shopping_list = []
print("=== Shopping List ===")
while True:
    action = input("\n(a)dd, (r)emove, (v)iew, (q)uit: ").lower()
    if action == "a":
        item = input("Item: ")
        shopping_list.append(item)
        print(f"Added: {item}")
    elif action == "r":
        item = input("Item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"Removed: {item}")
        else:
            print("Not found!")
    elif action == "v":
        if shopping_list:
            for i, item in enumerate(shopping_list, 1):
                print(f"  {i}. {item}")
        else:
            print("  List is empty!")
    elif action == "q":
        print(f"Total items: {len(shopping_list)}")
        break
