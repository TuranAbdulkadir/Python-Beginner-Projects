# Math Quiz Generator
import random
score = 0
rounds = 10
ops = ["+", "-", "*"]
for i in range(1, rounds+1):
    a = random.randint(1, 50)
    b = random.randint(1, 20)
    op = random.choice(ops)
    answer = eval(f"{a}{op}{b}")
    print(f"\nQ{i}: {a} {op} {b} = ?")
    guess = int(input("Answer: "))
    if guess == answer: print("Correct!"); score += 1
    else: print(f"Wrong! Answer: {answer}")
pct = score / rounds * 100
print(f"\nScore: {score}/{rounds} ({pct:.0f}%)")
grade = "A" if pct >= 90 else "B" if pct >= 80 else "C" if pct >= 70 else "F"
print(f"Grade: {grade}")
