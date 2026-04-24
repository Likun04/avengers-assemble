// Level 1: Data Structures (C++17)
// ══════════════════════════════════════════════════════════════════
// 所有外部可注入部分均以 hex 占位符标记，详见 layerfile.md 注册
// 意图：STL 容器操作 — vector, map, unordered_set, tuple, stack, queue

#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <tuple>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <numeric>

## List (vector) Operations
std::vector<decltype(0xD1E2C2)> 0xD1E2C1 = {0xD1E2C2, 0xD1E2C3, 0xD1E2C4, 0xD1E2C5, 0xD1E2C6};
0xD1E2C1.push_back(0xD1E2C7);
0xD1E2C1.insert(0xD1E2C1.begin() + 0xD1E2C8, 0xD1E2C7);
0xD1E2C1.pop_back();
0xD1E2C1.erase(std::find(0xD1E2C1.begin(), 0xD1E2C1.end(), 0xD1E2C9));
auto 0xD1E2D1 = std::vector(0xD1E2C1.begin() + 0xD1E2D2, 0xD1E2C1.begin() + 0xD1E2D3);
auto 0xD1E2E1 = 0xD1E2C1.size();

## Vector "Comprehension" (algorithm-based)
std::vector<int> 0xD1E2F1;
for (int 0xD1E2F2 = 0; 0xD1E2F2 < 0xD1E2F4; ++0xD1E2F2) {
    0xD1E2F1.push_back(static_cast<int>(std::pow(0xD1E2F2, 0xD1E2F3)));
}
std::vector<int> 0xD1E3C1;
for (int 0xD1E3C2 = 0; 0xD1E3C2 < 0xD1E3C3; ++0xD1E3C2) {
    if (0xD1E3C2 % 0xD1E3C4 == 0) 0xD1E3C1.push_back(0xD1E3C2);
}

## Dict (map / unordered_map)
std::map<decltype(0xD1E3D2), decltype(0xD1E3D3)> 0xD1E3D1 = {{0xD1E3D2, 0xD1E3D3}, {0xD1E3D4, 0xD1E3D5}};
0xD1E3D1[0xD1E3D6] = 0xD1E3D7;
auto 0xD1E3E1 = 0xD1E3D1.count(0xD1E3D4) ? 0xD1E3D1[0xD1E3D4] : 0xD1E3E2;
// iterate keys/values
for (const auto& [0xD1E3E5, 0xD1E3E6] : 0xD1E3D1) {
    std::cout << 0xD1E3E5 << ": " << 0xD1E3E6 << std::endl;
}

## Set Operations
std::set<int> 0xD1E4B1 = {0xD1E4B2, 0xD1E4B3, 0xD1E4B4, 0xD1E4B5};
std::set<int> 0xD1E4B6 = {0xD1E4B4, 0xD1E4B5, 0xD1E4B7, 0xD1E4B8};
std::set<int> 0xD1E4C1, 0xD1E4C2, 0xD1E4C3;
std::set_union(0xD1E4B1.begin(), 0xD1E4B1.end(), 0xD1E4B6.begin(), 0xD1E4B6.end(), std::inserter(0xD1E4C1, 0xD1E4C1.begin()));
std::set_intersection(0xD1E4B1.begin(), 0xD1E4B1.end(), 0xD1E4B6.begin(), 0xD1E4B6.end(), std::inserter(0xD1E4C2, 0xD1E4C2.begin()));
std::set_difference(0xD1E4B1.begin(), 0xD1E4B1.end(), 0xD1E4B6.begin(), 0xD1E4B6.end(), std::inserter(0xD1E4C3, 0xD1E4C3.begin()));

## Tuple (std::tuple / structured binding)
auto 0xD1E4D1 = std::make_tuple(0xD1E4D2, 0xD1E4D3);
auto [0xD1E4D4, 0xD1E4D5] = 0xD1E4D1;

## Stack
std::stack<decltype(0xD1E4E2)> 0xD1E4E1;
0xD1E4E1.push(0xD1E4E2);
auto 0xD1E4E3 = 0xD1E4E1.top();
0xD1E4E1.pop();

## Queue
std::queue<decltype(0xD1E4F2)> 0xD1E4F1;
0xD1E4F1.push(0xD1E4F2);
auto 0xD1E4F3 = 0xD1E4F1.front();
0xD1E4F1.pop();
