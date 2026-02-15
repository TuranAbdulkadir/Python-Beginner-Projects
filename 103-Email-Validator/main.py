# Email Validator
import re
email = input("Enter email: ")
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
if re.match(pattern, email):
    user, domain = email.split("@")
    print(f"\nValid email ✅")
    print(f"User: {user}")
    print(f"Domain: {domain}")
else:
    print("Invalid email ❌")
