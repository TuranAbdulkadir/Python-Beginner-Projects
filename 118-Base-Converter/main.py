# Base Converter
num = int(input("Enter decimal number: "))
print(f"\nDecimal:     {num}")
print(f"Binary:      {bin(num)}")
print(f"Octal:       {oct(num)}")
print(f"Hexadecimal: {hex(num).upper()}")
print(f"ASCII char:  {chr(num) if 32 <= num <= 126 else 'N/A'}")
