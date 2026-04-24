# Level 1: Function Definition
# Interface: 0xC1D2E3=input(函数名), 0xF4A5B6=input(参数列表), 0xB7C8D9=output(返回值)

## Basic Function
def 0xC1D2E3(0xF4A5B6):
    return 0xB7C8D9

## Function with Default Parameters
def 0xC1D2E3(0xF4A5B6, exp=2):
    return 0xF4A5B6 ** exp

## Function with Multiple Returns
def min_max(numbers):
    return min(numbers), max(numbers)

## Lambda
square = lambda x: x * x
add = lambda a, b: a + b

## Function with *args
def total(*args):
    return sum(args)

## Function with **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

## Decorator
def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result
    return wrapper
