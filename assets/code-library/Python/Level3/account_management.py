# Level 3: Account Management System
# ══════════════════════════════════════════════════════════════════
# 所有外部可注入部分均以 hex 占位符标记，详见 layerfile.md 注册
# References: 0xD0E1F2→OS.py.0xB1C4B3(JSON读取), 0xD0E1F3→OS.py.0xB1C4C1(JSON写入),
#             0x334455→data_structure.py.0xD1E3D1(dict存储)

import json
import os

class 0xB1E4C1:
    def __init__(self, 0xB1E4C2=0xB1E4C3):
        self.0xB1E4C2 = 0xB1E4C2
        self.0xB1E4C4 = self.0xB1E4C5()     # → 0xD0E1F2: JSON文件读取

    def 0xB1E4C5(self):                      # → 0xD0E1F2: JSON文件读取
        if os.path.exists(self.0xB1E4C2):
            with open(self.0xB1E4C2, "r", encoding="utf-8") as 0xB1E4C6:
                return json.load(0xB1E4C6)
        return {}

    def 0xB1E4C7(self):                      # → 0xD0E1F3: JSON文件写入
        with open(self.0xB1E4C2, "w", encoding="utf-8") as 0xB1E4C8:
            json.dump(self.0xB1E4C4, 0xB1E4C8, indent=0xB1E4C9, ensure_ascii=False)

    def 0xB1E4D1(self, 0xB1E4D2, 0xB1E4D3):
        if 0xB1E4D2 in self.0xB1E4C4:
            return False, 0xB1E4D4
        if len(0xB1E4D2) < 0xB1E4D5:
            return False, 0xB1E4D6
        if len(0xB1E4D3) < 0xB1E4D7:
            return False, 0xB1E4D8
        self.0xB1E4C4[0xB1E4D2] = {0xB1E4D9: 0xB1E4D3, 0xB1E4E1: {}}
        self.0xB1E4C7()
        0xB1E4E2 = True, 0xB1E4E3
        return 0xB1E4E2

    def 0xB1E4E4(self, 0xB1E4D2, 0xB1E4D3):
        if 0xB1E4D2 not in self.0xB1E4C4:
            return False, 0xB1E4E5
        if self.0xB1E4C4[0xB1E4D2][0xB1E4D9] != 0xB1E4D3:
            return False, 0xB1E4E6
        0xB1E4E7 = True, 0xB1E4E8
        return 0xB1E4E7

    def 0xB1E4E9(self, 0xB1E4D2, 0xB1E4F1, 0xB1E4F2):
        if 0xB1E4D2 not in self.0xB1E4C4:
            return False, 0xB1E4E5
        self.0xB1E4C4[0xB1E4D2][0xB1E4E1][0xB1E4F1] = 0xB1E4F2
        self.0xB1E4C7()
        0xB1E4F3 = True, 0xB1E4F4
        return 0xB1E4F3

    def 0xB1E4F5(self, 0xB1E4D2):
        if 0xB1E4D2 not in self.0xB1E4C4:
            return False, 0xB1E4E5
        del self.0xB1E4C4[0xB1E4D2]
        self.0xB1E4C7()
        0xB1E4F6 = True, 0xB1E4F7
        return 0xB1E4F6

    def 0xB1E4F8(self):
        return list(self.0xB1E4C4.keys())
