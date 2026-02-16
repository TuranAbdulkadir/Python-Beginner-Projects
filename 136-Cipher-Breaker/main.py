# Cipher Breaker - Brute Force Caesar
text = input("Enter encrypted text: ")
print("\nAll possible decryptions:")
for shift in range(26):
    decoded = ""
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            decoded += chr((ord(c) - base - shift) % 26 + base)
        else:
            decoded += c
    print(f"  Shift {shift:2d}: {decoded}")
