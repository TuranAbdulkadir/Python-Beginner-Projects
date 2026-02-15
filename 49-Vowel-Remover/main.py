# Vowel Remover
text = input("Enter text: ")
vowels = "aeiouAEIOU"
result = "".join(c for c in text if c not in vowels)
print(f"\nOriginal: {text}")
print(f"Without vowels: {result}")
print(f"Removed {len(text) - len(result)} vowels")
