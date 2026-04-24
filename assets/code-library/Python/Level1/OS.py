# Level 1: OS — File & System Operations
# Interface: 0xB1C2D3=input(文件路径), 0xE4F5A6=input-output(文件内容)

## Read Entire File
with open(0xB1C2D3, "r", encoding="utf-8") as f:
    0xE4F5A6 = f.read()

## Read File Line by Line
with open(0xB1C2D3, "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

## Write to File
with open(0xB1C2D3, "w", encoding="utf-8") as f:
    f.write(0xE4F5A6)

## Append to File
with open(0xB1C2D3, "a", encoding="utf-8") as f:
    f.write(0xE4F5A6)

## Check File Exists
import os
if os.path.exists(0xB1C2D3):
    print("File exists")

## List Directory Contents
import os
files = os.listdir(0xB1C2D3)
for f in files:
    print(f)

## Create Directory
import os
os.makedirs(0xB1C2D3, exist_ok=True)

## Get File Path Parts
import os
dirname = os.path.dirname(0xB1C2D3)
basename = os.path.basename(0xB1C2D3)
name, ext = os.path.splitext(basename)

## Environment Variable
import os
home = os.environ.get("HOME", "/default/path")

## Read JSON File
import json
with open(0xB1C2D3, "r", encoding="utf-8") as f:
    0xE4F5A6 = json.load(f)

## Write JSON File
import json
with open(0xB1C2D3, "w", encoding="utf-8") as f:
    json.dump(0xE4F5A6, f, indent=2, ensure_ascii=False)
