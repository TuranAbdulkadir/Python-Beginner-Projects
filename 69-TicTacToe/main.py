# Tic Tac Toe vs Computer
import random
board = [" "] * 9

def show():
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6: print("-----------")

def check_win(mark):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==mark for a,b,c in wins)

def computer_move():
    empty = [i for i in range(9) if board[i]==" "]
    return random.choice(empty) if empty else -1

print("Tic Tac Toe - You are X")
show()
while " " in board:
    pos = int(input("Your move (1-9): ")) - 1
    if board[pos] != " ": print("Taken!"); continue
    board[pos] = "X"
    if check_win("X"): show(); print("You win!"); break
    cm = computer_move()
    if cm == -1: show(); print("Draw!"); break
    board[cm] = "O"
    if check_win("O"): show(); print("Computer wins!"); break
    show()
