# Quiz Game
questions = [
    {"q": "What is the capital of Turkey?", "options": ["Istanbul","Ankara","Izmir","Bursa"], "answer": 1},
    {"q": "What is 2^10?", "options": ["512","1024","2048","4096"], "answer": 1},
    {"q": "Who created Python?", "options": ["Bill Gates","Guido van Rossum","Linus Torvalds","James Gosling"], "answer": 1},
    {"q": "What does HTML stand for?", "options": ["Hyper Text Markup Language","High Tech ML","Home Tool Markup Language","None"], "answer": 0},
    {"q": "Which planet is closest to the Sun?", "options": ["Venus","Earth","Mercury","Mars"], "answer": 2},
]
score = 0
for i, q in enumerate(questions, 1):
    print(f"\nQ{i}: {q['q']}")
    for j, opt in enumerate(q["options"]):
        print(f"  {j+1}. {opt}")
    ans = int(input("Your answer (1-4): ")) - 1
    if ans == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Answer: {q['options'][q['answer']]}")
print(f"\nScore: {score}/{len(questions)}")
