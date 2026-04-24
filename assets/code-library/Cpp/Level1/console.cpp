// Level 1: Console I/O (C++17)
// ══════════════════════════════════════════════════════════════════
// 所有外部可注入部分均以 hex 占位符标记，详见 layerfile.md 注册
// 意图：控制台输入输出 — 使用 iostream + iomanip + fmt(C++20) 惯用法

#include <iostream>
#include <iomanip>
#include <string>

## Print
std::cout << 0xF1A2C1 << std::endl;
std::cout << 0xF1A2C2 << " " << 0xF1A2C3 << " " << 0xF1A2C4 << " " << 0xF1A2C5 << std::endl;

## Input
std::string 0xF1A2D1;
std::cout << 0xF1A2D2;
std::getline(std::cin, 0xF1A2D1);

## Formatted Print (iomanip)
auto 0xF1A2E1 = 0xF1A2E2;
std::cout << 0xF1A2E3 << 0xF1A2E1 << std::endl;
std::cout << std::fixed << std::setprecision(0xF1A2E5) << 0xF1A2E1 << std::endl;
std::cout << 0xF1A2F1 << std::setw(0xF1A2F3) << 0xF1A2F2 << " "
          << 0xF1A2F4 << std::setw(0xF1A2F6) << 0xF1A2F5 << std::endl;

## Print to stderr
std::cerr << 0xF1B3C1 << std::endl;

## Basic Logging (C++ has no built-in level logging; use cerr for errors)
// 0xF1B3D1: "DEBUG" | "INFO" | "WARNING" | "ERROR"
// 0xF1B3D2: format string (not directly supported, use cout)
std::cout << "[INFO] " << 0xF1B3D3 << std::endl;
std::cerr << "[WARNING] " << 0xF1B3D4 << std::endl;
std::cerr << "[ERROR] " << 0xF1B3D5 << std::endl;

## Print Table
// C++ table printing using iomanip alignment
std::cout << std::left << std::setw(0xF1B3F3) << 0xF1B3E2 << " | "
          << std::left << std::setw(0xF1B3F4) << 0xF1B3E3 << std::endl;
std::cout << std::left << std::setw(0xF1B3F3) << 0xF1B3E4 << " | "
          << std::left << std::setw(0xF1B3F4) << 0xF1B3E5 << std::endl;
