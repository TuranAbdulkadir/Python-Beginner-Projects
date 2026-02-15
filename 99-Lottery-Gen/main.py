# Lottery Number Generator
import random
print("=== Lottery Number Generator ===")
main = sorted(random.sample(range(1, 50), 6))
bonus = random.randint(1, 10)
print(f"\nYour numbers: {main}")
print(f"Bonus ball: {bonus}")
print(f"\nGood luck! 🍀")
