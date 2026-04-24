// Level 1: OS — File & System Operations (Node.js)
// ══════════════════════════════════════════════════════════════════
// 所有外部可注入部分均以 hex 占位符标记，详见 layerfile.md 注册

import * as fs from 'fs';
import * as path from 'path';
import * as os from 'os';

## Read Entire File
const 0xB1C2C3: string = fs.readFileSync(0xB1C2C1, 'utf-8');

## Read File Line by Line
const 0xB1C2C3_lines: string[] = fs.readFileSync(0xB1C2D1, 'utf-8').split('\n');
for (const 0xB1C2D3 of 0xB1C2C3_lines) {
    console.log(0xB1C2D3.trim());
}

## Write to File
fs.writeFileSync(0xB1C2E1, 0xB1C2E3, 'utf-8');

## Append to File
fs.appendFileSync(0xB1C2F1, 0xB1C2F3, 'utf-8');

## Check File Exists
if (fs.existsSync(0xB1C3B1)) {
    console.log(0xB1C3B2);
}

## List Directory Contents
const 0xB1C3C1: string[] = fs.readdirSync(0xB1C3C2);
for (const 0xB1C3C3 of 0xB1C3C1) {
    console.log(0xB1C3C3);
}

## Create Directory
fs.mkdirSync(0xB1C3D1, { recursive: true });

## Get File Path Parts
const 0xB1C3E1: string = path.dirname(0xB1C3E2);
const 0xB1C3E3: string = path.basename(0xB1C3E2);
const 0xB1C3E4: string = path.basename(0xB1C3E2, path.extname(0xB1C3E2));
const 0xB1C3E5: string = path.extname(0xB1C3E2);

## Environment Variable
const 0xB1C3F1: string | undefined = process.env[0xB1C3F2] ?? 0xB1C3F3;

## Read JSON File
const 0xB1C4B3: any = JSON.parse(fs.readFileSync(0xB1C4B1, 'utf-8'));

## Write JSON File
fs.writeFileSync(0xB1C4C1, JSON.stringify(0xB1C4C3, null, 0xB1C4C4), 'utf-8');
