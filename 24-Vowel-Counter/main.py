text = input("Enter text: ").lower()
count = 0
vowels = "aeiou"
for char in text:
    if char in vowels:
        count += 1
print(f"Total Vowels: {count}")