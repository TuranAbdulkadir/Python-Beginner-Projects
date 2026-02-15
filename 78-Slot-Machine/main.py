# Slot Machine
import random
symbols = ["🍒", "🍋", "🍊", "🍇", "💎", "7️⃣"]
balance = 100
print("=== Slot Machine ===")
while balance > 0:
    print(f"\nBalance: ${balance}")
    bet = int(input("Bet (0 to quit): "))
    if bet == 0: break
    if bet > balance: print("Not enough!"); continue
    result = [random.choice(symbols) for _ in range(3)]
    print(f"  | {' | '.join(result)} |")
    if result[0] == result[1] == result[2]:
        win = bet * 10
        print(f"JACKPOT! +${win}")
        balance += win
    elif result[0] == result[1] or result[1] == result[2]:
        win = bet * 2
        print(f"Nice! +${win}")
        balance += win
    else:
        print(f"Lost -${bet}")
        balance -= bet
print(f"\nFinal balance: ${balance}")
