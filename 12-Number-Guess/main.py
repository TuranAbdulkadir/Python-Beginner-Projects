import random
target = random.randint(1,10)
while True:
    guess = int(input("Guess (1-10): "))
    if guess == target: print("Correct!"); break
    print("Try again.")