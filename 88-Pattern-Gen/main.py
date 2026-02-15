# Number Pattern Generator
n = int(input("Enter rows: "))
print("\n=== Pyramid ===")
for i in range(1, n+1):
    print(" " * (n-i) + "* " * i)
print("\n=== Diamond ===")
for i in range(1, n+1):
    print(" " * (n-i) + "* " * i)
for i in range(n-1, 0, -1):
    print(" " * (n-i) + "* " * i)
print("\n=== Numbers ===")
for i in range(1, n+1):
    print(" ".join(str(x) for x in range(1, i+1)))
