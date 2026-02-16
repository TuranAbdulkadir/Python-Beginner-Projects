# Vigenere Cipher
def vigenere(text, key, encrypt=True):
    result = ""
    key_idx = 0
    for c in text:
        if c.isalpha():
            shift = ord(key[key_idx % len(key)].upper()) - ord('A')
            if not encrypt: shift = -shift
            base = ord('A') if c.isupper() else ord('a')
            result += chr((ord(c) - base + shift) % 26 + base)
            key_idx += 1
        else:
            result += c
    return result

mode = input("(e)ncrypt or (d)ecrypt? ").lower()
text = input("Text: ")
key = input("Key: ")
result = vigenere(text, key, mode == "e")
print(f"\nResult: {result}")
