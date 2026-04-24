<div align="center">

# Avengers, Assemble!

**AI 代码拼装技能 — 让每一行代码都有据可查**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Safety: Intent Topology](https://img.shields.io/badge/Safety-Intent%20Topology%20Engine-red.svg)](references/red_list.yaml)

*伪代码 → 安全扫描 → 素材检索 → 原文摘抄*

不猜代码，只抄代码。目标文件中的每一行都来自经过验证的素材库。

</div>

---

## 这是什么？

**Avengers, Assemble!** 是一个 AI 代码生成技能，它将传统 "逐 token 猜测生成代码" 的方式，替换为 **"基于素材库的引用式拼装"**。

核心思路：代码库不是包管理器，不是黑盒 API，而是**一本例句教科书**。AI 读懂例句，理解模式，然后把代码片段原样抄进目标文件。

### 为什么这么做？

| 传统生成 | 素材拼装 |
|---------|---------|
| 逐 token 生成，容易缺引号、少括号 | 原文摘抄，零语法错误 |
| 看着像对，跑起来可能语义偏差 | 每个素材预先验证，行为确定 |
| 难以溯源，出了 bug 不知道哪来的 | 每行代码可追溯到一个素材文件 |
| 安全性依赖 AI 的"自觉" | 内置意图拓扑安全引擎 |

## 快速理解

### 三层素材体系

```
Level 1 — 原子操作（字母表）
  calculator.py    # 算术、赋值、类型转换
  OS.py            # 文件 I/O、路径操作
  control_flow.py  # 条件、循环、异常处理
  function.py      # 函数定义、装饰器
  data_structure.py # 列表、字典、集合、元组
  string.py        # 字符串操作、正则
  console.py       # 输入输出、日志

Level 2 — 算法模式（语法）
  bubble_sort.py      # 比较排序
  greedy_algorithm.py # 贪心优化
  binary_search.py    # 分治查找
  dfs_bfs.py          # 图遍历
  fibonacci.py        # 递归与动态规划
  game_of_life.py     # 元胞自动机

Level 3 — 业务架构（作文）
  actor_system.py        # 消息传递并发
  account_management.py  # 用户认证与 CRUD
  api_server.py          # HTTP REST 端点
```

### 四条铁律

1. **只抄不写** — 最终输出的每一行必须来自代码库，AI 负责拼装，不负责创作
2. **Hex 只标接口** — 十六进制占位符只标记输入/输出接口，内部实现变量保持原样
3. **引用不拍平** — 高层素材通过引用指针指向低层素材，递归展开，不是简单复制粘贴
4. **成品无 Hex** — 拼装完成后，所有占位符替换为业务语义化命名

### Hex 占位符系统

素材文件用十六进制地址标记接口点，拼装时映射到业务变量名：

```python
# 素材原文 (bubble_sort.py)
def 0x3A7F1E(collection):
    for i in range(len(collection)):
        for j in range(len(collection) - i - 1):
            ...

# 拼装后 → hex 被替换为业务名
def sort_player_scores(player_scores):
    for i in range(len(player_scores)):
        for j in range(len(player_scores) - i - 1):
            ...
```

## 安全引擎

### 过程控制，而非产物扫描

传统安全方案扫描最终生成的代码——太晚了，代码已经写出来了。

Avengers 采用 **过程控制**：在拼装过程中实时追踪模板调用链，检查是否激活了危险的意图拓扑。

### 意图拓扑图（Intent Topology）

不记录 "哪些 token 同时出现很危险"，而是建模 **"恶意代码想达成什么目的"**：

```yaml
# 意图：命令注入
intents:
  - id: INT-002
    intent: command_injection
    risk: CRITICAL
    topology:
      nodes:
        - id: acquire_external_input      # 获取外部输入
          templates: ["input()", "argv", "environ"]
        - id: shell_execution              # 执行系统命令
          templates: ["os.system()", "subprocess"]
      edges:
        - [acquire_external_input, shell_execution, "direct_pipe"]
      threshold: 2  # 2 个连通节点 = 最小攻击路径
```

**单个节点无害** — `open()` 本身没问题，`os.environ` 也正常。
**连通路径才触发** — 只有当调用链形成 `获取外部输入 → 执行系统命令` 的完整路径时才报警。

### 8 个危险意图拓扑

| ID | 意图 | 风险 |
|----|------|------|
| INT-001 | 动态代码执行 | CRITICAL |
| INT-002 | 命令注入 | CRITICAL |
| INT-003 | 文件系统越权 | HIGH |
| INT-004 | 数据外泄 | HIGH |
| INT-005 | 持久化驻留 | HIGH |
| INT-006 | 环境篡改 | MEDIUM |
| INT-007 | 反序列化攻击 | HIGH |
| INT-008 | 混淆对抗 | MEDIUM |

### 检测流程

```
素材进入调用链
    ↓
TemplateProfiler: 代码 → 意图节点映射
    ↓
CallChainTracker: 新节点加入调用链
    ↓
BFS 连通性检查：调用链是否激活某意图拓扑的连通路径？
    ↓
├── 未激活 → PASS，继续拼装
├── 激活 HIGH → WARNING，Agent 语义审查
└── 激活 CRITICAL → BLOCKED，Agent 必须做出最终裁定
```

## 使用方式

### 命令行工具

```bash
# 单层拼装：替换 hex 占位符
python Avengers.py bubble_sort.py --mapping 0x3A7F1E:player_scores

# 递归拼装：展开所有引用 + 安全扫描
python Avengers.py api_server.py --mapping 0xA1B2C3:username 0xD4E5F6:password \
    --recursive --library assets/code-library/

# 仅安全扫描
python Avengers.py community_contribution.py --scan-only
```

### AI 技能调用

当用户说 "写代码"、"开发功能"、"实现 XXX" 时自动触发：

1. AI 将需求分解为业务伪代码
2. 在素材索引（layerfile）中匹配对应素材
3. 安全扫描每个素材
4. 读取素材源码，标注接口点
5. 递归拼装，替换占位符为业务命名
6. 语法验证输出

## 项目结构

```
avengers-assemble/
├── SKILL.md                          # 技能定义（AI 工作流）
├── scripts/
│   └── Avengers.py                   # 拼装引擎 + 安全引擎（私有组件）
├── assets/
│   └── code-library/
│       └── Python/
│           ├── Level1/               # 原子操作（7 个模块）
│           ├── Level2/               # 算法模式（6 个模块）
│           └── Level3/               # 业务架构（3 个模块）
└── references/
    ├── layerfile.md                  # 素材索引（功能描述 + 关键词 + 接口点）
    └── red_list.yaml                 # 意图拓扑图（8 个危险意图）
```

## 贡献

### 公开仓库

- 素材代码、索引、红名单拓扑在 GitHub 开放
- 社区可以 PR 贡献新素材
- 维护者负责审核拓扑安全映射

### 私有组件

- `scripts/Avengers.py` 是安全引擎核心，**不在公开仓库中**
- 随 Skill 分发包私有分发，防止被移除或篡改

## License

[MIT](LICENSE)

---

<div align="center">

*"Avengers, Assemble!" — 不是生成代码，是组装正义。*

</div>
