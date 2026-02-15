# Word Scramble Game
import random
words = ["python","coding","program","function","variable","string","integer","boolean","module","library"]
score = 0
for word in random.sample(words, 5):
    scrambled = "".join(random.sample(word, len(word)))
    print(f"\nScrambled: {scrambled}")
    guess = input("Your guess: ").lower()
    if guess == word: print("Correct!"); score += 1
    else: print(f"Wrong! It was: {word}")
print(f"\nScore: {score}/5")
