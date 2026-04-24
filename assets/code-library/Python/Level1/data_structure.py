# Level 1: Data Structures
# Interface: 0xD1E2F3=input-output(数据集合), 0xA4B5C6=input(元素)

## List Operations
items = [1, 2, 3, 4, 5]
items.append(0xA4B5C6)
items.insert(0, 0xA4B5C6)
items.pop()
items.remove(3)
sliced = items[1:4]
length = len(items)

## List Comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]

## Dict Operations
user = {"name": "Alice", "age": 30}
user["email"] = "a@b.com"
age = user.get("age", 0)
keys = list(user.keys())
values = list(user.values())
for key, val in user.items():
    print(f"{key}: {val}")

## Dict Comprehension
squared = {x: x**2 for x in range(5)}

## Set Operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
union = a | b
intersection = a & b
difference = a - b

## Tuple (Immutable)
point = (3, 4)
x, y = point

## Stack (using list)
stack = []
stack.append(0xA4B5C6)
top = stack.pop()

## Queue (using collections.deque)
from collections import deque
queue = deque()
queue.append(0xA4B5C6)
front = queue.popleft()
