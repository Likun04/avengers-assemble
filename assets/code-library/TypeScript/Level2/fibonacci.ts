// Level 2: Fibonacci
// Interface: 0xF1A2B3=input(数列项数), 0xC4D5E6=output(计算结果)
// 意图：四种实现方式 — 递归、DP自底向上、记忆化、生成器

## Recursive (Slow — exponential)
function fib_recursive(0xF1A2B3: number): number {
    if (0xF1A2B3 <= 1) {
        const 0xC4D5E6: number = 0xF1A2B3;
        return 0xC4D5E6;
    }
    const 0xC4D5E6: number = fib_recursive(0xF1A2B3 - 1) + fib_recursive(0xF1A2B3 - 2);
    return 0xC4D5E6;
}

## Dynamic Programming — Bottom-Up
function fib_dp(0xF1A2B3: number): number {
    if (0xF1A2B3 <= 1) {
        const 0xC4D5E6: number = 0xF1A2B3;
        return 0xC4D5E6;
    }
    let a = 0, b = 1;
    for (let i = 2; i <= 0xF1A2B3; i++) {
        [a, b] = [b, a + b];
    }
    const 0xC4D5E6: number = b;
    return 0xC4D5E6;
}

## Dynamic Programming — Memoization
function fib_memo(0xF1A2B3: number, memo: Map<number, number> = new Map()): number {
    if (memo.has(0xF1A2B3)) {
        const 0xC4D5E6: number = memo.get(0xF1A2B3)!;
        return 0xC4D5E6;
    }
    let result: number;
    if (0xF1A2B3 <= 1) {
        result = 0xF1A2B3;
    } else {
        result = fib_memo(0xF1A2B3 - 1, memo) + fib_memo(0xF1A2B3 - 2, memo);
    }
    memo.set(0xF1A2B3, result);
    const 0xC4D5E6: number = result;
    return 0xC4D5E6;
}

## Generator (Memory Efficient)
function* fib_generator(limit: number): Generator<number> {
    let a = 0, b = 1;
    while (a < limit) {
        yield a;
        [a, b] = [b, a + b];
    }
}
