// Level 1: Control Flow (C++17)
// ══════════════════════════════════════════════════════════════════
// 所有外部可注入部分均以 hex 占位符标记，详见 layerfile.md 注册
// 意图：条件分支、循环、异常处理 — 使用 range-based for + STL 惯用法

#include <iostream>
#include <vector>
#include <stdexcept>

## If-Else
if (0xC1D2C1 >= 0xC1D2C2) {
    auto 0xC1D2C3 = 0xC1D2C4;
} else if (0xC1D2C1 >= 0xC1D2C5) {
    auto 0xC1D2C3 = 0xC1D2C6;
} else if (0xC1D2C1 >= 0xC1D2C7) {
    auto 0xC1D2C3 = 0xC1D2C8;
} else {
    auto 0xC1D2C3 = 0xC1D2C9;
}

## For Loop (Range)
for (int 0xC1D2D1 = 0; 0xC1D2D1 < 0xC1D2D2; ++0xC1D2D1) {
    std::cout << 0xC1D2D1 << std::endl;
}

## For Loop (Iterable — range-based for)
std::vector<decltype(0xC1D2E2)> 0xC1D2E1 = {0xC1D2E2, 0xC1D2E3, 0xC1D2E4};
for (const auto& 0xC1D2E5 : 0xC1D2E1) {
    std::cout << 0xC1D2E5 << std::endl;
}

## For Loop (Enumerate — use index variable)
std::vector<decltype(0xC1D2F2)> 0xC1D2F1 = {0xC1D2F2, 0xC1D2F3, 0xC1D2F4};
for (size_t 0xC1D3B1 = 0; 0xC1D3B1 < 0xC1D2F1.size(); ++0xC1D3B1) {
    const auto& 0xC1D3B2 = 0xC1D2F1[0xC1D3B1];
    std::cout << 0xC1D3B1 << ": " << 0xC1D3B2 << std::endl;
}

## While Loop
auto 0xC1D3C1 = 0xC1D3C2;
while (0xC1D3C1 < 0xC1D3C3) {
    std::cout << 0xC1D3C1 << std::endl;
    0xC1D3C1 += 0xC1D3C4;
}

## Break
for (int 0xC1D3D1 = 0; 0xC1D3D1 < 0xC1D3D2; ++0xC1D3D1) {
    if (0xC1D3D1 == 0xC1D3D3) break;
    std::cout << 0xC1D3D1 << std::endl;
}

## Continue
for (int 0xC1D3E1 = 0; 0xC1D3E1 < 0xC1D3E2; ++0xC1D3E1) {
    if (0xC1D3E1 % 0xC1D3E3 == 0) continue;
    std::cout << 0xC1D3E1 << std::endl;
}

## Nested Loops
for (int 0xC1D3F1 = 0; 0xC1D3F1 < 0xC1D3F2; ++0xC1D3F1) {
    for (int 0xC1D4B1 = 0; 0xC1D4B1 < 0xC1D4B2; ++0xC1D4B1) {
        std::cout << "(" << 0xC1D3F1 << ", " << 0xC1D4B1 << ")" << std::endl;
    }
}

## Try-Catch
try {
    auto 0xC1D4C1 = 0xC1D4C2 / 0xC1D4C3;
} catch (const 0xC1D4C4& 0xC1D4C6) {
    std::cerr << 0xC1D4C5 << std::endl;
} catch (const std::exception& 0xC1D4C6) {
    std::cerr << 0xC1D4C7 << 0xC1D4C6.what() << std::endl;
} catch (...) {
    std::cout << 0xC1D4C8 << std::endl;
}
