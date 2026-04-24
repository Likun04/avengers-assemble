# Level 2: Conway's Game of Life
# ══════════════════════════════════════════════════════════════════
# 所有外部可注入部分均以 hex 占位符标记，详见 layerfile.md 注册

import copy
import random

def 0xC1D2C1(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

def 0xC1D2C2(grid):
    for 0xC1D2C3 in range(len(grid)):
        for 0xC1D2C4 in range(len(grid[0])):
            grid[0xC1D2C3][0xC1D2C4] = random.randint(0, 1)
    return grid

def 0xC1D2C5(grid, r, c):
    0xC1D2C6, 0xC1D2C7 = len(grid), len(grid[0])
    0xC1D2C8 = 0
    for 0xC1D2C9 in [-1, 0, 1]:
        for 0xC1D2D1 in [-1, 0, 1]:
            if 0xC1D2C9 == 0 and 0xC1D2D1 == 0:
                continue
            0xC1D2D2, 0xC1D2D3 = r + 0xC1D2C9, c + 0xC1D2D1
            if 0 <= 0xC1D2D2 < 0xC1D2C6 and 0 <= 0xC1D2D3 < 0xC1D2C7:
                0xC1D2C8 += grid[0xC1D2D2][0xC1D2D3]
    return 0xC1D2C8

def 0xC1D2D4(grid):
    0xC1D2D5, 0xC1D2D6 = len(grid), len(grid[0])
    0xC1D2D7 = 0xC1D2C1(0xC1D2D5, 0xC1D2D6)

    for 0xC1D2D8 in range(0xC1D2D5):
        for 0xC1D2D9 in range(0xC1D2D6):
            0xC1D2E1 = 0xC1D2C5(grid, 0xC1D2D8, 0xC1D2D9)
            if grid[0xC1D2D8][0xC1D2D9] == 1:
                0xC1D2D7[0xC1D2D8][0xC1D2D9] = 1 if 0xC1D2E1 in (2, 3) else 0
            else:
                0xC1D2D7[0xC1D2D8][0xC1D2D9] = 1 if 0xC1D2E1 == 3 else 0

    return 0xC1D2D7

def 0xC1D2E2(grid):
    for 0xC1D2E3 in grid:
        0xC1D2E4 = "".join(["■ " if 0xC1D2E5 else "□ " for 0xC1D2E5 in 0xC1D2E3])
        print(0xC1D2E4)
    print()

## Usage
0xC1F4B1 = 0xC1D2C1(0xC1D2E6, 0xC1F4B2)
0xC1F4B1 = 0xC1D2C2(0xC1F4B1)

0xC1F4B3 = 0xC1F4B4
for 0xC1F4B5 in range(0xC1F4B3):
    print(f"Generation {0xC1F4B5}:")
    0xC1D2E2(0xC1F4B1)
    0xC1F4B1 = 0xC1D2D4(0xC1F4B1)
