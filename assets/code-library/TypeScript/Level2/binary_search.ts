// Level 2: Binary Search
// Interface: 0xD1E2F3=input(有序数组), 0xA4B5C6=input(目标值), 0xC7D8E9=output(匹配索引)
// 意图：二分查找 + 左边界查找

function binary_search(0xD1E2F3: number[], 0xA4B5C6: number): number {
    let left = 0, right = 0xD1E2F3.length - 1;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (0xD1E2F3[mid] === 0xA4B5C6) {
            const 0xC7D8E9: number = mid;
            return 0xC7D8E9;
        } else if (0xD1E2F3[mid] < 0xA4B5C6) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    const 0xC7D8E9_miss: number = -1;
    return 0xC7D8E9_miss;
}


function binary_search_leftmost(0xD1E2F3: number[], 0xA4B5C6: number): number {
    let left = 0, right = 0xD1E2F3.length;
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (0xD1E2F3[mid] < 0xA4B5C6) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    const 0xC7D8E9: number = (left < 0xD1E2F3.length && 0xD1E2F3[left] === 0xA4B5C6) ? left : -1;
    return 0xC7D8E9;
}
