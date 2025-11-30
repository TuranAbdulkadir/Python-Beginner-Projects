text = input("Enter text: ").lower()
cleaned = "".join(c for c in text if c.isalnum())
if cleaned == cleaned[::-1]:
    print("✅ It is a Palindrome!")
else:
    print("❌ Not a Palindrome.")