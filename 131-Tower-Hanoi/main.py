# Tower of Hanoi
def hanoi(n, source, target, aux):
    if n == 1:
        print(f"  Move disk 1 from {source} to {target}")
        return 1
    moves = hanoi(n-1, source, aux, target)
    print(f"  Move disk {n} from {source} to {target}")
    moves += 1 + hanoi(n-1, aux, target, source)
    return moves

n = int(input("Number of disks: "))
print(f"\nSolving Tower of Hanoi with {n} disks:\n")
total = hanoi(n, "A", "C", "B")
print(f"\nTotal moves: {total}")
