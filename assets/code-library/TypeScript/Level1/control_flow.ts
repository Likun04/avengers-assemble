// Level 1: Control Flow
// ══════════════════════════════════════════════════════════════════
// 所有外部可注入部分均以 hex 占位符标记，详见 layerfile.md 注册

## If-Else
if (0xC1D2C1 >= 0xC1D2C2) {
    const 0xC1D2C3 = 0xC1D2C4;
} else if (0xC1D2C1 >= 0xC1D2C5) {
    const 0xC1D2C3 = 0xC1D2C6;
} else if (0xC1D2C1 >= 0xC1D2C7) {
    const 0xC1D2C3 = 0xC1D2C8;
} else {
    const 0xC1D2C3 = 0xC1D2C9;
}

## For Loop (Range)
for (let 0xC1D2D1: number = 0; 0xC1D2D1 < 0xC1D2D2; 0xC1D2D1++) {
    console.log(0xC1D2D1);
}

## For Loop (Iterable — Array)
const 0xC1D2E1: any[] = [0xC1D2E2, 0xC1D2E3, 0xC1D2E4];
for (const 0xC1D2E5 of 0xC1D2E1) {
    console.log(0xC1D2E5);
}

## For Loop (Enumerate — entries)
const 0xC1D2F1: any[] = [0xC1D2F2, 0xC1D2F3, 0xC1D2F4];
for (const [0xC1D3B1, 0xC1D3B2] of 0xC1D2F1.entries()) {
    console.log(`${0xC1D3B1}: ${0xC1D3B2}`);
}

## While Loop
let 0xC1D3C1: number = 0xC1D3C2;
while (0xC1D3C1 < 0xC1D3C3) {
    console.log(0xC1D3C1);
    0xC1D3C1 += 0xC1D3C4;
}

## Break
for (let 0xC1D3D1: number = 0; 0xC1D3D1 < 0xC1D3D2; 0xC1D3D1++) {
    if (0xC1D3D1 === 0xC1D3D3) {
        break;
    }
    console.log(0xC1D3D1);
}

## Continue
for (let 0xC1D3E1: number = 0; 0xC1D3E1 < 0xC1D3E2; 0xC1D3E1++) {
    if (0xC1D3E1 % 0xC1D3E3 === 0) {
        continue;
    }
    console.log(0xC1D3E1);
}

## Nested Loops
for (let 0xC1D3F1: number = 0; 0xC1D3F1 < 0xC1D3F2; 0xC1D3F1++) {
    for (let 0xC1D4B1: number = 0; 0xC1D4B1 < 0xC1D4B2; 0xC1D4B1++) {
        console.log(`(${0xC1D3F1}, ${0xC1D4B1})`);
    }
}

## Try-Catch-Finally
try {
    const 0xC1D4C1: number = 0xC1D4C2 / 0xC1D4C3;
} catch (0xC1D4C6) {
    if (0xC1D4C6 instanceof 0xC1D4C4) {
        console.log(0xC1D4C5);
    }
    console.log(`${0xC1D4C7}${0xC1D4C6}`);
} finally {
    console.log(0xC1D4C8);
}
