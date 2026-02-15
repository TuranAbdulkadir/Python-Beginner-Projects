# Anagram Checker
w1 = input("First word: ").lower().replace(" ", "")
w2 = input("Second word: ").lower().replace(" ", "")
if sorted(w1) == sorted(w2):
    print(f"\n'{w1}' and '{w2}' ARE anagrams!")
else:
    print(f"\n'{w1}' and '{w2}' are NOT anagrams")
