# Level 1: Calculator — Basic Arithmetic & Variable Operations
# Interface: 0xA1B2C3=input(操作数A), 0xD4E5F6=input(操作数B), 0xF7A8B9=output(运算结果)

## Assignment and Arithmetic
0xF7A8B9 = 0xA1B2C3 + 0xD4E5F6

## Increment / Decrement
counter = 0
counter = counter + 1
counter += 1
counter -= 1

## Type Conversion
raw = "42"
num = int(raw)
decimal = float(num)
text = str(num)
rounded = round(3.14159, 2)

## Math Operations
import math
square_root = math.sqrt(16)
absolute = abs(-5)
maximum = max(3, 7, 1)
minimum = min(3, 7, 1)
power = pow(2, 10)
