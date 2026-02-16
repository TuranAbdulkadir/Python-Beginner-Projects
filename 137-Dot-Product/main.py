# Dot Product Calculator
v1 = input("Vector 1 (comma separated): ").split(",")
v2 = input("Vector 2 (comma separated): ").split(",")
v1 = [float(x) for x in v1]
v2 = [float(x) for x in v2]
if len(v1) != len(v2):
    print("Vectors must have same length!")
else:
    dot = sum(a*b for a, b in zip(v1, v2))
    mag1 = sum(x**2 for x in v1) ** 0.5
    mag2 = sum(x**2 for x in v2) ** 0.5
    print(f"\nVector 1: {v1}")
    print(f"Vector 2: {v2}")
    print(f"Dot product: {dot}")
    print(f"|V1|: {mag1:.4f}")
    print(f"|V2|: {mag2:.4f}")
