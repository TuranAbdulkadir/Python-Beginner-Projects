# Hangman Game
import random
words = ["python","javascript","programming","algorithm","developer","function","variable","database"]
word = random.choice(words)
guessed = set()
lives = 6
while lives > 0:
    display = " ".join(c if c in guessed else "_" for c in word)
    print(f"\n{display}  (Lives: {'❤️'*lives})")
    if "_" not in display:
        print("You WIN!"); break
    guess = input("Guess a letter: ").lower()
    if guess in guessed: print("Already guessed!"); continue
    guessed.add(guess)
    if guess not in word:
        lives -= 1
        print("Wrong!")
else:
    print(f"\nGame Over! Word was: {word}")
