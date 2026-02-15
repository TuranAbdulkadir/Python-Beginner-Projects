# Distance Calculator
import math
x1 = float(input("Point 1 - X: "))
y1 = float(input("Point 1 - Y: "))
x2 = float(input("Point 2 - X: "))
y2 = float(input("Point 2 - Y: "))
dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
manhattan = abs(x2-x1) + abs(y2-y1)
print(f"\nEuclidean distance: {dist:.4f}")
print(f"Manhattan distance: {manhattan:.4f}")
