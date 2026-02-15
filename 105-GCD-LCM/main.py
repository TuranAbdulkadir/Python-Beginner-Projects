# GCD & LCM Calculator
import math
a = int(input("First number: "))
b = int(input("Second number: "))
gcd = math.gcd(a, b)
lcm = abs(a * b) // gcd
print(f"\nGCD of {a} and {b}: {gcd}")
print(f"LCM of {a} and {b}: {lcm}")
