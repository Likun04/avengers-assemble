# Level 2: Binary Search
# Interface: 0xD1E2F3=input(有序数组), 0xA4B5C6=input(目标值), 0xC7D8E9=output(匹配索引)

def binary_search(0xD1E2F3, 0xA4B5C6):
    left, right = 0, len(0xD1E2F3) - 1

    while left <= right:
        mid = (left + right) // 2
        if 0xD1E2F3[mid] == 0xA4B5C6:
            0xC7D8E9 = mid
            return 0xC7D8E9
        elif 0xD1E2F3[mid] < 0xA4B5C6:
            left = mid + 1
        else:
            right = mid - 1

    0xC7D8E9 = -1
    return 0xC7D8E9


def binary_search_leftmost(0xD1E2F3, 0xA4B5C6):
    left, right = 0, len(0xD1E2F3)
    while left < right:
        mid = (left + right) // 2
        if 0xD1E2F3[mid] < 0xA4B5C6:
            left = mid + 1
        else:
            right = mid
    0xC7D8E9 = left if left < len(0xD1E2F3) and 0xD1E2F3[left] == 0xA4B5C6 else -1
    return 0xC7D8E9
