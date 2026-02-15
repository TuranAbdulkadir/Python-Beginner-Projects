# Coin Flip Simulator
import random
heads = tails = 0
n = int(input("How many flips? "))
for _ in range(n):
    if random.random() < 0.5:
        heads += 1
    else:
        tails += 1
print(f"\nResults ({n} flips):")
print(f"Heads: {heads} ({heads/n*100:.1f}%)")
print(f"Tails: {tails} ({tails/n*100:.1f}%)")
