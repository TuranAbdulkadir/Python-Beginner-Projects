# Text Adventure Game
import time
def slow_print(text, delay=0.03):
    for c in text: print(c, end="", flush=True); time.sleep(delay)
    print()

slow_print("You wake up in a dark room...")
slow_print("There's a DOOR to the left and a WINDOW to the right.\n")
choice = input("Go to (door/window): ").lower()
if choice == "door":
    slow_print("\nYou open the door and find a long hallway.")
    slow_print("At the end: a CHEST and a STAIRCASE.\n")
    c2 = input("Choose (chest/staircase): ").lower()
    if c2 == "chest":
        slow_print("\nYou found 100 gold coins! YOU WIN! 🏆")
    else:
        slow_print("\nThe stairs lead to freedom! YOU ESCAPED! 🌅")
elif choice == "window":
    slow_print("\nYou see a garden outside.")
    slow_print("There's a KEY on the ground and a MAP on the wall.\n")
    c2 = input("Take (key/map): ").lower()
    if c2 == "key":
        slow_print("\nThe key opens a secret vault! YOU WIN! 💎")
    else:
        slow_print("\nThe map leads to treasure! YOU WIN! 🗺️")
else:
    slow_print("\nYou stand still... nothing happens. Game over.")
