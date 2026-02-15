# List Sorter
items = input("Enter items (comma separated): ").split(",")
items = [i.strip() for i in items]
print(f"\nOriginal: {items}")
print(f"A-Z: {sorted(items)}")
print(f"Z-A: {sorted(items, reverse=True)}")
print(f"By length: {sorted(items, key=len)}")
print(f"Total: {len(items)} | Unique: {len(set(items))}")
