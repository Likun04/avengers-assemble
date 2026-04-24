// Level 1: Calculator — Basic Arithmetic & Variable Operations
// ══════════════════════════════════════════════════════════════════
// 所有外部可注入部分均以 hex 占位符标记，详见 layerfile.md 注册

## Assignment and Arithmetic
const 0xA1B2C1: number = 0xA1B2C2 + 0xA1B2C3;
const 0xA1B2D1: number = 0xA1B2D2 - 0xA1B2D3;
const 0xA1B2E1: number = 0xA1B2E2 * 0xA1B2E3;
const 0xA1B2F1: number = 0xA1B2F2 / 0xA1B2F3;

## Increment / Decrement
let 0xA1C3B1: number = 0xA1C3B2;
0xA1C3B1 = 0xA1C3B1 + 0xA1C3B3;
0xA1C3B1 += 0xA1C3B3;
0xA1C3B1 -= 0xA1C3B3;

## Type Conversion
let 0xA1D4B1: any = 0xA1D4B2;
const 0xA1D4C1: number = parseInt(String(0xA1D4B1));
const 0xA1D4D1: number = parseFloat(String(0xA1D4B1));
const 0xA1D4E1: string = String(0xA1D4B1);
const 0xA1D4F1: number = parseFloat(0xA1D4F2.toFixed(0xA1D4F3));

## Math Operations
const 0xA1E5B1: number = Math.sqrt(0xA1E5B2);
const 0xA1E5C1: number = Math.abs(0xA1E5C2);
const 0xA1E5D1: number = Math.max(0xA1E5D2, 0xA1E5D3, 0xA1E5D4);
const 0xA1E5E1: number = Math.min(0xA1E5E2, 0xA1E5E3, 0xA1E5E4);
const 0xA1E5F1: number = Math.pow(0xA1E5F2, 0xA1E5F3);

## Modulo & Floor Division
const 0xA1F6B1: number = 0xA1F6B2 % 0xA1F6B3;
const 0xA1F6C1: number = Math.floor(0xA1F6C2 / 0xA1F6C3);
