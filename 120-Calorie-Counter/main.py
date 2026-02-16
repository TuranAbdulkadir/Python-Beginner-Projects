# Calorie Counter
foods = {
    "apple": 95, "banana": 105, "bread": 79, "egg": 78, "milk": 149,
    "rice": 206, "chicken": 165, "pasta": 220, "pizza": 285, "salad": 20
}
total = 0
print("=== Calorie Counter ===")
print("Foods:", ", ".join(foods.keys()))
while True:
    food = input("\nFood (or 'done'): ").lower()
    if food == "done": break
    if food in foods:
        total += foods[food]
        print(f"  +{foods[food]} cal (Total: {total})")
    else: print("  Not in database!")
print(f"\nTotal calories: {total}")
print(f"{'Over' if total > 2000 else 'Under'} daily limit (2000)")
