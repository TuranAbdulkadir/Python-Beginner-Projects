# Unit Price Comparator
print("=== Unit Price Comparator ===")
items = []
while True:
    name = input("\nProduct name (or 'done'): ")
    if name.lower() == "done": break
    price = float(input("Price: $"))
    qty = float(input("Quantity/Weight: "))
    unit = input("Unit (g/ml/pcs): ")
    unit_price = price / qty
    items.append({"name": name, "price": price, "qty": qty, "unit": unit, "unit_price": unit_price})

if items:
    items.sort(key=lambda x: x["unit_price"])
    print("\n=== Best Value ===")
    for i, item in enumerate(items, 1):
        marker = "👑 BEST" if i == 1 else ""
        print(f"  {i}. {item['name']}: ${item['unit_price']:.4f}/{item['unit']} {marker}")
