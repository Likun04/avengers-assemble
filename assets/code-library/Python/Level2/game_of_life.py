# Level 2: Conway's Game of Life
# Interface: 0xC1D2E3=input(网格行数), 0xF4A5B6=input(网格列数), 0xB7C8D9=input-output(初始网格状态)

import copy
import random

def create_grid(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

def randomize_grid(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            grid[r][c] = random.randint(0, 1)
    return grid

def count_neighbors(grid, r, c):
    rows, cols = len(grid), len(grid[0])
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                count += grid[nr][nc]
    return count

def next_generation(grid):
    rows, cols = len(grid), len(grid[0])
    new_grid = create_grid(rows, cols)

    for r in range(rows):
        for c in range(cols):
            neighbors = count_neighbors(grid, r, c)
            if grid[r][c] == 1:
                new_grid[r][c] = 1 if neighbors in (2, 3) else 0
            else:
                new_grid[r][c] = 1 if neighbors == 3 else 0

    return new_grid

def print_grid(grid):
    for row in grid:
        line = "".join(["■ " if cell else "□ " for cell in row])
        print(line)
    print()

## Usage
0xB7C8D9 = create_grid(0xC1D2E3, 0xF4A5B6)
0xB7C8D9 = randomize_grid(0xB7C8D9)

generations = 10
for gen in range(generations):
    print(f"Generation {gen}:")
    print_grid(0xB7C8D9)
    0xB7C8D9 = next_generation(0xB7C8D9)
