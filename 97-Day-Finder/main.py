# Day of Week Finder
from datetime import date
y = int(input("Year: "))
m = int(input("Month: "))
d = int(input("Day: "))
day = date(y, m, d)
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print(f"\n{day.strftime('%B %d, %Y')} was a {days[day.weekday()]}")
