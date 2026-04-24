// Level 1: Function Definition
// ══════════════════════════════════════════════════════════════════
// 所有外部可注入部分均以 hex 占位符标记，详见 layerfile.md 注册

## Basic Function
function 0xF4A5C1(0xF4A5C2: any): any {
    return 0xF4A5C3;
}

## Function with Default Parameters
function 0xF4A5D1(0xF4A5D2: number, 0xF4A5D3: number = 0xF4A5D4): number {
    return 0xF4A5D2 ** 0xF4A5D3;
}

## Function with Multiple Returns
function 0xF4A5E1(0xF4A5E2: number[]): [number, number] {
    return [Math.min(...0xF4A5E2), Math.max(...0xF4A5E2)];
}

## Lambda (arrow function)
const 0xF4A5F1 = (0xF4A5F2: number): number => 0xF4A5F2 * 0xF4A5F2;
const 0xF4B6C1 = (0xF4B6C2: number, 0xF4B6C3: number): number => 0xF4B6C2 + 0xF4B6C3;

## Function with Rest Parameters (...args)
function 0xF4B6D1(...0xF4B6D2: number[]): number {
    return 0xF4B6D2.reduce((a, b) => a + b, 0);
}

## Function with Object Parameters (**kwargs equivalent)
function 0xF4B6E1(0xF4B6E2: Record<string, any>): void {
    for (const [0xF4B6E3, 0xF4B6E4] of Object.entries(0xF4B6E2)) {
        console.log(`${0xF4B6E3}: ${0xF4B6E4}`);
    }
}

## Decorator (higher-order function / wrapper)
function 0xF4B6F1(0xF4B6F2: (...args: any[]) => any) {
    return function 0xF4B7C1(...0xF4B7C2: any[]): any {
        const 0xF4B7C4: number = Date.now();
        const 0xF4B7C5: any = 0xF4B6F2(...0xF4B7C2);
        const 0xF4B7C6: number = Date.now();
        console.log(`${0xF4B6F2.name} took ${0xF4B7C6 - 0xF4B7C4}ms`);
        return 0xF4B7C5;
    };
}
