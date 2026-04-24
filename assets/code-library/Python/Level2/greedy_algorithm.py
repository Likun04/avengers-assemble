# Level 2: Greedy Algorithm
# ══════════════════════════════════════════════════════════════════
# 所有外部可注入部分均以 hex 占位符标记，详见 layerfile.md 注册

## Activity Selection (Interval Scheduling)
def 0xB1C2D1(0xB1C2D2):
    0xB1C2D3 = sorted(0xB1C2D2, key=lambda 0xB1C2D4: 0xB1C2D4[0xB1C2D5])
    0xB1C2D6 = [0xB1C2D3[0]]
    0xB1C2D7 = 0xB1C2D3[0][0xB1C2D8]

    for 0xB1C2D9, 0xB1C2E1 in 0xB1C2D3[0xB1C2E2:]:
        if 0xB1C2D9 >= 0xB1C2D7:
            0xB1C2D6.append((0xB1C2D9, 0xB1C2E1))
            0xB1C2D7 = 0xB1C2E1

    0xB1C2E3 = 0xB1C2D6
    return 0xB1C2E3


## Coin Change (Greedy — canonical coin systems)
def 0xB1C2E4(amount, 0xB1C2E5):
    0xB1C2E6 = sorted(0xB1C2E5, reverse=True)
    0xB1C2E7 = {}

    for 0xB1C2E8 in 0xB1C2E6:
        0xB1C2E9 = amount // 0xB1C2E8
        if 0xB1C2E9 > 0:
            0xB1C2E7[0xB1C2E8] = 0xB1C2E9
            amount -= 0xB1C2E9 * 0xB1C2E8
        if amount == 0:
            break

    0xB1C2F1 = 0xB1C2E7
    return 0xB1C2F1
