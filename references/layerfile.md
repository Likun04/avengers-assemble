# Layerfile — Code Library Index
# ══════════════════════════════════════════════════════════════════
# This is the index catalog for all code materials.
#
# Convention:
#   hex = 0x?????? (6-digit hex address, globally unique)
#   type: variable    → Replace with business variable name during assembly
#   type: reference   → Expand into another material's code (cross-file)
#   type: literal     → Replace with a business-specific value (string, number, etc.)
#
# Safety Gate: Before using any material, run Avengers.py scan (Step 2.5 in SKILL.md)
#   The scanner checks if the material activates any dangerous intent topology
#   Single nodes are harmless; only connected intent paths trigger alerts

# ══════════════════════════════════════════════════════════════════
# LEVEL 1 — Atomic Operations
# ══════════════════════════════════════════════════════════════════

## calculator.py — Basic Arithmetic & Variable Operations
# Source: assets/code-library/Python/Level1/calculator.py
# Function: 算术运算、赋值、类型转换、数学函数
# Keywords: 算术, 加减乘除, 赋值, 类型转换, 数学, sqrt, abs, max, min, pow, 取模, 整除
| hex       | type     | role            | description                    |
|-----------|----------|-----------------|--------------------------------|
| 0xA1B2C1  | variable | output          | 赋值运算结果                    |
| 0xA1B2C2  | variable | input           | 加法左操作数                    |
| 0xA1B2C3  | variable | input           | 加法右操作数                    |
| 0xA1B2D1  | variable | output          | 减法结果                        |
| 0xA1B2D2  | variable | input           | 减法左操作数                    |
| 0xA1B2D3  | variable | input           | 减法右操作数                    |
| 0xA1B2E1  | variable | output          | 乘法结果                        |
| 0xA1B2E2  | variable | input           | 乘法左操作数                    |
| 0xA1B2E3  | variable | input           | 乘法右操作数                    |
| 0xA1B2F1  | variable | output          | 除法结果                        |
| 0xA1B2F2  | variable | input           | 除法左操作数                    |
| 0xA1B2F3  | variable | input           | 除法右操作数                    |
| 0xA1C3B1  | variable | input-output    | 计数器变量                      |
| 0xA1C3B2  | literal  | initial_value   | 计数器初始值                    |
| 0xA1C3B3  | literal  | step            | 自增/自减步长                   |
| 0xA1D4B1  | variable | input           | 待转换的原始值                  |
| 0xA1D4B2  | literal  | string_value    | 字符串形式的数字                |
| 0xA1D4C1  | variable | output          | int() 转换结果                  |
| 0xA1D4D1  | variable | output          | float() 转换结果                |
| 0xA1D4E1  | variable | output          | str() 转换结果                  |
| 0xA1D4F1  | variable | output          | round() 四舍五入结果            |
| 0xA1D4F2  | variable | input           | 待四舍五入的数值                |
| 0xA1D4F3  | literal  | precision       | 保留小数位数                    |
| 0xA1E5B1  | variable | output          | 平方根结果                      |
| 0xA1E5B2  | variable | input           | 开方底数                        |
| 0xA1E5C1  | variable | output          | 绝对值结果                      |
| 0xA1E5C2  | variable | input           | 取绝对值的数值                  |
| 0xA1E5D1  | variable | output          | 最大值结果                      |
| 0xA1E5D2  | variable | input           | 比较值 1                       |
| 0xA1E5D3  | variable | input           | 比较值 2                       |
| 0xA1E5D4  | variable | input           | 比较值 3                       |
| 0xA1E5E1  | variable | output          | 最小值结果                      |
| 0xA1E5E2  | variable | input           | 比较值 1                       |
| 0xA1E5E3  | variable | input           | 比较值 2                       |
| 0xA1E5E4  | variable | input           | 比较值 3                       |
| 0xA1E5F1  | variable | output          | 幂运算结果                      |
| 0xA1E5F2  | variable | input           | 底数                            |
| 0xA1E5F3  | variable | input           | 指数                            |
| 0xA1F6B1  | variable | output          | 取模结果                        |
| 0xA1F6B2  | variable | input           | 被除数                          |
| 0xA1F6B3  | variable | input           | 除数                            |
| 0xA1F6C1  | variable | output          | 整除结果                        |
| 0xA1F6C2  | variable | input           | 被除数                          |
| 0xA1F6C3  | variable | input           | 除数                            |

## console.py — Console I/O
# Source: assets/code-library/Python/Level1/console.py
# Function: 打印输出、用户输入、格式化输出、日志
# Keywords: 打印, print, input, 输入, 输出, 格式化, f-string, logging, 日志, stderr
| hex       | type     | role            | description                    |
|-----------|----------|-----------------|--------------------------------|
| 0xF1A2C1  | variable | input           | print 单参数                    |
| 0xF1A2C2  | literal  | label           | print 多参数 label 1            |
| 0xF1A2C3  | variable | input           | print 多参数 value 1            |
| 0xF1A2C4  | literal  | label           | print 多参数 label 2            |
| 0xF1A2C5  | variable | input           | print 多参数 value 2            |
| 0xF1A2D1  | variable | output          | 用户输入值                      |
| 0xF1A2D2  | variable | input           | input 提示文本                  |
| 0xF1A2E1  | variable | input           | 格式化的变量                    |
| 0xF1A2E2  | literal  | label           | 变量描述标签                    |
| 0xF1A2E3  | literal  | prefix          | f-string 前缀文本               |
| 0xF1A2E4  | literal  | separator       | f-string 分隔符                 |
| 0xF1A2E5  | literal  | format_spec     | 格式说明符                      |
| 0xF1A2F1  | literal  | prefix          | 表头前缀                        |
| 0xF1A2F2  | literal  | header_text     | 表头文本 1                      |
| 0xF1A2F3  | literal  | width           | 格式宽度                        |
| 0xF1A2F4  | literal  | header_text     | 表头文本 2                      |
| 0xF1A2F5  | variable | input           | 表头变量值                      |
| 0xF1A2F6  | literal  | format_spec     | 格式说明符                      |
| 0xF1B3C1  | literal  | error_msg       | stderr 错误消息                |
| 0xF1B3D1  | literal  | log_level       | 日志级别                        |
| 0xF1B3D2  | literal  | format_str      | 日志格式字符串                  |
| 0xF1B3D3  | literal  | info_msg        | info 日志消息                   |
| 0xF1B3D4  | literal  | warning_msg     | warning 日志消息                |
| 0xF1B3D5  | literal  | error_msg       | error 日志消息                  |
| 0xF1B3E1  | variable | input           | 表格数据列表                    |
| 0xF1B3E2  | variable | input           | 表格行数据 1                    |
| 0xF1B3E3  | variable | input           | 表格行数据 2                    |
| 0xF1B3E4  | variable | input           | 表格行数据 3                    |
| 0xF1B3E5  | variable | input           | 表格行数据 4                    |
| 0xF1B3F1  | variable | input           | 循环变量名 1                    |
| 0xF1B3F2  | variable | input           | 循环变量名 2                    |
| 0xF1B3F3  | literal  | col_width       | 列宽格式                        |
| 0xF1B3F4  | literal  | col_width       | 列宽格式                        |

## control_flow.py — Control Flow Structures
# Source: assets/code-library/Python/Level1/control_flow.py
# Function: 条件判断、循环、异常处理
# Keywords: if, else, elif, for, while, 循环, 条件, break, continue, enumerate, try, except, 异常
| hex       | type     | role            | description                    |
|-----------|----------|-----------------|--------------------------------|
| 0xC1D2C1  | variable | input           | 条件判断变量                    |
| 0xC1D2C2  | literal  | threshold_high  | 最高阈值                        |
| 0xC1D2C3  | variable | output          | 条件分支结果                    |
| 0xC1D2C4  | literal  | result_A        | A 级结果                       |
| 0xC1D2C5  | literal  | threshold_mid   | 中间阈值                        |
| 0xC1D2C6  | literal  | result_B        | B 级结果                       |
| 0xC1D2C7  | literal  | threshold_low   | 低阈值                          |
| 0xC1D2C8  | literal  | result_C        | C 级结果                       |
| 0xC1D2C9  | literal  | result_F        | 默认结果                        |
| 0xC1D2D1  | variable | input           | 循环变量                        |
| 0xC1D2D2  | literal  | range_end       | 循环范围上限                    |
| 0xC1D2E1  | variable | input           | 可迭代对象                      |
| 0xC1D2E2  | variable | input           | 列表元素 1                      |
| 0xC1D2E3  | variable | input           | 列表元素 2                      |
| 0xC1D2E4  | variable | input           | 列表元素 3                      |
| 0xC1D2E5  | variable | input           | 迭代变量                        |
| 0xC1D2F1  | variable | input           | enumerate 可迭代对象            |
| 0xC1D2F2  | variable | input           | 列表元素 1                      |
| 0xC1D2F3  | variable | input           | 列表元素 2                      |
| 0xC1D2F4  | variable | input           | 列表元素 3                      |
| 0xC1D3B1  | variable | output          | enumerate 索引                  |
| 0xC1D3B2  | variable | output          | enumerate 值                    |
| 0xC1D3C1  | variable | input-output    | while 循环控制变量              |
| 0xC1D3C2  | literal  | initial_value   | 初始值                          |
| 0xC1D3C3  | literal  | range_end       | 循环结束条件                    |
| 0xC1D3C4  | literal  | step            | 步长                            |
| 0xC1D3D1  | variable | input           | break 循环变量                  |
| 0xC1D3D2  | literal  | range_end       | 循环范围上限                    |
| 0xC1D3D3  | literal  | break_condition  | break 触发条件                  |
| 0xC1D3E1  | variable | input           | continue 循环变量               |
| 0xC1D3E2  | literal  | range_end       | 循环范围上限                    |
| 0xC1D3E3  | literal  | modulo_divisor  | 取模除数                        |
| 0xC1D3F1  | variable | input           | 外层循环变量                    |
| 0xC1D3F2  | literal  | outer_range     | 外层循环范围                    |
| 0xC1D4B1  | variable | input           | 内层循环变量                    |
| 0xC1D4B2  | literal  | inner_range     | 内层循环范围                    |
| 0xC1D4C1  | variable | output          | 除法结果                        |
| 0xC1D4C2  | literal  | dividend        | 被除数                          |
| 0xC1D4C3  | literal  | divisor         | 除数                            |
| 0xC1D4C4  | literal  | exception_type  | 异常类型                        |
| 0xC1D4C5  | literal  | exception_msg   | 异常处理消息                    |
| 0xC1D4C6  | variable | output          | 通用异常对象                    |
| 0xC1D4C7  | literal  | prefix          | 错误消息前缀                    |
| 0xC1D4C8  | literal  | finally_msg     | finally 块消息                 |

## function.py — Function Definition
# Source: assets/code-library/Python/Level1/function.py
# Function: 函数定义、默认参数、lambda、装饰器
# Keywords: 函数, def, return, lambda, 默认参数, *args, **kwargs, 装饰器, decorator
| hex       | type     | role            | description                    |
|-----------|----------|-----------------|--------------------------------|
| 0xF4A5C1  | variable | function_name   | 基本函数名                      |
| 0xF4A5C2  | variable | input(param)    | 函数参数                        |
| 0xF4A5C3  | variable | output(return)  | 返回值                          |
| 0xF4A5D1  | variable | function_name   | 默认参数函数名                  |
| 0xF4A5D2  | variable | input(param)    | 函数参数                        |
| 0xF4A5D3  | variable | input(param)    | 默认参数名                      |
| 0xF4A5D4  | literal  | default_value   | 默认值                          |
| 0xF4A5E1  | variable | function_name   | 多返回值函数名                  |
| 0xF4A5E2  | variable | input(param)    | 函数参数（可迭代）              |
| 0xF4A5F1  | variable | output          | lambda 赋值目标                 |
| 0xF4A5F2  | variable | input(param)    | lambda 参数                     |
| 0xF4B6C1  | variable | output          | lambda 赋值目标                 |
| 0xF4B6C2  | variable | input(param)    | lambda 参数 1                   |
| 0xF4B6C3  | variable | input(param)    | lambda 参数 2                   |
| 0xF4B6D1  | variable | function_name   | *args 函数名                    |
| 0xF4B6D2  | variable | input(*args)    | 可变位置参数                    |
| 0xF4B6E1  | variable | function_name   | **kwargs 函数名                 |
| 0xF4B6E2  | variable | input(**kwargs) | 可变关键字参数                  |
| 0xF4B6E3  | variable | input           | 字典键变量                      |
| 0xF4B6E4  | variable | input           | 字典值变量                      |
| 0xF4B6F1  | variable | function_name   | 装饰器函数名                    |
| 0xF4B6F2  | variable | input(param)    | 被装饰函数                      |
| 0xF4B7C1  | variable | function_name   | wrapper 函数名                  |
| 0xF4B7C2  | variable | input(*args)    | wrapper 可变位置参数            |
| 0xF4B7C3  | variable | input(**kwargs) | wrapper 可变关键字参数          |
| 0xF4B7C4  | variable | output          | 开始时间                        |
| 0xF4B7C5  | variable | output          | 函数执行结果                    |
| 0xF4B7C6  | variable | output          | 结束时间                        |

## data_structure.py — Data Structures
# Source: assets/code-library/Python/Level1/data_structure.py
# Function: 列表、字典、集合、元组、栈、队列操作
# Keywords: 列表, list, 字典, dict, 集合, set, 元组, tuple, 栈, stack, 队列, queue, 推导式
| hex       | type     | role            | description                    |
|-----------|----------|-----------------|--------------------------------|
| 0xD1E2C1  | variable | input-output    | 列表变量                        |
| 0xD1E2C2  | variable | input           | 列表初始元素 1                  |
| 0xD1E2C3  | variable | input           | 列表初始元素 2                  |
| 0xD1E2C4  | variable | input           | 列表初始元素 3                  |
| 0xD1E2C5  | variable | input           | 列表初始元素 4                  |
| 0xD1E2C6  | variable | input           | 列表初始元素 5                  |
| 0xD1E2C7  | variable | input           | append/insert 元素              |
| 0xD1E2C8  | literal  | index           | insert 位置索引                 |
| 0xD1E2C9  | variable | input           | remove 元素值                   |
| 0xD1E2D1  | variable | output          | 切片结果                        |
| 0xD1E2D2  | literal  | slice_start     | 切片起始                        |
| 0xD1E2D3  | literal  | slice_end       | 切片结束                        |
| 0xD1E2E1  | variable | output          | 列表长度                        |
| 0xD1E2F1  | variable | output          | 推导式结果列表                  |
| 0xD1E2F2  | variable | input           | 推导式迭代变量                  |
| 0xD1E2F3  | literal  | exponent        | 推导式幂次                      |
| 0xD1E2F4  | literal  | range_end       | 推导式范围上限                  |
| 0xD1E3C1  | variable | output          | 过滤推导式结果                  |
| 0xD1E3C2  | variable | input           | 过滤迭代变量                    |
| 0xD1E3C3  | literal  | range_end       | 过滤范围上限                    |
| 0xD1E3C4  | literal  | modulo_divisor  | 过滤条件除数                    |
| 0xD1E3D1  | variable | input-output    | 字典变量                        |
| 0xD1E3D2  | variable | input           | 字典键 1                        |
| 0xD1E3D3  | variable | input           | 字典值 1                        |
| 0xD1E3D4  | variable | input           | 字典键 2                        |
| 0xD1E3D5  | variable | input           | 字典值 2                        |
| 0xD1E3D6  | variable | input           | 新增键                          |
| 0xD1E3D7  | variable | input           | 新增值                          |
| 0xD1E3E1  | variable | output          | get() 结果                      |
| 0xD1E3E2  | literal  | default_value   | get() 默认值                    |
| 0xD1E3E3  | variable | output          | keys() 列表                     |
| 0xD1E3E4  | variable | output          | values() 列表                   |
| 0xD1E3E5  | variable | input           | 遍历键变量                      |
| 0xD1E3E6  | variable | input           | 遍历值变量                      |
| 0xD1E3F1  | variable | output          | 字典推导式结果                  |
| 0xD1E3F2  | variable | input           | 推导式迭代变量                  |
| 0xD1E3F3  | literal  | exponent        | 推导式幂次                      |
| 0xD1E3F4  | literal  | range_end       | 推导式范围上限                  |
| 0xD1E4B1  | variable | input           | 集合 A                          |
| 0xD1E4B2  | variable | input           | 集合 A 元素 1                   |
| 0xD1E4B3  | variable | input           | 集合 A 元素 2                   |
| 0xD1E4B4  | variable | input           | 共有元素 1                      |
| 0xD1E4B5  | variable | input           | 共有元素 2                      |
| 0xD1E4B6  | variable | input           | 集合 B                          |
| 0xD1E4B7  | variable | input           | 集合 B 独有元素 1               |
| 0xD1E4B8  | variable | input           | 集合 B 独有元素 2               |
| 0xD1E4C1  | variable | output          | 并集结果                        |
| 0xD1E4C2  | variable | output          | 交集结果                        |
| 0xD1E4C3  | variable | output          | 差集结果                        |
| 0xD1E4D1  | variable | output          | 元组                            |
| 0xD1E4D2  | variable | input           | 元组元素 1                      |
| 0xD1E4D3  | variable | input           | 元组元素 2                      |
| 0xD1E4D4  | variable | output          | 解包元素 1                      |
| 0xD1E4D5  | variable | output          | 解包元素 2                      |
| 0xD1E4E1  | variable | input-output    | 栈（列表）                      |
| 0xD1E4E2  | variable | input           | 入栈元素                        |
| 0xD1E4E3  | variable | output          | 出栈元素                        |
| 0xD1E4F1  | variable | input-output    | 队列（deque）                   |
| 0xD1E4F2  | variable | input           | 入队元素                        |
| 0xD1E4F3  | variable | output          | 出队元素                        |

## string.py — String Operations
# Source: assets/code-library/Python/Level1/string.py
# Function: 字符串操作、格式化、正则、编解码
# Keywords: 字符串, string, 分割, 拼接, 替换, 查找, 正则, regex, encode, decode, strip
| hex       | type     | role            | description                    |
|-----------|----------|-----------------|--------------------------------|
| 0xE1F2C1  | variable | output          | 字符串长度                      |
| 0xE1F2C2  | variable | input           | 原始字符串                      |
| 0xE1F2C3  | variable | output          | 大写结果                        |
| 0xE1F2C4  | variable | output          | 小写结果                        |
| 0xE1F2C5  | variable | output          | 去空格结果                      |
| 0xE1F2C6  | variable | input           | 待 strip 的字符串               |
| 0xE1F2D1  | variable | input           | 格式化变量 1                    |
| 0xE1F2D2  | literal  | label           | 变量描述                        |
| 0xE1F2D3  | variable | input           | 格式化变量 2                    |
| 0xE1F2D4  | literal  | label           | 变量描述                        |
| 0xE1F2D5  | variable | output          | 格式化结果字符串                |
| 0xE1F2D6  | variable | output          | 格式化结果字符串                |
| 0xE1F2D7  | variable | input           | 待格式化数值                    |
| 0xE1F2D8  | literal  | format_spec     | 格式说明符                      |
| 0xE1F2E1  | variable | output          | split 结果列表                  |
| 0xE1F2E2  | variable | input           | 待分割字符串                    |
| 0xE1F2E3  | literal  | delimiter       | 分隔符                          |
| 0xE1F2E4  | variable | output          | join 结果字符串                 |
| 0xE1F2E5  | literal  | delimiter       | 连接符                          |
| 0xE1F2F1  | variable | output          | replace 结果                    |
| 0xE1F2F2  | variable | input           | 原始字符串                      |
| 0xE1F2F3  | literal  | old_substring   | 被替换子串                      |
| 0xE1F2F4  | literal  | new_substring   | 替换子串                        |
| 0xE1F3B1  | variable | output          | find 位置索引                   |
| 0xE1F3B2  | variable | input           | 搜索目标字符串                  |
| 0xE1F3B3  | literal  | substring       | 查找的子串                      |
| 0xE1F3B4  | variable | output          | in 运算结果                     |
| 0xE1F3C1  | variable | output          | findall 结果列表                |
| 0xE1F3C2  | literal  | regex_pattern   | 正则表达式                      |
| 0xE1F3C3  | variable | input           | 正则匹配目标字符串              |
| 0xE1F3C4  | variable | output          | sub 替换结果                    |
| 0xE1F3C5  | literal  | regex_pattern   | 正则表达式                      |
| 0xE1F3C6  | literal  | replacement     | 替换文本                        |
| 0xE1F3C7  | variable | output          | match 结果                      |
| 0xE1F3C8  | literal  | regex_pattern   | 正则表达式                      |
| 0xE1F3C9  | variable | input           | match 目标字符串                |
| 0xE1F3D1  | variable | output          | 字符列表                        |
| 0xE1F3D2  | variable | input           | 原始字符串                      |
| 0xE1F3E1  | variable | output          | 多行字符串结果                  |
| 0xE1F3E2  | literal  | multiline_text  | 多行文本内容                    |
| 0xE1F3F1  | variable | output          | 编码结果                        |
| 0xE1F3F2  | variable | input           | 待编码字符串                    |
| 0xE1F3F3  | literal  | encoding        | 编码格式                        |
| 0xE1F3F4  | variable | output          | 解码结果                        |

## OS.py — File & System Operations
# Source: assets/code-library/Python/Level1/OS.py
# Function: 文件读写、路径操作、环境变量、JSON 处理
# Keywords: 文件, file, 读取, 写入, 追加, 路径, path, 目录, 环境变量, JSON, os
| hex       | type     | role            | description                    |
|-----------|----------|-----------------|--------------------------------|
| 0xB1C2C1  | variable | input           | 文件路径                        |
| 0xB1C2C2  | variable | output          | 文件句柄                        |
| 0xB1C2C3  | variable | output          | 读取的文件内容                  |
| 0xB1C2D1  | variable | input           | 文件路径                        |
| 0xB1C2D2  | variable | output          | 文件句柄                        |
| 0xB1C2D3  | variable | output          | 行内容                          |
| 0xB1C2E1  | variable | input           | 写入文件路径                    |
| 0xB1C2E2  | variable | output          | 文件句柄                        |
| 0xB1C2E3  | variable | input           | 写入内容                        |
| 0xB1C2F1  | variable | input           | 追加文件路径                    |
| 0xB1C2F2  | variable | output          | 文件句柄                        |
| 0xB1C2F3  | variable | input           | 追加内容                        |
| 0xB1C3B1  | variable | input           | 检查路径                        |
| 0xB1C3B2  | literal  | message         | 存在时的消息                    |
| 0xB1C3C1  | variable | output          | 目录文件列表                    |
| 0xB1C3C2  | variable | input           | 目录路径                        |
| 0xB1C3C3  | variable | output          | 文件名变量                      |
| 0xB1C3D1  | variable | input           | 创建目录路径                    |
| 0xB1C3E1  | variable | output          | 目录名                          |
| 0xB1C3E2  | variable | input           | 完整文件路径                    |
| 0xB1C3E3  | variable | output          | 文件基名                        |
| 0xB1C3E4  | variable | output          | 文件名（无扩展名）              |
| 0xB1C3E5  | variable | output          | 扩展名                          |
| 0xB1C3F1  | variable | output          | 环境变量值                      |
| 0xB1C3F2  | literal  | env_key         | 环境变量名                      |
| 0xB1C3F3  | literal  | default_value   | 默认值                          |
| 0xB1C4B1  | variable | input           | JSON 文件路径                   |
| 0xB1C4B2  | variable | output          | 文件句柄                        |
| 0xB1C4B3  | variable | output          | JSON 解析结果（dict/list）      |
| 0xB1C4C1  | variable | input           | JSON 写入文件路径               |
| 0xB1C4C2  | variable | output          | 文件句柄                        |
| 0xB1C4C3  | variable | input           | 待序列化数据                    |
| 0xB1C4C4  | literal  | indent          | JSON 缩进空格数                 |

# ══════════════════════════════════════════════════════════════════
# LEVEL 2 — Algorithmic Patterns
# ══════════════════════════════════════════════════════════════════

## bubble_sort.py — Bubble Sort
# Source: assets/code-library/Python/Level2/bubble_sort.py
# Function: 比较排序，时间复杂度 O(n²)
# Keywords: 排序, 冒泡排序, bubble sort, 比较排序, 升序
| hex       | type     | role            | description                    |
|-----------|----------|-----------------|--------------------------------|
| 0xA1B2C3  | variable | input-output    | 待排序数组（原地排序）          |
| 0xD4E5F6  | variable | output          | 排序结果数组                    |

## binary_search.py — Binary Search
# Source: assets/code-library/Python/Level2/binary_search.py
# Function: 有序数组二分查找，时间复杂度 O(log n)
# Keywords: 查找, 二分查找, binary search, 有序数组, 搜索
| hex       | type     | role            | description                    |
|-----------|----------|-----------------|--------------------------------|
| 0xD1E2F3  | variable | input           | 有序数组                        |
| 0xA4B5C6  | variable | input           | 目标值                          |
| 0xC7D8E9  | variable | output          | 匹配索引（未找到返回 -1）       |

## fibonacci.py — Fibonacci Sequence
# Source: assets/code-library/Python/Level2/fibonacci.py
# Function: 斐波那契数列（递归/DP/记忆化/生成器）
# Keywords: 斐波那契, fibonacci, 递归, 动态规划, DP, 记忆化, 生成器, generator
| hex       | type     | role            | description                    |
|-----------|----------|-----------------|--------------------------------|
| 0xF1A2B3  | variable | input           | 数列项数 n                      |
| 0xC4D5E6  | variable | output          | 第 n 项计算结果                 |
| limit     | variable | input           | 生成器上限值（fib_generator）   |

## dfs_bfs.py — Graph Traversal
# Source: assets/code-library/Python/Level2/dfs_bfs.py
# Function: 深度优先/广度优先搜索，最短路径
# Keywords: 图, 遍历, DFS, BFS, 深度优先, 广度优先, 最短路径, shortest path
| hex       | type     | role            | description                    |
|-----------|----------|-----------------|--------------------------------|
| 0xE1F2A3  | variable | input           | 图邻接表（dict: node→list）    |
| 0xB4C5D6  | variable | input           | 起始节点                        |
| 0xD7E8F9  | variable | output          | 遍历结果（set: visited nodes） |
| start     | variable | input           | 起始节点（shortest_path）       |
| end       | variable | input           | 目标节点（shortest_path）       |

## greedy_algorithm.py — Greedy Algorithm
# Source: assets/code-library/Python/Level2/greedy_algorithm.py
# Function: 贪心算法（活动选择、硬币找零）
# Keywords: 贪心, greedy, 活动选择, 区间调度, 硬币找零, coin change
| hex       | type     | role            | description                    |
|-----------|----------|-----------------|--------------------------------|
| 0xB1C2D1  | variable | function_name   | 活动选择函数名                  |
| 0xB1C2D2  | variable | input           | 活动列表（list of tuples）      |
| 0xB1C2D3  | variable | output          | 排序后的活动列表                |
| 0xB1C2D4  | variable | input           | lambda 迭代变量                 |
| 0xB1C2D5  | literal  | sort_key_index  | 排序依据的字段索引              |
| 0xB1C2D6  | variable | output          | 已选活动列表                    |
| 0xB1C2D7  | variable | output          | 上一个活动的结束时间            |
| 0xB1C2D8  | literal  | end_time_index  | 结束时间字段索引                |
| 0xB1C2D9  | variable | input           | 活动开始时间                    |
| 0xB1C2E1  | variable | input           | 活动结束时间                    |
| 0xB1C2E2  | literal  | slice_start     | 切片起始（跳过第一个）          |
| 0xB1C2E3  | variable | output          | 最终选中结果                    |
| 0xB1C2E4  | variable | function_name   | 硬币找零函数名                  |
| 0xB1C2E5  | variable | input           | 可用面额列表                    |
| 0xB1C2E6  | variable | output          | 降序排列的面额列表              |
| 0xB1C2E7  | variable | output          | 找零结果（dict: coin→count）    |
| 0xB1C2E8  | variable | input           | 当前面额                        |
| 0xB1C2E9  | variable | output          | 该面额使用数量                  |
| 0xB1C2F1  | variable | output          | 最终返回结果                    |
| amount    | variable | input           | 待找零金额                      |

## game_of_life.py — Conway's Game of Life
# Source: assets/code-library/Python/Level2/game_of_life.py
# Function: 元胞自动机生命游戏模拟
# Keywords: 元胞自动机, 康威生命游戏, game of life, 网格模拟, cellular automaton
| hex       | type     | role            | description                    |
|-----------|----------|-----------------|--------------------------------|
| 0xC1D2C1  | variable | function_name   | 创建空网格函数                  |
| 0xC1D2C2  | variable | function_name   | 随机化网格函数                  |
| 0xC1D2C3  | variable | output          | 行索引                          |
| 0xC1D2C4  | variable | output          | 列索引                          |
| 0xC1D2C5  | variable | function_name   | 计算邻居数函数                  |
| 0xC1D2C6  | variable | output          | 网格行数                        |
| 0xC1D2C7  | variable | output          | 网格列数                        |
| 0xC1D2C8  | variable | output          | 邻居计数                        |
| 0xC1D2C9  | variable | input           | 行偏移量                        |
| 0xC1D2D1  | variable | input           | 列偏移量                        |
| 0xC1D2D2  | variable | output          | 邻居行坐标                      |
| 0xC1D2D3  | variable | output          | 邻居列坐标                      |
| 0xC1D2D4  | variable | function_name   | 下一代演化函数                  |
| 0xC1D2D5  | variable | output          | 新网格行数                      |
| 0xC1D2D6  | variable | output          | 新网格列数                      |
| 0xC1D2D7  | variable | output          | 新网格                          |
| 0xC1D2D8  | variable | output          | 当前行索引                      |
| 0xC1D2D9  | variable | output          | 当前列索引                      |
| 0xC1D2E1  | variable | output          | 邻居数量                        |
| 0xC1D2E2  | variable | function_name   | 打印网格函数                    |
| 0xC1D2E3  | variable | input           | 网格行数据                      |
| 0xC1D2E4  | variable | output          | 格式化行字符串                  |
| 0xC1D2E5  | variable | input           | 单元格状态                      |
| 0xC1F4B1  | variable | input-output    | 网格状态                        |
| 0xC1F4B2  | variable | input           | 网格列数                        |
| 0xC1F4B3  | variable | output          | 当前代数变量                    |
| 0xC1F4B4  | literal  | generation_count| 演化总代数                      |
| 0xC1F4B5  | variable | output          | 循环代数变量                    |
| 0xC1D2E6  | variable | input           | 网格行数（usage 中）            |

# ══════════════════════════════════════════════════════════════════
# LEVEL 3 — Architectural Patterns
# ══════════════════════════════════════════════════════════════════

## account_management.py — Account Management System
# Source: assets/code-library/Python/Level3/account_management.py
# Function: 用户注册、登录、信息管理（JSON 持久化）
# Keywords: 账户, 用户, 注册, 登录, CRUD, 认证, authentication, 用户管理
# References:
#   0xD0E1F2 → OS.py.0xB1C4B3 (JSON 文件读取)
#   0xD0E1F3 → OS.py.0xB1C4C1 (JSON 文件写入)
#   0x334455 → data_structure.py.0xD1E3D1 (dict 存储)
| hex       | type     | role            | description                    |
|-----------|----------|-----------------|--------------------------------|
| 0xB1E4C1  | variable | class_name      | 账户管理器类名                  |
| 0xB1E4C2  | variable | input           | 存储文件路径（构造参数）        |
| 0xB1E4C3  | literal  | default_path    | 默认文件路径                    |
| 0xB1E4C4  | variable | input-output    | 账户字典数据                    |
| 0xB1E4C5  | variable | function_name   | 加载方法                        |
| 0xB1E4C6  | variable | output          | 文件句柄                        |
| 0xB1E4C7  | variable | function_name   | 保存方法                        |
| 0xB1E4C8  | variable | output          | 文件句柄                        |
| 0xB1E4C9  | literal  | indent          | JSON 缩进数                     |
| 0xB1E4D1  | variable | function_name   | 注册方法                        |
| 0xB1E4D2  | variable | input           | 用户名                          |
| 0xB1E4D3  | variable | input           | 密码                            |
| 0xB1E4D4  | literal  | error_msg       | 用户已存在错误                  |
| 0xB1E4D5  | literal  | min_length      | 用户名最小长度                  |
| 0xB1E4D6  | literal  | error_msg       | 用户名太短错误                  |
| 0xB1E4D7  | literal  | min_length      | 密码最小长度                    |
| 0xB1E4D8  | literal  | error_msg       | 密码太短错误                    |
| 0xB1E4D9  | literal  | dict_key        | password 字段键名               |
| 0xB1E4E1  | literal  | dict_key        | info 字段键名                   |
| 0xB1E4E2  | variable | output          | 操作结果元组                    |
| 0xB1E4E3  | literal  | success_msg     | 注册成功消息模板                |
| 0xB1E4E4  | variable | function_name   | 登录方法                        |
| 0xB1E4E5  | literal  | error_msg       | 用户不存在错误                  |
| 0xB1E4E6  | literal  | error_msg       | 密码错误                        |
| 0xB1E4E7  | variable | output          | 登录结果元组                    |
| 0xB1E4E8  | literal  | success_msg     | 登录成功消息模板                |
| 0xB1E4E9  | variable | function_name   | 更新信息方法                    |
| 0xB1E4F1  | variable | input           | 信息字段键名                    |
| 0xB1E4F2  | variable | input           | 信息字段值                      |
| 0xB1E4F3  | variable | output          | 操作结果元组                    |
| 0xB1E4F4  | literal  | success_msg     | 更新成功消息模板                |
| 0xB1E4F5  | variable | function_name   | 删除账户方法                    |
| 0xB1E4F6  | variable | output          | 操作结果元组                    |
| 0xB1E4F7  | literal  | success_msg     | 删除成功消息模板                |
| 0xB1E4F8  | variable | function_name   | 列出账户方法                    |

## actor_system.py — Actor System
# Source: assets/code-library/Python/Level3/actor_system.py
# Function: 消息传递并发模型（Actor 模式）
# Keywords: Actor, 并发, 消息传递, 邮箱, mailbox, 广播, broadcast
# References:
#   0x112233 → data_structure.py.0xD1E4F1 (消息队列 deque)
#   0x445566 → function.py.0xF4B6D1 (处理器注册)
| hex       | type     | role            | description                    |
|-----------|----------|-----------------|--------------------------------|
| 0xA1D4C1  | variable | class_name      | Actor 类名                      |
| 0xA1D4C2  | variable | input           | Actor 名称                      |
| 0xA1D4C3  | variable | input           | 自定义消息处理函数              |
| 0xA1D4C4  | variable | output          | Actor 名称（self 属性）         |
| 0xA1D4C5  | variable | input-output    | 消息邮箱（deque）               |
| 0xA1D4C6  | variable | input-output    | 消息处理函数                    |
| 0xA1D4C7  | variable | function_name   | 默认处理函数                    |
| 0xA1D4C8  | variable | output          | 运行状态标志                    |
| 0xA1D4C9  | variable | input           | 消息内容                        |
| 0xA1D4D1  | variable | input           | 发送者名称                      |
| 0xA1D4D2  | variable | function_name   | 发送消息方法                    |
| 0xA1D4D3  | literal  | default_sender  | 默认发送者名                    |
| 0xA1D4D4  | literal  | default_sender  | 默认发送者值                    |
| 0xA1D4D5  | variable | function_name   | 处理全部消息方法                |
| 0xA1D4D6  | variable | class_name      | ActorSystem 类名                |
| 0xA1D4D7  | variable | input-output    | Actor 注册表（dict）            |
| 0xA1D4D8  | variable | function_name   | 注册 Actor 方法                 |
| 0xA1D4D9  | variable | input           | Actor 实例                      |
| 0xA1D4E1  | variable | input           | 目标 Actor 名称                 |
| 0xA1D4E2  | variable | function_name   | 处理指定 Actor 消息方法         |
| 0xA1D4E3  | variable | input           | Actor 名称                      |
| 0xA1D4E4  | variable | function_name   | 广播方法                        |
| 0xA1D4E5  | variable | output          | 循环中的 Actor 名称              |
| 0xA1D4E6  | variable | function_name   | 处理所有 Actor 消息方法         |
| 0xA1D4E7  | variable | output          | 循环中的 Actor 实例              |

## api_server.py — Basic API Server
# Source: assets/code-library/Python/Level3/api_server.py
# Function: 基于 http.server 的 REST API 服务器
# Keywords: API, 服务器, REST, HTTP, 端点, endpoint, GET, POST, JSON
# References:
#   0x566778 → OS.py.0xB1C4C3 (JSON 序列化)
#   0x889900 → data_structure.py.0xD1E3D1 (dict 数据存储)
| hex       | type     | role            | description                    |
|-----------|----------|-----------------|--------------------------------|
| 0xC1F4C1  | variable | input-output    | 数据存储字典                    |
| 0xC1F4C2  | literal  | dict_key        | 数据集合键名（如 "items"）     |
| 0xC1F4C3  | literal  | dict_key        | ID 字段键名                     |
| 0xC1F4C4  | literal  | id_value        | 记录 1 的 ID                    |
| 0xC1F4C5  | literal  | dict_key        | 名称字段键名                    |
| 0xC1F4C6  | literal  | name_value      | 记录 1 的名称                   |
| 0xC1F4C7  | literal  | dict_key        | 价格字段键名                    |
| 0xC1F4C8  | literal  | price_value     | 记录 1 的价格                   |
| 0xC1F4C9  | literal  | id_value        | 记录 2 的 ID                    |
| 0xC1F4D1  | literal  | name_value      | 记录 2 的名称                   |
| 0xC1F4D2  | literal  | price_value     | 记录 2 的价格                   |
| 0xC1F4D3  | variable | class_name      | 请求处理器类名                  |
| 0xC1F4D4  | variable | function_name   | 发送 JSON 响应方法              |
| 0xC1F4D5  | variable | input           | 响应数据                        |
| 0xC1F4D6  | literal  | status_code     | HTTP 状态码                     |
| 0xC1F4D7  | literal  | status_code     | 默认状态码（200）               |
| 0xC1F4D8  | literal  | header_name     | Content-Type 头名               |
| 0xC1F4D9  | literal  | header_value    | application/json                |
| 0xC1F4E1  | literal  | encoding        | 编码格式                        |
| 0xC1F4E2  | literal  | endpoint        | 集合端点路径（如 "/items"）     |
| 0xC1F4E3  | literal  | endpoint_prefix  | 单项端点前缀（如 "/items/"）    |
| 0xC1F4E4  | variable | output          | 解析出的 ID 值                  |
| 0xC1F4E5  | literal  | delimiter       | URL 路径分隔符                  |
| 0xC1F4E6  | variable | output          | 查找到的记录                    |
| 0xC1F4E7  | variable | input           | 循环遍历的记录变量              |
| 0xC1F4E8  | literal  | dict_key        | error 字段键名                  |
| 0xC1F4E9  | literal  | error_msg       | 未找到错误消息                  |
| 0xC1F4F1  | literal  | status_code     | 404 状态码                      |
| 0xC1F4F4  | variable | output          | 请求体长度                      |
| 0xC1F4F5  | literal  | header_name     | Content-Length 头名             |
| 0xC1F4F6  | variable | output          | 解析出的请求体                  |
| 0xC1F4F7  | variable | output          | 新生成的 ID                     |
| 0xC1F4F8  | literal  | status_code     | 201 状态码                      |
| 0xC1F4F9  | literal  | error_msg       | 端点不存在错误                  |
| 0xC1F5B1  | variable | input           | 日志格式字符串                  |
| 0xC1F5B2  | variable | input           | 日志参数                        |
| 0xC1F5B3  | variable | function_name   | 启动服务器函数                  |
| 0xC1F5B4  | variable | input           | 主机地址                        |
| 0xC1F5B5  | literal  | default_host    | 默认主机（如 "localhost"）      |
| 0xC1F5B6  | variable | input           | 端口号                          |
| 0xC1F5B7  | literal  | default_port    | 默认端口号（如 8080）           |
| 0xC1F5B8  | variable | output          | HTTP 服务器实例                 |
| 0xC1F5B9  | literal  | message         | 端点列表提示消息                |
| 0xC1F5C1  | literal  | message         | 服务器停止消息                  |
