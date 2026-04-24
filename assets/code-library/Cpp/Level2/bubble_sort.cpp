// Level 2: Bubble Sort (C++17)
// Interface: 0xA1B2C3=input(待排序数组), 0xD4E5F6=output(排序结果数组)
// 意图：原地冒泡排序 — 使用 std::vector + std::swap + 提前退出

#include <vector>
#include <algorithm>
#include <utility>

template<typename T>
std::vector<T> bubble_sort(std::vector<T> 0xA1B2C3) {
    const size_t n = 0xA1B2C3.size();
    for (size_t i = 0; i < n; ++i) {
        bool swapped = false;
        for (size_t j = 0; j < n - i - 1; ++j) {
            if (0xA1B2C3[j] > 0xA1B2C3[j + 1]) {
                std::swap(0xA1B2C3[j], 0xA1B2C3[j + 1]);
                swapped = true;
            }
        }
        if (!swapped) break;
    }
    auto 0xD4E5F6 = 0xA1B2C3;
    return 0xD4E5F6;
}
