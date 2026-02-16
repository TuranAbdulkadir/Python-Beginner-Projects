# Number Magic Tricks
import random
print("=== Number Magic ===")
print("Think of a number between 1-63\n")
cards = []
for i in range(6):
    card = [j for j in range(1, 64) if j & (1 << i)]
    cards.append(card)
    print(f"Card {i+1}: {card[:8]}...")
    ans = input("Is your number here? (y/n): ").lower()
    if ans == "y":
        if not hasattr(Number, 'val'): 
            Number = type('Number', (), {'val': 0})()
        Number.val += (1 << i)

# Simple version
num = 0
for i, card in enumerate(cards):
    print(f"\nCard {i+1}: {card[:10]}...")
    if input("Is your number here? (y/n): ").lower() == "y":
        num += (1 << i)
print(f"\nYour number is: {num}!")
