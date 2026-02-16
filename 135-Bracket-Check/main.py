# Bracket Checker
def check_brackets(text):
    stack = []
    pairs = {"(": ")", "[": "]", "{": "}"}
    for i, c in enumerate(text):
        if c in pairs:
            stack.append((c, i))
        elif c in pairs.values():
            if not stack:
                return f"Extra closing '{c}' at position {i}"
            open_b, pos = stack.pop()
            if pairs[open_b] != c:
                return f"Mismatch: '{open_b}' at {pos} closed by '{c}' at {i}"
    if stack:
        return f"Unclosed '{stack[-1][0]}' at position {stack[-1][1]}"
    return "All brackets matched!"

text = input("Enter code/text: ")
print(f"\nResult: {check_brackets(text)}")
