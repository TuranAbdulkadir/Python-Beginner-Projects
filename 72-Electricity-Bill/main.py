# Electricity Bill Calculator
units = float(input("Enter units consumed: "))
if units <= 100: rate = 1.5
elif units <= 200: rate = 2.5
elif units <= 300: rate = 4.0
else: rate = 6.0
bill = units * rate
tax = bill * 0.18
total = bill + tax
print(f"\nUnits: {units}")
print(f"Rate: ${rate}/unit")
print(f"Bill: ${bill:.2f}")
print(f"Tax (18%): ${tax:.2f}")
print(f"Total: ${total:.2f}")
