# GPA Calculator
print("=== GPA Calculator ===")
grades = {"A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7, "C+": 2.3, "C": 2.0, "C-": 1.7, "D": 1.0, "F": 0.0}
total_points = 0
total_credits = 0
while True:
    grade = input("Grade (or 'done'): ").upper()
    if grade == "DONE": break
    if grade not in grades:
        print("Invalid grade!")
        continue
    credits = int(input("Credits: "))
    total_points += grades[grade] * credits
    total_credits += credits

if total_credits > 0:
    gpa = total_points / total_credits
    print(f"\nGPA: {gpa:.2f}")
    print(f"Total Credits: {total_credits}")
