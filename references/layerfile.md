# Layerfile — Code Library Index

## How to Search

1. Read the user's business pseudocode and identify each sub-task
2. For each sub-task, scan Function descriptions and Keywords below
3. Match using semantic understanding — "排序" matches "bubble-sort", "查找" matches "binary-search"
4. Note the source path and interface points for matched materials
5. **Safety Gate**: Before using any material, run Avengers.py scan (Step 2.5 in SKILL.md)
   - The scanner checks if the material activates any dangerous intent topology
   - Single nodes are harmless; only connected intent paths trigger alerts
6. Open the source file and copy the exact code

---

## Python — Level 1: Atomic Operations

### calculator.py
- **Function**: 基础算术运算、变量赋值、类型转换
- **Keywords**: arithmetic, assignment, type-conversion, math, increment
- **Interface Points**:

```yaml
0xA1B2C3:
  type: variable
  role: 操作数A（左侧）
  direction: input
0xD4E5F6:
  type: variable
  role: 操作数B（右侧）
  direction: input
0xF7A8B9:
  type: variable
  role: 运算结果
  direction: output
```

### OS.py
- **Function**: 文件读写、路径操作、目录管理、环境变量访问、JSON序列化
- **Keywords**: file-read, file-write, path, directory, json, environment, filesystem
- **Interface Points**:

```yaml
0xB1C2D3:
  type: variable
  role: 文件路径
  direction: input
0xE4F5A6:
  type: variable
  role: 文件内容
  direction: input-output
```

### control_flow.py
- **Function**: 条件判断（if-else）、循环（for/while）、异常处理（try-except）
- **Keywords**: if-else, loop, for, while, break, continue, try-except, conditional, iteration
- **Interface Points**: None (pure control structures, no external interface)

### function.py
- **Function**: 函数定义、参数传递、返回值、默认参数、装饰器、lambda
- **Keywords**: function, def, parameter, return, lambda, decorator, default-argument
- **Interface Points**:

```yaml
0xC1D2E3:
  type: variable
  role: 函数名
  direction: input
0xF4A5B6:
  type: variable
  role: 参数列表
  direction: input
0xB7C8D9:
  type: variable
  role: 返回值
  direction: output
```

### data_structure.py
- **Function**: 列表/字典/集合/元组操作、列表推导式、栈、队列
- **Keywords**: list, dict, set, tuple, stack, queue, comprehension, collection
- **Interface Points**:

```yaml
0xD1E2F3:
  type: variable
  role: 数据集合
  direction: input-output
0xA4B5C6:
  type: variable
  role: 元素
  direction: input
```

### string.py
- **Function**: 字符串格式化、分割合并、替换、正则匹配、编解码
- **Keywords**: string, format, split, join, replace, regex, substring, encode, decode
- **Interface Points**:

```yaml
0xE1F2A3:
  type: variable
  role: 原始字符串
  direction: input
0xB4C5D6:
  type: variable
  role: 处理结果
  direction: output
```

### console.py
- **Function**: 控制台输入输出、格式化打印、基础日志
- **Keywords**: input, print, prompt, stdout, stderr, logging, display
- **Interface Points**:

```yaml
0xF1A2B3:
  type: variable
  role: 提示文本
  direction: input
0xC4D5E6:
  type: variable
  role: 用户输入
  direction: output
```

---

## Python — Level 2: Algorithmic Patterns

### bubble_sort.py
- **Function**: 对列表进行升序排序（冒泡排序，原地排序，稳定）
- **Keywords**: bubble-sort, comparison-sort, in-place, stable, ordering
- **Interface Points**:

```yaml
0xA1B2C3:
  type: variable
  role: 待排序数组
  direction: input
0xD4E5F6:
  type: variable
  role: 排序结果数组
  direction: output
```

### greedy_algorithm.py
- **Function**: 贪心算法模式——活动选择（区间调度）、硬币找零
- **Keywords**: greedy, optimization, interval-scheduling, coin-change, activity-selection
- **Interface Points**:

```yaml
0xB1C2D3:
  type: variable
  role: 问题输入数据
  direction: input
0xE4F5A6:
  type: variable
  role: 贪心选择结果
  direction: output
```

### game_of_life.py
- **Function**: Conway 生命游戏——二维细胞自动机模拟
- **Keywords**: game-of-life, cellular-automaton, grid, simulation, Conway, 2D
- **Interface Points**:

```yaml
0xC1D2E3:
  type: variable
  role: 网格行数
  direction: input
0xF4A5B6:
  type: variable
  role: 网格列数
  direction: input
0xB7C8D9:
  type: variable
  role: 初始网格状态
  direction: input-output
```

### binary_search.py
- **Function**: 在有序列表中二分查找目标值
- **Keywords**: binary-search, divide-conquer, search, sorted-array, lookup, O(log-n)
- **Interface Points**:

```yaml
0xD1E2F3:
  type: variable
  role: 有序数组
  direction: input
0xA4B5C6:
  type: variable
  role: 目标值
  direction: input
0xC7D8E9:
  type: variable
  role: 匹配索引（-1 表示未找到）
  direction: output
```

### dfs_bfs.py
- **Function**: 图的深度优先和广度优先遍历、最短路径（BFS）
- **Keywords**: graph, dfs, bfs, traversal, depth-first, breadth-first, shortest-path, tree
- **Interface Points**:

```yaml
0xE1F2A3:
  type: variable
  role: 图的邻接表
  direction: input
0xB4C5D6:
  type: variable
  role: 起始节点
  direction: input
0xD7E8F9:
  type: variable
  role: 遍历结果
  direction: output
```

### fibonacci.py
- **Function**: 斐波那契数列——递归、动态规划（自底向上+记忆化）、生成器
- **Keywords**: fibonacci, recursion, dynamic-programming, memoization, generator, sequence
- **Interface Points**:

```yaml
0xF1A2B3:
  type: variable
  role: 数列项数
  direction: input
0xC4D5E6:
  type: variable
  role: 计算结果
  direction: output
```

---

## Python — Level 3: Architectural Patterns

### actor_system.py
- **Function**: Actor 系统——独立 Actor 通过消息邮箱异步通信
- **Keywords**: actor, message-passing, concurrency, mailbox, async, parallel
- **Interface Points**:

```yaml
0xA1B2C3:
  type: variable
  role: Actor 名称
  direction: input
0xD4E5F6:
  type: variable
  role: 消息内容
  direction: input
0xF7A8B9:
  type: variable
  role: 消息处理函数
  direction: input
0x112233:
  type: reference
  target: Level1/data_structure.py
  role: 消息队列（deque）
0x445566:
  type: reference
  target: Level1/function.py
  role: 处理器注册
```

### account_management.py
- **Function**: 用户账号管理——注册、登录验证、信息更新、删除、JSON持久化
- **Keywords**: account, authentication, login, register, CRUD, session, persistence
- **Interface Points**:

```yaml
0xB1C2D3:
  type: variable
  role: 用户名
  direction: input
0xE4F5A6:
  type: variable
  role: 密码
  direction: input
0xA7B8C9:
  type: variable
  role: 操作结果
  direction: output
0xD0E1F2:
  type: reference
  target: Level1/OS.py
  role: JSON 文件持久化
0x334455:
  type: reference
  target: Level1/data_structure.py
  role: 账号数据存储（dict）
```

### api_server.py
- **Function**: 基于 http.server 的基础 REST API 服务器——GET/POST 端点处理
- **Keywords**: server, REST, HTTP, request, response, endpoint, route, API
- **Interface Points**:

```yaml
0xC1D2E3:
  type: variable
  role: 服务器主机地址
  direction: input
0xF4A5B6:
  type: variable
  role: 服务器端口
  direction: input
0xB7C8D9:
  type: variable
  role: 数据库/数据源
  direction: input-output
0x566778:
  type: reference
  target: Level1/OS.py
  role: JSON 序列化响应
0x889900:
  type: reference
  target: Level1/data_structure.py
  role: 数据存储结构
```

---

## Expanding the Library

To add new code materials:

1. Place the source file in the appropriate `assets/code-library/<Language>/Level<N>/` directory
2. Identify interface points — mark ONLY external inputs/outputs with hex placeholders
   (leave internal implementation variables as normal identifiers)
3. Add an entry to the corresponding section of this Layerfile
4. Include a precise **Function** description and critical **Keywords**
5. List all interface points with type (variable/reference), role, and direction

For **reference** type interface points, specify the `target` path to the referenced material file.
The assembly process will recursively expand these references.
