// Level 1: String Operations (C++17)
// ══════════════════════════════════════════════════════════════════
// 所有外部可注入部分均以 hex 占位符标记，详见 layerfile.md 注册
// 意图：字符串操作 — 使用 std::string + <regex> + <sstream> 惯用法

#include <iostream>
#include <string>
#include <vector>
#include <regex>
#include <sstream>
#include <algorithm>
#include <cctype>

## Basic String
auto 0xE1F2C1 = 0xE1F2C2.length();
std::string 0xE1F2C3 = 0xE1F2C2;
std::transform(0xE1F2C3.begin(), 0xE1F2C3.end(), 0xE1F2C3.begin(), ::toupper);
std::string 0xE1F2C4 = 0xE1F2C2;
std::transform(0xE1F2C4.begin(), 0xE1F2C4.end(), 0xE1F2C4.begin(), ::tolower);
std::string 0xE1F2C5 = 0xE1F2C6;
0xE1F2C5.erase(0xE1F2C5.begin(), std::find_if(0xE1F2C5.begin(), 0xE1F2C5.end(), [](int ch) { return !std::isspace(ch); }));
0xE1F2C5.erase(std::find_if(0xE1F2C5.rbegin(), 0xE1F2C5.rend(), [](int ch) { return !std::isspace(ch); }).base(), 0xE1F2C5.end());

## String Format (ostringstream)
auto 0xE1F2D1 = 0xE1F2D2;
auto 0xE1F2D3 = 0xE1F2D4;
std::string 0xE1F2D5 = std::to_string(0xE1F2D1) + " is " + std::to_string(0xE1F2D3) + " years old";
// formatted number
std::ostringstream oss;
oss << std::fixed << std::setprecision(0xE1F2D8) << 0xE1F2D7;
std::string 0xE1F2D6 = "Pi is " + oss.str();

## String Split & Join
std::vector<std::string> 0xE1F2E1;
std::string token;
std::istringstream iss(0xE1F2E2);
while (std::getline(iss, token, 0xE1F2E3[0])) {
    0xE1F2E1.push_back(token);
}
std::string 0xE1F2E4;
for (size_t i = 0; i < 0xE1F2E1.size(); ++i) {
    if (i > 0) 0xE1F2E4 += 0xE1F2E5;
    0xE1F2E4 += 0xE1F2E1[i];
}

## String Replace
std::string 0xE1F2F1 = 0xE1F2F2;
size_t pos = 0;
while ((pos = 0xE1F2F1.find(0xE1F2F3, pos)) != std::string::npos) {
    0xE1F2F1.replace(pos, 0xE1F2F3.length(), 0xE1F2F4);
    pos += 0xE1F2F4.length();
}

## String Find
auto 0xE1F3B1 = 0xE1F3B2.find(0xE1F3B3);  // returns std::string::npos if not found
bool 0xE1F3B4 = (0xE1F3B2.find(0xE1F3B3) != std::string::npos);

## Regex
std::regex re(0xE1F3C2);
std::vector<std::string> 0xE1F3C1;
auto words_begin = std::sregex_iterator(0xE1F3C3.begin(), 0xE1F3C3.end(), re);
auto words_end = std::sregex_iterator();
for (auto it = words_begin; it != words_end; ++it) {
    0xE1F3C1.push_back(it->str());
}
std::string 0xE1F3C4 = std::regex_replace(0xE1F3C3, std::regex(0xE1F3C5), 0xE1F3C6);
std::smatch 0xE1F3C7;
std::regex_search(0xE1F3C9, 0xE1F3C7, std::regex(0xE1F3C8));

## String to Vector (Character)
std::vector<char> 0xE1F3D1(0xE1F3D2.begin(), 0xE1F3D2.end());

## Multiline String (C++11 raw string literal)
const char* 0xE1F3E1 = 0xE1F3E2;
