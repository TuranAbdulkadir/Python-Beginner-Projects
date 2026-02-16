# Blackjack Card Game
import random
def deal(): return random.randint(1, 11)
def hand_value(hand): return sum(hand)

print("=== Blackjack ===")
player = [deal(), deal()]
dealer = [deal(), deal()]
print(f"Your hand: {player} = {hand_value(player)}")
print(f"Dealer shows: [{dealer[0]}, ?]")

while hand_value(player) < 21:
    action = input("\n(h)it or (s)tand? ").lower()
    if action == "h":
        player.append(deal())
        print(f"Your hand: {player} = {hand_value(player)}")
    else:
        break

if hand_value(player) > 21:
    print("BUST! You lose! 💥")
else:
    print(f"\nDealer's hand: {dealer} = {hand_value(dealer)}")
    while hand_value(dealer) < 17:
        dealer.append(deal())
        print(f"Dealer hits: {dealer} = {hand_value(dealer)}")
    if hand_value(dealer) > 21:
        print("Dealer busts! YOU WIN! 🎉")
    elif hand_value(player) > hand_value(dealer):
        print("YOU WIN! 🎉")
    elif hand_value(player) < hand_value(dealer):
        print("Dealer wins! 😞")
    else:
        print("Push! (Tie) 🤝")
