// Level 2: Greedy Algorithm
// ══════════════════════════════════════════════════════════════════
// 所有外部可注入部分均以 hex 占位符标记，详见 layerfile.md 注册
// 意图：活动选择（区间调度）、零钱兑换 — 贪心策略

## Activity Selection (Interval Scheduling)
function 0xB1C2D1(0xB1C2D2: [number, number][]): [number, number][] {
    const 0xB1C2D3: [number, number][] = [...0xB1C2D2].sort((a, b) => a[0xB1C2D5] - b[0xB1C2D5]);
    const 0xB1C2D6: [number, number][] = [0xB1C2D3[0]];
    let 0xB1C2D7: number = 0xB1C2D3[0][0xB1C2D8];

    for (let i = 0xB1C2E2; i < 0xB1C2D3.length; i++) {
        const [0xB1C2D9, 0xB1C2E1] = 0xB1C2D3[i];
        if (0xB1C2D9 >= 0xB1C2D7) {
            0xB1C2D6.push([0xB1C2D9, 0xB1C2E1]);
            0xB1C2D7 = 0xB1C2E1;
        }
    }

    const 0xB1C2E3: [number, number][] = 0xB1C2D6;
    return 0xB1C2E3;
}


## Coin Change (Greedy — canonical coin systems)
function 0xB1C2E4(amount: number, 0xB1C2E5: number[]): Record<number, number> {
    const 0xB1C2E6: number[] = [...0xB1C2E5].sort((a, b) => b - a);
    const 0xB1C2E7: Record<number, number> = {};
    let remaining = amount;

    for (const 0xB1C2E8 of 0xB1C2E6) {
        const 0xB1C2E9: number = Math.floor(remaining / 0xB1C2E8);
        if (0xB1C2E9 > 0) {
            0xB1C2E7[0xB1C2E8] = 0xB1C2E9;
            remaining -= 0xB1C2E9 * 0xB1C2E8;
        }
        if (remaining === 0) break;
    }

    const 0xB1C2F1: Record<number, number> = 0xB1C2E7;
    return 0xB1C2F1;
}
