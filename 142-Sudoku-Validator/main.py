# Sudoku Validator
def is_valid_sudoku(board):
    for row in board:
        nums = [n for n in row if n != 0]
        if len(nums) != len(set(nums)): return False
    for col in range(9):
        nums = [board[row][col] for row in range(9) if board[row][col] != 0]
        if len(nums) != len(set(nums)): return False
    for box_r in range(3):
        for box_c in range(3):
            nums = []
            for r in range(3):
                for c in range(3):
                    val = board[box_r*3+r][box_c*3+c]
                    if val != 0: nums.append(val)
            if len(nums) != len(set(nums)): return False
    return True

board = [
    [5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]
]
print("Sudoku Board:")
for row in board:
    print(" ".join(str(x) if x else "." for x in row))
print(f"\nValid: {'Yes' if is_valid_sudoku(board) else 'No'}")
