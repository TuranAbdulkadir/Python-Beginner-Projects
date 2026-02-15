# Percentage Calculator
print("=== Percentage Calculator ===")
print("1. What is X% of Y?")
print("2. X is what % of Y?")
print("3. % change from X to Y")
choice = int(input("Choose: "))
if choice == 1:
    x = float(input("X%: "))
    y = float(input("of Y: "))
    print(f"\n{x}% of {y} = {y * x / 100:.2f}")
elif choice == 2:
    x = float(input("X: "))
    y = float(input("of Y: "))
    print(f"\n{x} is {x/y*100:.2f}% of {y}")
elif choice == 3:
    x = float(input("From X: "))
    y = float(input("To Y: "))
    change = ((y - x) / x) * 100
    print(f"\nChange: {change:+.2f}%")
