# Area Calculator
import math
print("=== Area Calculator ===")
print("1. Circle  2. Rectangle  3. Triangle  4. Square")
choice = int(input("Choose shape: "))
if choice == 1:
    r = float(input("Radius: "))
    print(f"Area: {math.pi * r**2:.2f}")
elif choice == 2:
    l = float(input("Length: "))
    w = float(input("Width: "))
    print(f"Area: {l * w:.2f}")
elif choice == 3:
    b = float(input("Base: "))
    h = float(input("Height: "))
    print(f"Area: {0.5 * b * h:.2f}")
elif choice == 4:
    s = float(input("Side: "))
    print(f"Area: {s**2:.2f}")
