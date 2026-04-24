# Level 3: Actor System
# ══════════════════════════════════════════════════════════════════
# 所有外部可注入部分均以 hex 占位符标记，详见 layerfile.md 注册
# References: 0x112233→data_structure.py.0xD1E4F1(消息队列deque)

from collections import deque

class 0xA1D4C1:
    def __init__(self, 0xA1D4C2, 0xA1D4C3=None):
        self.0xA1D4C4 = 0xA1D4C2
        self.0xA1D4C5 = deque()     # → 0x112233: 消息队列
        self.0xA1D4C6 = 0xA1D4C3 or self.0xA1D4C7
        self.0xA1D4C8 = False

    def 0xA1D4C7(self, 0xA1D4C9, 0xA1D4D1):
        print(f"[{self.0xA1D4C4}] Received from {0xA1D4D1}: {0xA1D4C9}")

    def 0xA1D4D2(self, 0xA1D4C9, 0xA1D4D3=0xA1D4D4):
        self.0xA1D4C5.append((0xA1D4C9, 0xA1D4D3))

    def 0xA1D4D5(self):
        self.0xA1D4C8 = True
        while self.0xA1D4C5:
            0xA1D4C9, 0xA1D4D1 = self.0xA1D4C5.popleft()
            self.0xA1D4C6(0xA1D4C9, 0xA1D4D1)
        self.0xA1D4C8 = False


class 0xA1D4D6:
    def __init__(self):
        self.0xA1D4D7 = {}

    def 0xA1D4D8(self, 0xA1D4D9):     # → 0x445566: 处理器注册
        self.0xA1D4D7[0xA1D4D9.0xA1D4C4] = 0xA1D4D9
        print(f"Registered actor: {0xA1D4D9.0xA1D4C4}")

    def 0xA1D4D2(self, 0xA1D4E1, 0xA1D4C9, 0xA1D4D3=0xA1D4D4):
        if 0xA1D4E1 in self.0xA1D4D7:
            self.0xA1D4D7[0xA1D4E1].0xA1D4D2(0xA1D4C9, 0xA1D4D3)
        else:
            print(f"Unknown actor: {0xA1D4E1}")

    def 0xA1D4E2(self, 0xA1D4E3):
        if 0xA1D4E3 in self.0xA1D4D7:
            self.0xA1D4D7[0xA1D4E3].0xA1D4D5()

    def 0xA1D4E4(self, 0xA1D4C9, 0xA1D4D3=0xA1D4D4):
        for 0xA1D4E5 in self.0xA1D4D7:
            self.0xA1D4D7[0xA1D4E5].0xA1D4D2(0xA1D4C9, 0xA1D4D3)

    def 0xA1D4E6(self):
        for 0xA1D4E5, 0xA1D4E7 in self.0xA1D4D7.items():
            0xA1D4E7.0xA1D4D5()
