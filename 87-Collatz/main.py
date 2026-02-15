# Collatz Conjecture
num = int(input("Enter a positive number: "))
steps = 0
sequence = [num]
while num != 1:
    num = num // 2 if num % 2 == 0 else num * 3 + 1
    sequence.append(num)
    steps += 1
print(f"Steps to reach 1: {steps}")
print(f"Max value: {max(sequence)}")
print(f"Sequence: {' -> '.join(str(x) for x in sequence[:20])}{'...' if len(sequence) > 20 else ''}")
