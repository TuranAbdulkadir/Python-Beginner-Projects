import random
choices = ['rock','paper','scissors']
comp = random.choice(choices)
user = input("rock/paper/scissors: ")
print(f"Computer: {comp}")
if user == comp: print("Tie")
elif (user=='rock' and comp=='scissors') or (user=='paper' and comp=='rock') or (user=='scissors' and comp=='paper'): print("Win")
else: print("Lose")