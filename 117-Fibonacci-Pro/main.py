# Fibonacci Sequence Generator
n = int(input("How many terms? "))
a, b = 0, 1
fib = []
for _ in range(n):
    fib.append(a)
    a, b = b, a + b
print(f"\nFibonacci ({n} terms): {fib}")
print(f"Sum: {sum(fib)}")
print(f"Golden ratio approx: {fib[-1]/fib[-2]:.6f}")
