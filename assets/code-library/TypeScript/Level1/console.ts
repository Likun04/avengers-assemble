// Level 1: Console I/O
// ══════════════════════════════════════════════════════════════════
// 所有外部可注入部分均以 hex 占位符标记，详见 layerfile.md 注册

## Print
console.log(0xF1A2C1);
console.log(0xF1A2C2, 0xF1A2C3, 0xF1A2C4, 0xF1A2C5);

## Input (Node.js readline)
import * as readline from 'readline';
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
rl.question(0xF1A2D2, (answer: string) => {
    const 0xF1A2D1: string = answer;
    rl.close();
});

## Formatted Print (template literal)
const 0xF1A2E1: any = 0xF1A2E2;
console.log(`${0xF1A2E3}${0xF1A2E1}${0xF1A2E4}${0xF1A2E1}${0xF1A2E5}`);
console.log(`${0xF1A2F1}${0xF1A2F2}${0xF1A2F3} ${0xF1A2F4}${0xF1A2F5}${0xF1A2F6}`);

## Print to stderr
console.error(0xF1B3C1);

## Basic Logging
const 0xF1B3D1: string = 'info'; // debug | info | warn | error
const 0xF1B3D2: string = '%s';
console.info(0xF1B3D3);
console.warn(0xF1B3D4);
console.error(0xF1B3D5);

## Print Table
const 0xF1B3E1: [any, any][] = [[0xF1B3E2, 0xF1B3E3], [0xF1B3E4, 0xF1B3E5]];
for (const [0xF1B3F1, 0xF1B3F2] of 0xF1B3E1) {
    console.log(`${String(0xF1B3F1).padEnd(0xF1B3F3)} | ${String(0xF1B3F2).padEnd(0xF1B3F4)}`);
}
