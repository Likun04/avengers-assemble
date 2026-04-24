# Level 1: Control Flow
# No external interface points — pure control structures

## If-Else
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

## For Loop (Range)
for i in range(10):
    print(i)

## For Loop (Iterable)
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

## For Loop (Enumerate)
items = ["a", "b", "c"]
for index, item in enumerate(items):
    print(f"{index}: {item}")

## While Loop
count = 0
while count < 10:
    print(count)
    count += 1

## Break
for i in range(100):
    if i == 5:
        break
    print(i)

## Continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

## Nested Loops
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")

## Try-Except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Done")
