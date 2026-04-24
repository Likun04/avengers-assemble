# Level 1: Function Definition
# ══════════════════════════════════════════════════════════════════
# 所有外部可注入部分均以 hex 占位符标记，详见 layerfile.md 注册

## Basic Function
def 0xF4A5C1(0xF4A5C2):
    return 0xF4A5C3

## Function with Default Parameters
def 0xF4A5D1(0xF4A5D2, 0xF4A5D3=0xF4A5D4):
    return 0xF4A5D2 ** 0xF4A5D3

## Function with Multiple Returns
def 0xF4A5E1(0xF4A5E2):
    return min(0xF4A5E2), max(0xF4A5E2)

## Lambda
0xF4A5F1 = lambda 0xF4A5F2: 0xF4A5F2 * 0xF4A5F2
0xF4B6C1 = lambda 0xF4B6C2, 0xF4B6C3: 0xF4B6C2 + 0xF4B6C3

## Function with *args
def 0xF4B6D1(*0xF4B6D2):
    return sum(0xF4B6D2)

## Function with **kwargs
def 0xF4B6E1(**0xF4B6E2):
    for 0xF4B6E3, 0xF4B6E4 in 0xF4B6E2.items():
        print(f"{0xF4B6E3}: {0xF4B6E4}")

## Decorator
def 0xF4B6F1(0xF4B6F2):
    import time
    def 0xF4B7C1(*0xF4B7C2, **0xF4B7C3):
        0xF4B7C4 = time.time()
        0xF4B7C5 = 0xF4B6F2(*0xF4B7C2, **0xF4B7C3)
        0xF4B7C6 = time.time()
        print(f"{0xF4B6F2.__name__} took {0xF4B7C6 - 0xF4B7C4:.4f}s")
        return 0xF4B7C5
    return 0xF4B7C1
