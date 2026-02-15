# Palindrome Generator
text = input("Enter text: ")
clean = "".join(c.lower() for c in text if c.isalnum())
is_palindrome = clean == clean[::-1]
print(f"\nOriginal: {text}")
print(f"Cleaned: {clean}")
print(f"Palindrome: {'Yes ✅' if is_palindrome else 'No ❌'}")
if not is_palindrome:
    palindrome = clean + clean[-2::-1]
    print(f"Made into palindrome: {palindrome}")
