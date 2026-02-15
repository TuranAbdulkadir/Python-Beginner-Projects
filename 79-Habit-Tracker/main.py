# Habit Tracker
from datetime import date
habits = {}
while True:
    action = input("\n(a)dd habit, (l)og, (v)iew, (q)uit: ").lower()
    if action == "a":
        habit = input("Habit name: ")
        habits[habit] = []
        print(f"Added '{habit}'")
    elif action == "l":
        if not habits: print("No habits!"); continue
        for h in habits: print(f"  - {h}")
        habit = input("Which habit? ")
        if habit in habits:
            habits[habit].append(str(date.today()))
            print(f"Logged! Streak: {len(habits[habit])} days")
    elif action == "v":
        for h, days in habits.items():
            print(f"  {h}: {len(days)} days logged")
    elif action == "q": break
