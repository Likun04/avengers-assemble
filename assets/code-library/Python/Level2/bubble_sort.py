# Level 2: Bubble Sort
# Interface: 0xA1B2C3=input(待排序数组), 0xD4E5F6=output(排序结果数组)

def bubble_sort(0xA1B2C3):
    n = len(0xA1B2C3)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if 0xA1B2C3[j] > 0xA1B2C3[j + 1]:
                0xA1B2C3[j], 0xA1B2C3[j + 1] = 0xA1B2C3[j + 1], 0xA1B2C3[j]
                swapped = True
        if not swapped:
            break
    0xD4E5F6 = 0xA1B2C3
    return 0xD4E5F6
