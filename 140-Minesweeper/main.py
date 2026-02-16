# Minesweeper Board Generator
import random
size = int(input("Board size (5-10): "))
mines = int(input("Number of mines: "))
board = [[0]*size for _ in range(size)]
mine_positions = random.sample(range(size*size), mines)
for pos in mine_positions:
    board[pos//size][pos%size] = -1
for r in range(size):
    for c in range(size):
        if board[r][c] == -1: continue
        count = 0
        for dr in [-1,0,1]:
            for dc in [-1,0,1]:
                nr, nc = r+dr, c+dc
                if 0<=nr<size and 0<=nc<size and board[nr][nc]==-1:
                    count += 1
        board[r][c] = count
print("\nMinesweeper Board (X=mine):")
for row in board:
    print(" ".join("X" if x==-1 else str(x) for x in row))
