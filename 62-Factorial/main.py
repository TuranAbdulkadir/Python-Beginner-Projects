# Factorial Calculator
def factorial(n):
    if n <= 1: return 1
    return n * factorial(n - 1)

num = int(input("Enter a number: "))
result = factorial(num)
print(f"\n{num}! = {result}")
print(f"Digits: {len(str(result))}")
