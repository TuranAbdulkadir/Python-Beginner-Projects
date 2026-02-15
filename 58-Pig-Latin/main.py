# Pig Latin Translator
def to_pig_latin(word):
    vowels = "aeiouAEIOU"
    if word[0] in vowels:
        return word + "yay"
    for i, c in enumerate(word):
        if c in vowels:
            return word[i:] + word[:i] + "ay"
    return word + "ay"

text = input("Enter text: ")
result = " ".join(to_pig_latin(w) for w in text.split())
print(f"\nOriginal:  {text}")
print(f"Pig Latin: {result}")
