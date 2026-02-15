# Rock Paper Scissors Stats
import random
wins = losses = ties = 0
choices = ["rock", "paper", "scissors"]
beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
while True:
    player = input("\nrock/paper/scissors/quit: ").lower()
    if player == "quit": break
    if player not in choices: continue
    computer = random.choice(choices)
    print(f"Computer: {computer}")
    if player == computer: print("Tie!"); ties += 1
    elif beats[player] == computer: print("You win!"); wins += 1
    else: print("You lose!"); losses += 1
    total = wins + losses + ties
    print(f"W:{wins} L:{losses} T:{ties} | Win rate: {wins/total*100:.0f}%")
