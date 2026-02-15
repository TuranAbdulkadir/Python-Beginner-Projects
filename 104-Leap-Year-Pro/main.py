# Leap Year Checker Pro
year = int(input("Enter year: "))
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
days = 366 if is_leap else 365
print(f"\n{year} {'IS' if is_leap else 'is NOT'} a leap year")
print(f"Days in {year}: {days}")
print(f"February has {'29' if is_leap else '28'} days")
