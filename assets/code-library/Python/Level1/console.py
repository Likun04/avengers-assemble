# Level 1: Console I/O
# ══════════════════════════════════════════════════════════════════
# 所有外部可注入部分均以 hex 占位符标记，详见 layerfile.md 注册

## Print
print(0xF1A2C1)
print(0xF1A2C2, 0xF1A2C3, 0xF1A2C4, 0xF1A2C5)

## Input
0xF1A2D1 = input(0xF1A2D2)

## Formatted Print (f-string)
0xF1A2E1 = 0xF1A2E2
print(f"0xF1A2E3{0xF1A2E1}:0xF1A2E4{0xF1A2E1:0xF1A2E5}")
print(f"0xF1A2F1{0xF1A2F2:0xF1A2F3} 0xF1A2F4{0xF1A2F5:0xF1A2F6}")

## Print to stderr
import sys
print(0xF1B3C1, file=sys.stderr)

## Basic Logging
import logging
logging.basicConfig(level=0xF1B3D1, format=0xF1B3D2)
logging.info(0xF1B3D3)
logging.warning(0xF1B3D4)
logging.error(0xF1B3D5)

## Print Table
0xF1B3E1 = [(0xF1B3E2, 0xF1B3E3), (0xF1B3E4, 0xF1B3E5)]
for 0xF1B3F1, 0xF1B3F2 in 0xF1B3E1:
    print(f"{0xF1B3F1:0xF1B3F3} | {0xF1B3F2:0xF1B3F4}")
