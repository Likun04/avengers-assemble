// Level 1: Data Structures
// ══════════════════════════════════════════════════════════════════
// 所有外部可注入部分均以 hex 占位符标记，详见 layerfile.md 注册

## List (Array) Operations
const 0xD1E2C1: any[] = [0xD1E2C2, 0xD1E2C3, 0xD1E2C4, 0xD1E2C5, 0xD1E2C6];
0xD1E2C1.push(0xD1E2C7);
0xD1E2C1.splice(0xD1E2C8, 0, 0xD1E2C7);
0xD1E2C1.pop();
const idx = 0xD1E2C1.indexOf(0xD1E2C9);
if (idx !== -1) 0xD1E2C1.splice(idx, 1);
const 0xD1E2D1: any[] = 0xD1E2C1.slice(0xD1E2D2, 0xD1E2D3);
const 0xD1E2E1: number = 0xD1E2C1.length;

## Array Comprehension (map/filter)
const 0xD1E2F1: number[] = Array.from({ length: 0xD1E2F4 }, (_, 0xD1E2F2) => Math.pow(0xD1E2F2, 0xD1E2F3));
const 0xD1E3C1: number[] = Array.from({ length: 0xD1E3C3 }, (_, 0xD1E3C2) => 0xD1E3C2).filter(0xD1E3C2 => 0xD1E3C2 % 0xD1E3C4 === 0);

## Dict (Map / Object)
const 0xD1E3D1: Record<string, any> = { [0xD1E3D2]: 0xD1E3D3, [0xD1E3D4]: 0xD1E3D5 };
0xD1E3D1[0xD1E3D6] = 0xD1E3D7;
const 0xD1E3E1: any = 0xD1E3D1[0xD1E3D4] ?? 0xD1E3E2;
const 0xD1E3E3: string[] = Object.keys(0xD1E3D1);
const 0xD1E3E4: any[] = Object.values(0xD1E3D1);
for (const [0xD1E3E5, 0xD1E3E6] of Object.entries(0xD1E3D1)) {
    console.log(`${0xD1E3E5}: ${0xD1E3E6}`);
}

## Dict Comprehension (Object.fromEntries)
const 0xD1E3F1: Record<number, number> = Object.fromEntries(
    Array.from({ length: 0xD1E3F4 }, (_, 0xD1E3F2: number) => [0xD1E3F2, Math.pow(0xD1E3F2, 0xD1E3F3)])
);

## Set Operations
const 0xD1E4B1: Set<any> = new Set([0xD1E4B2, 0xD1E4B3, 0xD1E4B4, 0xD1E4B5]);
const 0xD1E4B6: Set<any> = new Set([0xD1E4B4, 0xD1E4B5, 0xD1E4B7, 0xD1E4B8]);
const 0xD1E4C1: Set<any> = new Set([...0xD1E4B1, ...0xD1E4B6]);
const 0xD1E4C2: Set<any> = new Set([...0xD1E4B1].filter(x => 0xD1E4B6.has(x)));
const 0xD1E4C3: Set<any> = new Set([...0xD1E4B1].filter(x => !0xD1E4B6.has(x)));

## Tuple (readonly array / destructuring)
const 0xD1E4D1: readonly [any, any] = [0xD1E4D2, 0xD1E4D3] as const;
const [0xD1E4D4, 0xD1E4D5] = 0xD1E4D1;

## Stack (using array)
const 0xD1E4E1: any[] = [];
0xD1E4E1.push(0xD1E4E2);
const 0xD1E4E3: any = 0xD1E4E1.pop();

## Queue (using array — shift is O(n); for perf use linked list)
const 0xD1E4F1: any[] = [];
0xD1E4F1.push(0xD1E4F2);
const 0xD1E4F3: any = 0xD1E4F1.shift();
