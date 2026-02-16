# Subtitle Text Cleaner
text = input("Enter subtitle text with timestamps: ")
import re
cleaned = re.sub(r'\d{2}:\d{2}:\d{2}[.,]\d{3}\s*-->\s*\d{2}:\d{2}:\d{2}[.,]\d{3}', '', text)
cleaned = re.sub(r'<[^>]+>', '', cleaned)
cleaned = re.sub(r'\d+\n', '', cleaned)
cleaned = re.sub(r'\n{2,}', '\n', cleaned).strip()
print(f"\nCleaned text:\n{cleaned}")
