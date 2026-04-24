# Level 1: String Operations
# Interface: 0xE1F2A3=input(原始字符串), 0xB4C5D6=output(处理结果)

## Basic String
length = len(0xE1F2A3)
upper = 0xE1F2A3.upper()
lower = 0xE1F2A3.lower()
stripped = "  hello  ".strip()

## String Format (f-string)
name = "Alice"
age = 30
msg = f"{name} is {age} years old"
pi_str = f"Pi is {3.14159:.2f}"

## String Split & Join
parts = 0xE1F2A3.split(",")
0xB4C5D6 = "-".join(parts)

## String Replace
0xB4C5D6 = 0xE1F2A3.replace("world", "Python")

## String Find
pos = 0xE1F2A3.find("world")
has_sub = "world" in 0xE1F2A3

## Regex
import re
emails = re.findall(r"\w+@\w+\.\w+", 0xE1F2A3)
cleaned = re.sub(r"[^a-zA-Z0-9]", "", 0xE1F2A3)
is_match = re.match(r"^\d+$", "12345")

## String to List (Character)
chars = list(0xE1F2A3)

## Multiline String
template = """Line 1
Line 2
Line 3
"""

## Encode / Decode
encoded = 0xE1F2A3.encode("utf-8")
decoded = encoded.decode("utf-8")
