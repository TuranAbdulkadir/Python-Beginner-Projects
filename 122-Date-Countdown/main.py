# Countdown by Date
from datetime import date
print("=== Countdown to Date ===")
y = int(input("Year: "))
m = int(input("Month: "))
d = int(input("Day: "))
target = date(y, m, d)
today = date.today()
diff = (target - today).days
if diff > 0:
    print(f"\n{diff} days until {target.strftime('%B %d, %Y')}")
    print(f"That's {diff // 7} weeks and {diff % 7} days")
elif diff == 0:
    print("That's TODAY!")
else:
    print(f"That was {abs(diff)} days ago")
