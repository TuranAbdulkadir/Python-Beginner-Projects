# Stopwatch
import time

print("=== Stopwatch ===")
input("Press Enter to START...")
start = time.time()
input("Press Enter to STOP...")
elapsed = time.time() - start
mins, secs = divmod(elapsed, 60)
print(f"\nElapsed: {int(mins):02d}:{secs:05.2f}")
