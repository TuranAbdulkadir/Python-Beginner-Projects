# Text Reverser
text = input("Enter text: ")
print(f"\nReversed: {text[::-1]}")
print(f"Word reversed: {' '.join(text.split()[::-1])}")
print(f"Is palindrome: {text.lower() == text.lower()[::-1]}")
