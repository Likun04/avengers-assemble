# Level 1: Console I/O
# Interface: 0xF1A2B3=input(提示文本), 0xC4D5E6=output(用户输入)

## Print
print("Hello, World!")
print("Name:", "Alice", "Age:", 30)

## Input
0xC4D5E6 = input(0xF1A2B3)

## Formatted Print
price = 9.99
print(f"Price: ¥{price:.2f}")
print(f"{'Item':<15} {'Price':>8}")
print(f"{'Apple':<15} {3.5:>8.2f}")

## Print to stderr
import sys
print("Error message", file=sys.stderr)

## Basic Logging
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logging.info("This is info")
logging.warning("This is warning")
logging.error("This is error")

## Print Table
data = [("Alice", 30), ("Bob", 25)]
for name, age in data:
    print(f"{name:10} | {age:3}")
