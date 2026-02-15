# Binary Converter
num = int(input("Enter a decimal number: "))
print(f"\nDecimal: {num}")
print(f"Binary:  {bin(num)[2:]}")
print(f"Octal:   {oct(num)[2:]}")
print(f"Hex:     {hex(num)[2:].upper()}")
