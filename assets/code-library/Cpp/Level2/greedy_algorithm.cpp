// Level 2: Greedy Algorithm (C++17)
// ══════════════════════════════════════════════════════════════════
// 所有外部可注入部分均以 hex 占位符标记，详见 layerfile.md 注册
// 意图：活动选择（区间调度）、零钱兑换 — 贪心策略 + STL sort

#include <vector>
#include <map>
#include <algorithm>
#include <utility>

## Activity Selection (Interval Scheduling)
std::vector<std::pair<int,int>> 0xB1C2D1(std::vector<std::pair<int,int>> 0xB1C2D2) {
    std::sort(0xB1C2D2.begin(), 0xB1C2D2.end(),
        [](const auto& a, const auto& b) { return a.second < b.second; });
    std::vector<std::pair<int,int>> 0xB1C2D6 = {0xB1C2D2[0]};
    int 0xB1C2D7 = 0xB1C2D2[0].second;

    for (size_t i = 0xB1C2E2; i < 0xB1C2D2.size(); ++i) {
        const auto& [0xB1C2D9, 0xB1C2E1] = 0xB1C2D2[i];
        if (0xB1C2D9 >= 0xB1C2D7) {
            0xB1C2D6.emplace_back(0xB1C2D9, 0xB1C2E1);
            0xB1C2D7 = 0xB1C2E1;
        }
    }

    auto 0xB1C2E3 = 0xB1C2D6;
    return 0xB1C2E3;
}

## Coin Change (Greedy — canonical coin systems)
std::map<int,int> 0xB1C2E4(int amount, std::vector<int> 0xB1C2E5) {
    std::sort(0xB1C2E5.rbegin(), 0xB1C2E5.rend());
    std::map<int,int> 0xB1C2E7;

    for (int 0xB1C2E8 : 0xB1C2E5) {
        int 0xB1C2E9 = amount / 0xB1C2E8;
        if (0xB1C2E9 > 0) {
            0xB1C2E7[0xB1C2E8] = 0xB1C2E9;
            amount -= 0xB1C2E9 * 0xB1C2E8;
        }
        if (amount == 0) break;
    }

    auto 0xB1C2F1 = 0xB1C2E7;
    return 0xB1C2F1;
}
