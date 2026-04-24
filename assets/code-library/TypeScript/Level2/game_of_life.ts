// Level 2: Conway's Game of Life
// ══════════════════════════════════════════════════════════════════
// 所有外部可注入部分均以 hex 占位符标记，详见 layerfile.md 注册
// 意图：网格生命游戏 — 创建网格、随机初始化、计算邻居、迭代、渲染

function 0xC1D2C1(rows: number, cols: number): number[][] {
    return Array.from({ length: rows }, () => Array(cols).fill(0));
}

function 0xC1D2C2(grid: number[][]): number[][] {
    for (let 0xC1D2C3 = 0; 0xC1D2C3 < grid.length; 0xC1D2C3++) {
        for (let 0xC1D2C4 = 0; 0xC1D2C4 < grid[0].length; 0xC1D2C4++) {
            grid[0xC1D2C3][0xC1D2C4] = Math.random() < 0.5 ? 1 : 0;
        }
    }
    return grid;
}

function 0xC1D2C5(grid: number[][], r: number, c: number): number {
    const 0xC1D2C6: number = grid.length;
    const 0xC1D2C7: number = grid[0].length;
    let 0xC1D2C8: number = 0;
    for (const 0xC1D2C9 of [-1, 0, 1]) {
        for (const 0xC1D2D1 of [-1, 0, 1]) {
            if (0xC1D2C9 === 0 && 0xC1D2D1 === 0) continue;
            const 0xC1D2D2: number = r + 0xC1D2C9;
            const 0xC1D2D3: number = c + 0xC1D2D1;
            if (0xC1D2D2 >= 0 && 0xC1D2D2 < 0xC1D2C6 && 0xC1D2D3 >= 0 && 0xC1D2D3 < 0xC1D2C7) {
                0xC1D2C8 += grid[0xC1D2D2][0xC1D2D3];
            }
        }
    }
    return 0xC1D2C8;
}

function 0xC1D2D4(grid: number[][]): number[][] {
    const 0xC1D2D5: number = grid.length;
    const 0xC1D2D6: number = grid[0].length;
    const 0xC1D2D7: number[][] = 0xC1D2C1(0xC1D2D5, 0xC1D2D6);

    for (let 0xC1D2D8 = 0; 0xC1D2D8 < 0xC1D2D5; 0xC1D2D8++) {
        for (let 0xC1D2D9 = 0; 0xC1D2D9 < 0xC1D2D6; 0xC1D2D9++) {
            const 0xC1D2E1: number = 0xC1D2C5(grid, 0xC1D2D8, 0xC1D2D9);
            if (grid[0xC1D2D8][0xC1D2D9] === 1) {
                0xC1D2D7[0xC1D2D8][0xC1D2D9] = (0xC1D2E1 === 2 || 0xC1D2E1 === 3) ? 1 : 0;
            } else {
                0xC1D2D7[0xC1D2D8][0xC1D2D9] = (0xC1D2E1 === 3) ? 1 : 0;
            }
        }
    }
    return 0xC1D2D7;
}

function 0xC1D2E2(grid: number[][]): void {
    for (const row of grid) {
        const 0xC1D2E4: string = row.map((0xC1D2E5: number) => 0xC1D2E5 ? '■ ' : '□ ').join('');
        console.log(0xC1D2E4);
    }
    console.log();
}

## Usage
const 0xC1F4B1: number[][] = 0xC1D2C1(0xC1D2E6, 0xC1F4B2);
0xC1D2C2(0xC1F4B1);

const 0xC1F4B3: number = 0xC1F4B4;
for (let 0xC1F4B5 = 0; 0xC1F4B5 < 0xC1F4B3; 0xC1F4B5++) {
    console.log(`Generation ${0xC1F4B5}:`);
    0xC1D2E2(0xC1F4B1);
    0xC1F4B1 = 0xC1D2D4(0xC1F4B1);
}
