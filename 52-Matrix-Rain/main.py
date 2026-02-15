# Matrix Rain Effect
import random, time, os
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$%&"
width = 60
try:
    while True:
        line = ""
        for _ in range(width):
            line += random.choice(chars) if random.random() > 0.7 else " "
        print(f"\033[32m{line}\033[0m")
        time.sleep(0.05)
except KeyboardInterrupt:
    os.system("cls" if os.name == "nt" else "clear")
    print("Matrix disconnected.")
