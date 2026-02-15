# Flashcard Quiz
flashcards = {
    "Python": "A high-level programming language",
    "HTML": "HyperText Markup Language",
    "CSS": "Cascading Style Sheets",
    "API": "Application Programming Interface",
    "SQL": "Structured Query Language",
    "RAM": "Random Access Memory",
    "CPU": "Central Processing Unit",
    "DNS": "Domain Name System"
}
import random
score = 0
cards = list(flashcards.items())
random.shuffle(cards)
for term, definition in cards:
    print(f"\nDefinition: {definition}")
    ans = input("Term: ").strip()
    if ans.lower() == term.lower():
        print("Correct!"); score += 1
    else:
        print(f"Wrong! Answer: {term}")
print(f"\nScore: {score}/{len(cards)}")
