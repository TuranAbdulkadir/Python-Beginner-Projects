# Conway's Game of Life
import os, time, random
rows, cols = 15, 30
grid = [[random.choice([0,1]) for _ in range(cols)] for _ in range(rows)]

def count_neighbors(g, r, c):
    count = 0
    for dr in [-1,0,1]:
        for dc in [-1,0,1]:
            if dr == 0 and dc == 0: continue
            nr, nc = (r+dr) % rows, (c+dc) % cols
            count += g[nr][nc]
    return count

def next_gen(g):
    new = [[0]*cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            n = count_neighbors(g, r, c)
            if g[r][c] == 1:
                new[r][c] = 1 if n in [2,3] else 0
            else:
                new[r][c] = 1 if n == 3 else 0
    return new

try:
    gen = 0
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"Game of Life - Gen {gen}")
        for row in grid:
            print("".join("█" if c else " " for c in row))
        grid = next_gen(grid)
        gen += 1
        time.sleep(0.2)
except KeyboardInterrupt:
    print(f"\nStopped at generation {gen}")
