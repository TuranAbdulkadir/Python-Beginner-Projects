# Typing Speed Test
import time
sentences = [
    "the quick brown fox jumps over the lazy dog",
    "python is the best programming language ever",
    "coding is fun and rewarding for everyone"
]
import random
sentence = random.choice(sentences)
print(f"\nType this:\n  {sentence}\n")
input("Press Enter when ready...")
start = time.time()
typed = input("> ")
elapsed = time.time() - start
words = len(sentence.split())
wpm = (words / elapsed) * 60
correct = sum(a == b for a, b in zip(typed, sentence))
accuracy = (correct / len(sentence)) * 100
print(f"\nTime: {elapsed:.1f}s")
print(f"Speed: {wpm:.0f} WPM")
print(f"Accuracy: {accuracy:.0f}%")
