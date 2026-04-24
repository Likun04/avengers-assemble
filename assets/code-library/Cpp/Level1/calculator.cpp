// Level 1: Calculator — Basic Arithmetic & Variable Operations (C++17)
// ══════════════════════════════════════════════════════════════════
// 所有外部可注入部分均以 hex 占位符标记，详见 layerfile.md 注册
// 意图：算术运算、类型转换、数学函数 — 使用 C++ 标准库惯用法

#include <cmath>
#include <cstdlib>

## Assignment and Arithmetic
auto 0xA1B2C1 = 0xA1B2C2 + 0xA1B2C3;
auto 0xA1B2D1 = 0xA1B2D2 - 0xA1B2D3;
auto 0xA1B2E1 = 0xA1B2E2 * 0xA1B2E3;
auto 0xA1B2F1 = static_cast<double>(0xA1B2F2) / 0xA1B2F3;

## Increment / Decrement
auto 0xA1C3B1 = 0xA1C3B2;
0xA1C3B1 = 0xA1C3B1 + 0xA1C3B3;
0xA1C3B1 += 0xA1C3B3;
0xA1C3B1 -= 0xA1C3B3;

## Type Conversion
auto 0xA1D4B1 = 0xA1D4B2;
auto 0xA1D4C1 = static_cast<int>(0xA1D4B1);
auto 0xA1D4D1 = static_cast<double>(0xA1D4B1);
auto 0xA1D4E1 = std::to_string(0xA1D4B1);
// round with precision — C++ lacks built-in, use std::round + power of 10
auto 0xA1D4F1 = std::round(0xA1D4F2 * std::pow(10, 0xA1D4F3)) / std::pow(10, 0xA1D4F3);

## Math Operations
auto 0xA1E5B1 = std::sqrt(0xA1E5B2);
auto 0xA1E5C1 = std::abs(0xA1E5C2);
auto 0xA1E5D1 = std::max({0xA1E5D2, 0xA1E5D3, 0xA1E5D4});
auto 0xA1E5E1 = std::min({0xA1E5E2, 0xA1E5E3, 0xA1E5E4});
auto 0xA1E5F1 = std::pow(0xA1E5F2, 0xA1E5F3);

## Modulo & Floor Division
auto 0xA1F6B1 = 0xA1F6B2 % 0xA1F6B3;
auto 0xA1F6C1 = 0xA1F6C2 / 0xA1F6C3;  // C++ integer division is already floor for positive
