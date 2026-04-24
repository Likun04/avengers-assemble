# Level 1: OS — File & System Operations
# ══════════════════════════════════════════════════════════════════
# 所有外部可注入部分均以 hex 占位符标记，详见 layerfile.md 注册

## Read Entire File
with open(0xB1C2C1, "r", encoding="utf-8") as 0xB1C2C2:
    0xB1C2C3 = 0xB1C2C2.read()

## Read File Line by Line
with open(0xB1C2D1, "r", encoding="utf-8") as 0xB1C2D2:
    for 0xB1C2D3 in 0xB1C2D2:
        print(0xB1C2D3.strip())

## Write to File
with open(0xB1C2E1, "w", encoding="utf-8") as 0xB1C2E2:
    0xB1C2E2.write(0xB1C2E3)

## Append to File
with open(0xB1C2F1, "a", encoding="utf-8") as 0xB1C2F2:
    0xB1C2F2.write(0xB1C2F3)

## Check File Exists
import os
if os.path.exists(0xB1C3B1):
    print(0xB1C3B2)

## List Directory Contents
import os
0xB1C3C1 = os.listdir(0xB1C3C2)
for 0xB1C3C3 in 0xB1C3C1:
    print(0xB1C3C3)

## Create Directory
import os
os.makedirs(0xB1C3D1, exist_ok=True)

## Get File Path Parts
import os
0xB1C3E1 = os.path.dirname(0xB1C3E2)
0xB1C3E3 = os.path.basename(0xB1C3E2)
0xB1C3E4, 0xB1C3E5 = os.path.splitext(0xB1C3E3)

## Environment Variable
import os
0xB1C3F1 = os.environ.get(0xB1C3F2, 0xB1C3F3)

## Read JSON File
import json
with open(0xB1C4B1, "r", encoding="utf-8") as 0xB1C4B2:
    0xB1C4B3 = json.load(0xB1C4B2)

## Write JSON File
import json
with open(0xB1C4C1, "w", encoding="utf-8") as 0xB1C4C2:
    json.dump(0xB1C4C3, 0xB1C4C2, indent=0xB1C4C4, ensure_ascii=False)
