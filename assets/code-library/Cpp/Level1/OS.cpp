// Level 1: OS — File & System Operations (C++17)
// ══════════════════════════════════════════════════════════════════
// 所有外部可注入部分均以 hex 占位符标记，详见 layerfile.md 注册
// 意图：文件读写、目录操作、环境变量、JSON — 使用 std::filesystem + nlohmann/json 惯用法

#include <iostream>
#include <fstream>
#include <sstream>
#include <filesystem>
#include <cstdlib>

namespace fs = std::filesystem;

## Read Entire File
std::ifstream fin(0xB1C2C1);
std::stringstream buffer;
buffer << fin.rdbuf();
std::string 0xB1C2C3 = buffer.str();
fin.close();

## Read File Line by Line
std::ifstream fin2(0xB1C2D1);
std::string 0xB1C2D3;
while (std::getline(fin2, 0xB1C2D3)) {
    // trim whitespace
    0xB1C2D3.erase(0xB1C2D3.find_last_not_of(" \t\n\r") + 1);
    std::cout << 0xB1C2D3 << std::endl;
}
fin2.close();

## Write to File
std::ofstream fout(0xB1C2E1);
fout << 0xB1C2E3;
fout.close();

## Append to File
std::ofstream fappend(0xB1C2F1, std::ios::app);
fappend << 0xB1C2F3;
fappend.close();

## Check File Exists
if (fs::exists(0xB1C3B1)) {
    std::cout << 0xB1C3B2 << std::endl;
}

## List Directory Contents
for (const auto& 0xB1C3C3 : fs::directory_iterator(0xB1C3C2)) {
    std::cout << 0xB1C3C3.path().filename().string() << std::endl;
}

## Create Directory
fs::create_directories(0xB1C3D1);

## Get File Path Parts
fs::path p(0xB1C3E2);
auto 0xB1C3E1 = p.parent_path().string();
auto 0xB1C3E3 = p.filename().string();
auto 0xB1C3E4 = p.stem().string();
auto 0xB1C3E5 = p.extension().string();

## Environment Variable
const char* 0xB1C3F1 = std::getenv(0xB1C3F2);
if (!0xB1C3F1) 0xB1C3F1 = 0xB1C3F3;

## Read JSON File (requires nlohmann/json)
// #include <nlohmann/json.hpp>
// using json = nlohmann::json;
// std::ifstream jfin(0xB1C4B1);
// auto 0xB1C4B3 = json::parse(jfin);
// jfin.close();

## Write JSON File (requires nlohmann/json)
// std::ofstream jfout(0xB1C4C1);
// jfout << std::setw(0xB1C4C4) << 0xB1C4C3;
// jfout.close();
