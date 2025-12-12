print("--- FIZZ BUZZ PRO ---")
# 1'den 100'e kadar sayar.
# 3'e bölünenlere "Fizz", 5'e bölünenlere "Buzz", ikisine de bölünene "FizzBuzz" der.

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("⚡ FizzBuzz")
    elif number % 3 == 0:
        print("🔵 Fizz")
    elif number % 5 == 0:
        print("🟡 Buzz")
    else:
        print(number)