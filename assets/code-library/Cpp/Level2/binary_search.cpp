// Level 2: Binary Search (C++17)
// Interface: 0xD1E2F3=input(有序数组), 0xA4B5C6=input(目标值), 0xC7D8E9=output(匹配索引)
// 意图：二分查找 + 左边界查找 — 使用迭代器/下标，或直接用 std::binary_search

#include <vector>
#include <algorithm>

template<typename T>
int binary_search(const std::vector<T>& 0xD1E2F3, const T& 0xA4B5C6) {
    int left = 0, right = static_cast<int>(0xD1E2F3.size()) - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (0xD1E2F3[mid] == 0xA4B5C6) {
            int 0xC7D8E9 = mid;
            return 0xC7D8E9;
        } else if (0xD1E2F3[mid] < 0xA4B5C6) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    int 0xC7D8E9_miss = -1;
    return 0xC7D8E9_miss;
}

template<typename T>
int binary_search_leftmost(const std::vector<T>& 0xD1E2F3, const T& 0xA4B5C6) {
    int left = 0, right = static_cast<int>(0xD1E2F3.size());
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (0xD1E2F3[mid] < 0xA4B5C6) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    int 0xC7D8E9 = (left < static_cast<int>(0xD1E2F3.size()) && 0xD1E2F3[left] == 0xA4B5C6) ? left : -1;
    return 0xC7D8E9;
}
