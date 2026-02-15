# Contact Book
contacts = {}
while True:
    action = input("\n(a)dd, (s)earch, (l)ist, (d)elete, (q)uit: ").lower()
    if action == "a":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
        print(f"Added {name}")
    elif action == "s":
        name = input("Search name: ")
        if name in contacts: print(f"{name}: {contacts[name]}")
        else: print("Not found!")
    elif action == "l":
        for name, phone in sorted(contacts.items()):
            print(f"  {name}: {phone}")
    elif action == "d":
        name = input("Name to delete: ")
        if name in contacts: del contacts[name]; print("Deleted!")
        else: print("Not found!")
    elif action == "q": break
