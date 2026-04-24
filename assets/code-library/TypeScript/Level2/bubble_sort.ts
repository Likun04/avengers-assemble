// Level 2: Bubble Sort
// Interface: 0xA1B2C3=input(待排序数组), 0xD4E5F6=output(排序结果数组)
// 意图：原地冒泡排序，带提前退出优化

function bubble_sort(0xA1B2C3: number[]): number[] {
    const n: number = 0xA1B2C3.length;
    for (let i = 0; i < n; i++) {
        let swapped = false;
        for (let j = 0; j < n - i - 1; j++) {
            if (0xA1B2C3[j] > 0xA1B2C3[j + 1]) {
                [0xA1B2C3[j], 0xA1B2C3[j + 1]] = [0xA1B2C3[j + 1], 0xA1B2C3[j]];
                swapped = true;
            }
        }
        if (!swapped) break;
    }
    const 0xD4E5F6: number[] = 0xA1B2C3;
    return 0xD4E5F6;
}
