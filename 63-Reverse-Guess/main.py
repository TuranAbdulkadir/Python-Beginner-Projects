# Guess the Number - Computer guesses YOUR number
low, high = 1, 100
print(f"Think of a number between {low} and {high}")
input("Press Enter when ready...")

attempts = 0
while True:
    guess = (low + high) // 2
    attempts += 1
    print(f"\nMy guess: {guess}")
    ans = input("Too (h)igh, too (l)ow, or (c)orrect? ").lower()
    if ans == "c":
        print(f"\nI got it in {attempts} attempts!")
        break
    elif ans == "h":
        high = guess - 1
    elif ans == "l":
        low = guess + 1
