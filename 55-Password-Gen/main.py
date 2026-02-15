# Password Generator
import random
import string

length = int(input("Password length: "))
use_upper = input("Include uppercase? (y/n): ").lower() == "y"
use_nums = input("Include numbers? (y/n): ").lower() == "y"
use_special = input("Include symbols? (y/n): ").lower() == "y"

chars = string.ascii_lowercase
if use_upper: chars += string.ascii_uppercase
if use_nums: chars += string.digits
if use_special: chars += "!@#$%^&*"

password = "".join(random.choice(chars) for _ in range(length))
strength = "Weak" if length < 8 else "Medium" if length < 12 else "Strong"
print(f"\nPassword: {password}")
print(f"Strength: {strength}")
print(f"Length: {length} characters")
