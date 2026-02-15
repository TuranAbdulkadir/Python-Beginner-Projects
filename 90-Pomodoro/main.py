# Pomodoro Timer
import time
work_min = int(input("Work minutes (default 25): ") or "25")
break_min = int(input("Break minutes (default 5): ") or "5")
sessions = int(input("Sessions (default 4): ") or "4")
for s in range(1, sessions+1):
    print(f"\n🍅 Session {s}/{sessions} - WORK ({work_min} min)")
    for remaining in range(work_min * 60, 0, -1):
        m, sec = divmod(remaining, 60)
        print(f"\r  {m:02d}:{sec:02d}", end="", flush=True)
        time.sleep(1)
    print(f"\n☕ Break time! ({break_min} min)")
    for remaining in range(break_min * 60, 0, -1):
        m, sec = divmod(remaining, 60)
        print(f"\r  {m:02d}:{sec:02d}", end="", flush=True)
        time.sleep(1)
print("\n\n✅ All sessions complete!")
