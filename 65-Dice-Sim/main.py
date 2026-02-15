# Dice Simulator
import random
print("=== Dice Simulator ===")
while True:
    dice_count = int(input("How many dice? (0 to quit): "))
    if dice_count == 0: break
    rolls = [random.randint(1, 6) for _ in range(dice_count)]
    faces = {1:"⚀",2:"⚁",3:"⚂",4:"⚃",5:"⚄",6:"⚅"}
    print(" ".join(faces[r] for r in rolls))
    print(f"Values: {rolls} | Total: {sum(rolls)}")
