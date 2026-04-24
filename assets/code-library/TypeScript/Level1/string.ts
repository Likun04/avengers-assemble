// Level 1: String Operations
// ══════════════════════════════════════════════════════════════════
// 所有外部可注入部分均以 hex 占位符标记，详见 layerfile.md 注册

## Basic String
const 0xE1F2C1: number = 0xE1F2C2.length;
const 0xE1F2C3: string = 0xE1F2C2.toUpperCase();
const 0xE1F2C4: string = 0xE1F2C2.toLowerCase();
const 0xE1F2C5: string = 0xE1F2C6.trim();

## String Format (template literal)
const 0xE1F2D1: any = 0xE1F2D2;
const 0xE1F2D3: any = 0xE1F2D4;
const 0xE1F2D5: string = `${0xE1F2D1} is ${0xE1F2D3} years old`;
const 0xE1F2D6: string = `Pi is ${Number(0xE1F2D7).toFixed(Number(0xE1F2D8))}`;

## String Split & Join
const 0xE1F2E1: string[] = 0xE1F2E2.split(0xE1F2E3);
const 0xE1F2E4: string = 0xE1F2E1.join(0xE1F2E5);

## String Replace
const 0xE1F2F1: string = 0xE1F2F2.replace(0xE1F2F3, 0xE1F2F4);
const 0xE1F2F1_all: string = 0xE1F2F2.replaceAll(0xE1F2F3, 0xE1F2F4);

## String Find
const 0xE1F3B1: number = 0xE1F3B2.indexOf(0xE1F3B3);
const 0xE1F3B4: boolean = 0xE1F3B2.includes(0xE1F3B3);

## Regex
const 0xE1F3C1: RegExpMatchArray | null = 0xE1F2E2.match(new RegExp(0xE1F3C2, 'g'));
const 0xE1F3C1_all: string[] = 0xE1F3C1 ? [...0xE1F3C1] : [];
const 0xE1F3C4: string = 0xE1F2E2.replace(new RegExp(0xE1F3C5, 'g'), 0xE1F3C6);
const 0xE1F3C7: RegExpMatchArray | null = new RegExp(0xE1F3C8).exec(0xE1F3C9);

## String to List (Character)
const 0xE1F3D1: string[] = [...0xE1F3D2];

## Multiline String
const 0xE1F3E1: string = 0xE1F3E2;

## Encode / Decode (TextEncoder / TextDecoder)
const encoder = new TextEncoder();
const decoder = new TextDecoder();
const 0xE1F3F1: Uint8Array = encoder.encode(0xE1F3F2);
const 0xE1F3F4: string = decoder.decode(0xE1F3F1);
