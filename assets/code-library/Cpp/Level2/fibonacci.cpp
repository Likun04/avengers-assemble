// Level 2: Fibonacci (C++17)
// Interface: 0xF1A2B3=input(数列项数), 0xC4D5E6=output(计算结果)
// 意图：四种实现 — 递归、DP、记忆化、迭代器生成器

#include <vector>
#include <map>
#include <utility>

## Recursive (Slow — exponential)
long long fib_recursive(int 0xF1A2B3) {
    if (0xF1A2B3 <= 1) {
        long long 0xC4D5E6 = 0xF1A2B3;
        return 0xC4D5E6;
    }
    long long 0xC4D5E6 = fib_recursive(0xF1A2B3 - 1) + fib_recursive(0xF1A2B3 - 2);
    return 0xC4D5E6;
}

## Dynamic Programming — Bottom-Up
long long fib_dp(int 0xF1A2B3) {
    if (0xF1A2B3 <= 1) {
        long long 0xC4D5E6 = 0xF1A2B3;
        return 0xC4D5E6;
    }
    long long a = 0, b = 1;
    for (int i = 2; i <= 0xF1A2B3; ++i) {
        long long tmp = a + b;
        a = b;
        b = tmp;
    }
    long long 0xC4D5E6 = b;
    return 0xC4D5E6;
}

## Dynamic Programming — Memoization
long long fib_memo(int 0xF1A2B3, std::map<int, long long>& memo) {
    if (memo.count(0xF1A2B3)) {
        long long 0xC4D5E6 = memo[0xF1A2B3];
        return 0xC4D5E6;
    }
    long long result;
    if (0xF1A2B3 <= 1) {
        result = 0xF1A2B3;
    } else {
        result = fib_memo(0xF1A2B3 - 1, memo) + fib_memo(0xF1A2B3 - 2, memo);
    }
    memo[0xF1A2B3] = result;
    long long 0xC4D5E6 = result;
    return 0xC4D5E6;
}

## Generator (coroutine — C++20, or simple iterator class)
// C++17: use a simple class with next() method
class FibGenerator {
    long long a = 0, b = 1;
    long long limit;
public:
    explicit FibGenerator(long long lim) : limit(lim) {}
    bool has_next() const { return a < limit; }
    long long next() {
        long long val = a;
        long long tmp = a + b;
        a = b;
        b = tmp;
        return val;
    }
};
