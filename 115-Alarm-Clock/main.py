# Alarm Clock
import time
alarm = input("Set alarm (HH:MM): ")
print(f"Alarm set for {alarm}. Waiting...")
try:
    while True:
        now = time.strftime("%H:%M")
        if now == alarm:
            print(f"\n🔔 ALARM! It's {alarm}!")
            for _ in range(5):
                print("RING! 🔔", end=" ", flush=True)
                time.sleep(0.5)
            break
        time.sleep(10)
except KeyboardInterrupt:
    print("\nAlarm cancelled.")
