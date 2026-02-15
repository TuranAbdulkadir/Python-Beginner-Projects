# Age Calculator
from datetime import date

birth_year = int(input("Birth year: "))
birth_month = int(input("Birth month: "))
birth_day = int(input("Birth day: "))

today = date.today()
birth = date(birth_year, birth_month, birth_day)
age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
days = (today - birth).days

print(f"\nYou are {age} years old")
print(f"Alive for {days:,} days")
print(f"That is {days * 24:,} hours!")
