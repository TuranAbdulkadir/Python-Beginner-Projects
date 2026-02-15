# Encryption Tool (Caesar Cipher)
def encrypt(text, shift):
    result = ""
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result += chr((ord(c) - base + shift) % 26 + base)
        else:
            result += c
    return result

mode = input("(e)ncrypt or (d)ecrypt? ").lower()
text = input("Enter text: ")
shift = int(input("Shift (1-25): "))
if mode == "d": shift = -shift
result = encrypt(text, shift)
print(f"\nResult: {result}")
