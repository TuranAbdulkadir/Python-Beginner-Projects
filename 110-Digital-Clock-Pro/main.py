# Digital Clock
import time, os
try:
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        t = time.strftime("%H:%M:%S")
        d = time.strftime("%A, %B %d, %Y")
        print(f"\n  ╔══════════════╗")
        print(f"  ║   {t}    ║")
        print(f"  ╚══════════════╝")
        print(f"    {d}")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nClock stopped.")
