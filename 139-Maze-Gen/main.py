# Maze Generator (Text-based)
import random

def generate_maze(width, height):
    maze = [['#' for _ in range(width)] for _ in range(height)]
    def carve(x, y):
        maze[y][x] = ' '
        directions = [(0,2),(0,-2),(2,0),(-2,0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 < nx < width and 0 < ny < height and maze[ny][nx] == '#':
                maze[y+dy//2][x+dx//2] = ' '
                carve(nx, ny)
    carve(1, 1)
    maze[0][1] = 'S'
    maze[height-1][width-2] = 'E'
    return maze

w, h = 21, 11
maze = generate_maze(w, h)
for row in maze:
    print(''.join(row))
print("\nS=Start, E=End")
