# Pig Dice Game
import random
scores = [0, 0]
current = 0
while max(scores) < 100:
    print(f"\nPlayer {current+1}'s turn (Score: {scores[current]})")
    turn_total = 0
    while True:
        action = input("(r)oll or (h)old? ").lower()
        if action == "r":
            roll = random.randint(1, 6)
            print(f"  Rolled: {roll}")
            if roll == 1:
                print("  Pig! Turn over, no points!")
                turn_total = 0; break
            turn_total += roll
            print(f"  Turn total: {turn_total}")
        elif action == "h":
            scores[current] += turn_total
            print(f"  Banked {turn_total}! Total: {scores[current]}")
            break
    current = 1 - current
winner = 1 if scores[0] > scores[1] else 2
print(f"\nPlayer {winner} wins! Final: {scores}")
