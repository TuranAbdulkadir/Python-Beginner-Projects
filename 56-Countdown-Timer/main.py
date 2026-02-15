# Countdown Timer
import time

minutes = int(input("Enter minutes: "))
seconds = minutes * 60

print(f"\nCountdown started: {minutes} minutes")
while seconds > 0:
    mins, secs = divmod(seconds, 60)
    print(f"\r  {mins:02d}:{secs:02d}", end="", flush=True)
    time.sleep(1)
    seconds -= 1

print("\n\n⏰ TIME'S UP!")
