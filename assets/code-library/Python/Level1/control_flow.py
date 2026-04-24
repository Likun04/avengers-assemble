# Level 1: Control Flow
# ══════════════════════════════════════════════════════════════════
# 所有外部可注入部分均以 hex 占位符标记，详见 layerfile.md 注册

## If-Else
if 0xC1D2C1 >= 0xC1D2C2:
    0xC1D2C3 = 0xC1D2C4
elif 0xC1D2C1 >= 0xC1D2C5:
    0xC1D2C3 = 0xC1D2C6
elif 0xC1D2C1 >= 0xC1D2C7:
    0xC1D2C3 = 0xC1D2C8
else:
    0xC1D2C3 = 0xC1D2C9

## For Loop (Range)
for 0xC1D2D1 in range(0xC1D2D2):
    print(0xC1D2D1)

## For Loop (Iterable)
0xC1D2E1 = [0xC1D2E2, 0xC1D2E3, 0xC1D2E4]
for 0xC1D2E5 in 0xC1D2E1:
    print(0xC1D2E5)

## For Loop (Enumerate)
0xC1D2F1 = [0xC1D2F2, 0xC1D2F3, 0xC1D2F4]
for 0xC1D3B1, 0xC1D3B2 in enumerate(0xC1D2F1):
    print(f"{0xC1D3B1}: {0xC1D3B2}")

## While Loop
0xC1D3C1 = 0xC1D3C2
while 0xC1D3C1 < 0xC1D3C3:
    print(0xC1D3C1)
    0xC1D3C1 += 0xC1D3C4

## Break
for 0xC1D3D1 in range(0xC1D3D2):
    if 0xC1D3D1 == 0xC1D3D3:
        break
    print(0xC1D3D1)

## Continue
for 0xC1D3E1 in range(0xC1D3E2):
    if 0xC1D3E1 % 0xC1D3E3 == 0:
        continue
    print(0xC1D3E1)

## Nested Loops
for 0xC1D3F1 in range(0xC1D3F2):
    for 0xC1D4B1 in range(0xC1D4B2):
        print(f"({0xC1D3F1}, {0xC1D4B1})")

## Try-Except
try:
    0xC1D4C1 = 0xC1D4C2 / 0xC1D4C3
except 0xC1D4C4:
    print(0xC1D4C5)
except Exception as 0xC1D4C6:
    print(f"0xC1D4C7{0xC1D4C6}")
finally:
    print(0xC1D4C8)
