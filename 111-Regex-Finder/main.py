# Regex Finder
import re
text = input("Enter text: ")
print("\n1. Find emails  2. Find URLs  3. Find phone numbers  4. Find words")
choice = int(input("Choose: "))
patterns = {
    1: (r'[\w.+-]+@[\w-]+\.[\w.]+', "Emails"),
    2: (r'https?://[^\s]+', "URLs"),
    3: (r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', "Phone numbers"),
    4: (r'\b[A-Z][a-z]+\b', "Capitalized words")
}
pattern, label = patterns.get(choice, (r'\w+', "Words"))
matches = re.findall(pattern, text)
print(f"\n{label} found: {len(matches)}")
for m in matches:
    print(f"  - {m}")
