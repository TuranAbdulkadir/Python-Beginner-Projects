# Tip Calculator - Split bills easily
bill = float(input("Total bill amount: $"))
tip_pct = int(input("Tip percentage (10/12/15/20): "))
people = int(input("Number of people splitting: "))

tip = bill * (tip_pct / 100)
total = bill + tip
per_person = total / people

print(f"\n{'='*30}")
print(f"  Bill:    ${bill:.2f}")
print(f"  Tip:     ${tip:.2f} ({tip_pct}%)")
print(f"  Total:   ${total:.2f}")
print(f"  Per person: ${per_person:.2f}")
print(f"{'='*30}")
