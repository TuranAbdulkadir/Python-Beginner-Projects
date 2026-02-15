# Rock Paper Scissors Lizard Spock
import random
choices = ["rock", "paper", "scissors", "lizard", "spock"]
wins = {
    "rock": ["scissors","lizard"], "paper": ["rock","spock"],
    "scissors": ["paper","lizard"], "lizard": ["spock","paper"],
    "spock": ["scissors","rock"]
}
score = {"player": 0, "computer": 0}
while True:
    player = input("\nChoose (rock/paper/scissors/lizard/spock/quit): ").lower()
    if player == "quit": break
    if player not in choices:
        print("Invalid!"); continue
    computer = random.choice(choices)
    print(f"Computer: {computer}")
    if player == computer: print("Tie!")
    elif computer in wins[player]:
        print("You win!"); score["player"] += 1
    else:
        print("Computer wins!"); score["computer"] += 1
    print(f"Score - You: {score['player']} | PC: {score['computer']}")
