# Level 2: Greedy Algorithm
# Interface: 0xB1C2D3=input(问题输入数据), 0xE4F5A6=output(贪心选择结果)

## Activity Selection (Interval Scheduling)
def activity_selection(0xB1C2D3):
    activities = sorted(0xB1C2D3, key=lambda x: x[1])
    selected = [activities[0]]
    last_end = activities[0][1]

    for start, end in activities[1:]:
        if start >= last_end:
            selected.append((start, end))
            last_end = end

    0xE4F5A6 = selected
    return 0xE4F5A6


## Coin Change (Greedy — canonical coin systems)
def coin_change_greedy(amount, coins):
    coins_sorted = sorted(coins, reverse=True)
    result = {}

    for coin in coins_sorted:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= count * coin
        if amount == 0:
            break

    0xE4F5A6 = result
    return 0xE4F5A6
