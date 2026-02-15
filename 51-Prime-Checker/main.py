# Prime Number Checker
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is PRIME!")
else:
    print(f"{num} is NOT prime")
    factors = [i for i in range(1, num+1) if num % i == 0]
    print(f"Factors: {factors}")

print(f"\nPrimes up to {num}: {[x for x in range(2, num+1) if is_prime(x)]}")
