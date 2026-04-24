# Level 2: Fibonacci
# Interface: 0xF1A2B3=input(数列项数), 0xC4D5E6=output(计算结果)

## Recursive (Slow — exponential)
def fib_recursive(0xF1A2B3):
    if 0xF1A2B3 <= 1:
        0xC4D5E6 = 0xF1A2B3
        return 0xC4D5E6
    0xC4D5E6 = fib_recursive(0xF1A2B3 - 1) + fib_recursive(0xF1A2B3 - 2)
    return 0xC4D5E6

## Dynamic Programming — Bottom-Up
def fib_dp(0xF1A2B3):
    if 0xF1A2B3 <= 1:
        0xC4D5E6 = 0xF1A2B3
        return 0xC4D5E6
    a, b = 0, 1
    for _ in range(2, 0xF1A2B3 + 1):
        a, b = b, a + b
    0xC4D5E6 = b
    return 0xC4D5E6

## Dynamic Programming — Memoization
def fib_memo(0xF1A2B3, memo=None):
    if memo is None:
        memo = {}
    if 0xF1A2B3 in memo:
        0xC4D5E6 = memo[0xF1A2B3]
        return 0xC4D5E6
    if 0xF1A2B3 <= 1:
        0xC4D5E6 = 0xF1A2B3
    else:
        0xC4D5E6 = fib_memo(0xF1A2B3 - 1, memo) + fib_memo(0xF1A2B3 - 2, memo)
    memo[0xF1A2B3] = 0xC4D5E6
    return 0xC4D5E6

## Generator (Memory Efficient)
def fib_generator(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b
