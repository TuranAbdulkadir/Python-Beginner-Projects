# Student Grade Manager
students = {}
while True:
    action = input("\n(a)dd, (g)rades, (r)eport, (q)uit: ").lower()
    if action == "a":
        name = input("Student name: ")
        grade = float(input("Grade (0-100): "))
        students.setdefault(name, []).append(grade)
        print(f"Added grade {grade} for {name}")
    elif action == "g":
        name = input("Student name: ")
        if name in students:
            grades = students[name]
            print(f"Grades: {grades} | Avg: {sum(grades)/len(grades):.1f}")
        else:
            print("Student not found!")
    elif action == "r":
        for name, grades in students.items():
            avg = sum(grades) / len(grades)
            letter = "A" if avg >= 90 else "B" if avg >= 80 else "C" if avg >= 70 else "D" if avg >= 60 else "F"
            print(f"  {name}: Avg={avg:.1f} ({letter})")
    elif action == "q": break
