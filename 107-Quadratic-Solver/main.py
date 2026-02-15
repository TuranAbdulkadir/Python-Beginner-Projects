# Quadratic Equation Solver
import math
print("ax² + bx + c = 0")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
disc = b**2 - 4*a*c
if disc > 0:
    x1 = (-b + math.sqrt(disc)) / (2*a)
    x2 = (-b - math.sqrt(disc)) / (2*a)
    print(f"\nTwo roots: x1={x1:.4f}, x2={x2:.4f}")
elif disc == 0:
    x = -b / (2*a)
    print(f"\nOne root: x={x:.4f}")
else:
    real = -b / (2*a)
    imag = math.sqrt(abs(disc)) / (2*a)
    print(f"\nComplex roots: {real:.4f}±{imag:.4f}i")
