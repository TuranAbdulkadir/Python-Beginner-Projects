# Interest Calculator
principal = float(input("Principal amount: $"))
rate = float(input("Annual rate (%): "))
years = int(input("Years: "))
simple = principal * (1 + rate/100 * years)
compound = principal * (1 + rate/100) ** years
print(f"\nSimple Interest: ${simple:.2f}")
print(f"Compound Interest: ${compound:.2f}")
print(f"Difference: ${compound - simple:.2f}")
