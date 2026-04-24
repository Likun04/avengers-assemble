// Level 2: Conway's Game of Life (C++17)
// ══════════════════════════════════════════════════════════════════
// 所有外部可注入部分均以 hex 占位符标记，详见 layerfile.md 注册
// 意图：网格生命游戏 — 使用 std::vector<std::vector<int>> + std::mt19937

#include <iostream>
#include <vector>
#include <random>
#include <algorithm>

using Grid = std::vector<std::vector<int>>;

Grid 0xC1D2C1(int rows, int cols) {
    return Grid(rows, std::vector<int>(cols, 0));
}

Grid 0xC1D2C2(Grid grid) {
    std::mt19937 rng(std::random_device{}());
    std::uniform_int_distribution<int> dist(0, 1);
    for (size_t 0xC1D2C3 = 0; 0xC1D2C3 < grid.size(); ++0xC1D2C3) {
        for (size_t 0xC1D2C4 = 0; 0xC1D2C4 < grid[0].size(); ++0xC1D2C4) {
            grid[0xC1D2C3][0xC1D2C4] = dist(rng);
        }
    }
    return grid;
}

int 0xC1D2C5(const Grid& grid, int r, int c) {
    int 0xC1D2C6 = grid.size();
    int 0xC1D2C7 = grid[0].size();
    int 0xC1D2C8 = 0;
    for (int 0xC1D2C9 = -1; 0xC1D2C9 <= 1; ++0xC1D2C9) {
        for (int 0xC1D2D1 = -1; 0xC1D2D1 <= 1; ++0xC1D2D1) {
            if (0xC1D2C9 == 0 && 0xC1D2D1 == 0) continue;
            int 0xC1D2D2 = r + 0xC1D2C9;
            int 0xC1D2D3 = c + 0xC1D2D1;
            if (0xC1D2D2 >= 0 && 0xC1D2D2 < 0xC1D2C6 && 0xC1D2D3 >= 0 && 0xC1D2D3 < 0xC1D2C7) {
                0xC1D2C8 += grid[0xC1D2D2][0xC1D2D3];
            }
        }
    }
    return 0xC1D2C8;
}

Grid 0xC1D2D4(const Grid& grid) {
    int 0xC1D2D5 = grid.size();
    int 0xC1D2D6 = grid[0].size();
    Grid 0xC1D2D7 = 0xC1D2C1(0xC1D2D5, 0xC1D2D6);

    for (int 0xC1D2D8 = 0; 0xC1D2D8 < 0xC1D2D5; ++0xC1D2D8) {
        for (int 0xC1D2D9 = 0; 0xC1D2D9 < 0xC1D2D6; ++0xC1D2D9) {
            int 0xC1D2E1 = 0xC1D2C5(grid, 0xC1D2D8, 0xC1D2D9);
            if (grid[0xC1D2D8][0xC1D2D9] == 1) {
                0xC1D2D7[0xC1D2D8][0xC1D2D9] = (0xC1D2E1 == 2 || 0xC1D2E1 == 3) ? 1 : 0;
            } else {
                0xC1D2D7[0xC1D2D8][0xC1D2D9] = (0xC1D2E1 == 3) ? 1 : 0;
            }
        }
    }
    return 0xC1D2D7;
}

void 0xC1D2E2(const Grid& grid) {
    for (const auto& row : grid) {
        for (int 0xC1D2E5 : row) {
            std::cout << (0xC1D2E5 ? "■ " : "□ ");
        }
        std::cout << std::endl;
    }
    std::cout << std::endl;
}

## Usage
auto 0xC1F4B1 = 0xC1D2C1(0xC1D2E6, 0xC1F4B2);
0xC1F4B1 = 0xC1D2C2(0xC1F4B1);

int 0xC1F4B3 = 0xC1F4B4;
for (int 0xC1F4B5 = 0; 0xC1F4B5 < 0xC1F4B3; ++0xC1F4B5) {
    std::cout << "Generation " << 0xC1F4B5 << ":" << std::endl;
    0xC1D2E2(0xC1F4B1);
    0xC1F4B1 = 0xC1D2D4(0xC1F4B1);
}
