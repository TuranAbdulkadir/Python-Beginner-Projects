# ISBN Validator
isbn = input("Enter ISBN-10: ").replace("-", "")
if len(isbn) != 10:
    print("Invalid length!")
else:
    total = sum((10-i) * (10 if c == 'X' else int(c)) for i, c in enumerate(isbn))
    if total % 11 == 0:
        print(f"ISBN {isbn} is VALID ✅")
    else:
        print(f"ISBN {isbn} is INVALID ❌")
