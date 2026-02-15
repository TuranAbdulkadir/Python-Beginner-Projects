# Fortune Cookie
import random
fortunes = [
    "A beautiful day awaits you tomorrow.",
    "Your code will compile on the first try.",
    "Success is just around the corner.",
    "A new opportunity will present itself soon.",
    "Your debugging skills will save the day.",
    "Today is a good day to learn something new.",
    "Great things come from small projects.",
    "Your commit history tells a great story.",
    "The bug you're looking for is on line 42.",
    "Stack Overflow will have your answer."
]
print("🥠 Fortune Cookie Says:")
print(f"\n  \"{random.choice(fortunes)}\"")
print(f"\n  Lucky numbers: {sorted(random.sample(range(1,50), 6))}")
