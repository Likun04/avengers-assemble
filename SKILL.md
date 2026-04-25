---
name: avengers-assemble
description: >
  AI 程序员的代码拼装技能 — Avengers, Assemble!
  通过"伪代码 → 安全扫描 → 素材检索 → 原文摘抄"的方式产出代码，
  而非直接逐 token 生成代码。确保目标文件中的每一行代码都来自经过验证的素材库，
  消除语法错误（缺引号、少括号等）和局部语义错误。
  内置基于意图拓扑子图匹配的过程控制安全引擎，防止恶意社区素材注入。
  适用于：让 AI 写代码、构建程序、生成脚本、编写功能模块、开发中型工具性代码。
  触发词：写代码、编写程序、开发功能、构建模块、实现功能、写个脚本、code、implement、build。
---

# Avengers, Assemble!

## Overview

Transform code generation from "token-by-token guessing" into "reference-based assembly".

The code library is a collection of pre-verified code example files. It is NOT a package manager
or a set of black-box APIs — it is a **textbook of example sentences**. The Agent reads the examples,
understands the patterns, and copies the exact code snippets into the target file.

Code materials use **hex placeholders** only at **interface points** (inputs/outputs that need
external injection). Internal implementation variables remain as normal identifiers.
Hex placeholders are resolved during assembly by mapping them to business-meaningful names
derived from the business pseudocode.

Higher-level materials can **reference** lower-level materials via hex reference pointers,
enabling **recursive assembly** from Level 3 (architectural) down to Level 1 (atomic operations).

## Core Principles

1. **Copy, never generate**: Every line in the final output MUST come from the code library.
   The Agent assembles; it does not author.
2. **Hex only at interfaces**: Hex placeholders mark ONLY external interface points (input/output).
   Internal variables stay as-is — they are implementation details, not assembly concerns.
3. **References, not inlining**: Higher-level materials reference lower-level materials via
   hex reference pointers. Assembly recursively expands these references — no flat copy-paste.
4. **Business pseudocode drives naming**: Variable/function names in the final output are
   derived from business pseudocode semantics, not invented by the Agent.
5. **Safety first**: All community-sourced materials are scanned before assembly.
   The Agent performs semantic-level safety judgment that no static scanner can replicate.
6. **Step echo is non-negotiable**: Every step MUST be explicitly echoed with sequential labels.
   Skipping step labels = failed assembly. This is how the user knows the process ran correctly.

## 强制回显标号机制 (Mandatory Step Echo Mechanism)

### 设计初衷

Prompt 约束无法 100% 阻止 AI 直接生成代码（实测遵从率 ~70%）。
本机制采用**暴露式设计**：不让 AI "忍住"，而是让违规行为**无处藏身**。

当 AI 跳过步骤直接输出代码时，回显标号会断裂——
**人类审查者一眼就能看出流程没有完整执行**。

### 强制输出格式

每个 Step 的输出**必须**以以下格式包裹：

```
=== STEP X/6 | [步骤名称] | 状态：进行中 ===

（本步骤的实际内容）

=== STEP X/6 | 完成 ✓ ===
```

### 格式约束

1. **标号连续性**：STEP 1 → 2 → 3 → 4 → 5 → 6，不得跳跃
2. **状态标记**：每个 Step 必须有「状态：进行中」开头和「完成 ✓」结尾
3. **内容隔离**：Step 之间的内容必须被标号块隔离，不得连写
4. **伪代码纯文本约束**：Step 1 的输出中**不得出现任何代码语法字符**
   - 禁止：`{ } ( ) = ; < > [ ] function def class`
   - 允许：中文、英文、数字、标点、换行

### 违规检测（人类审查）

| 现象 | 判定 |
|------|------|
| 标号从 1 直接跳到 6 | AI 跳过了中间步骤 → 产物无效 |
| Step 1 内容出现 `{` 或 `function` | AI 在伪代码阶段直接写代码 → 产物无效 |
| 标号重复（两个 STEP 2） | AI 流程混乱 → 产物无效 |
| 缺少「完成 ✓」标记 | AI 未确认步骤完成 → 产物无效 |

### 对用户的意义

- **可审查**：标号断了 = 流程没走完 = 产物不可信
- **无需改 AI 架构**：纯 Prompt 层面实现
- **失败模式明确**：不是"为什么出错了"，而是"标号断了，步骤 X 被跳过了"

## Code Library Structure

```
assets/code-library/
  Python/
    Level1/              # Atomic operations — the alphabet
      calculator.py      # Arithmetic, assignment, type conversion
      OS.py              # File I/O, path operations
      control_flow.py    # Conditionals, loops, error handling
      function.py        # Function definitions, decorators
      data_structure.py  # List, dict, set, tuple operations
      string.py          # String manipulation, regex
      console.py         # Input/output, logging
    Level2/              # Algorithmic patterns — the grammar
      bubble_sort.py     # Comparison-based sorting
      greedy_algorithm.py# Optimization by local choice
      game_of_life.py    # Cellular automaton simulation
      binary_search.py   # Divide-and-conquer search
      dfs_bfs.py         # Graph traversal
      fibonacci.py       # Recursion and dynamic programming
    Level3/              # Architectural patterns — the prose
      actor_system.py    # Message-passing concurrency
      account_management.py  # User auth and CRUD
      api_server.py      # HTTP REST endpoint handler
  JavaScript/
    Level1/
    Level2/
    Level3/
```

### Granularity Levels

- **Level 1 (Atomic)**: Single-purpose basic operations. Any code decomposes to these.
- **Level 2 (Algorithmic)**: Complete algorithm implementations with proven correctness.
- **Level 3 (Architectural)**: Business-level component assemblies built from Level 1 + Level 2.

## Safety System

### Architecture: Process Control via Intent Topology Matching

The safety system does NOT scan the final assembled code (that's "product scanning").
Instead, it controls safety DURING assembly ("process control") by tracking the
**template call chain** and checking against **dangerous intent topologies**.

Two layers:

1. **Avengers.py** (`scripts/Avengers.py`) — Automated intent topology subgraph matcher.
   Maintains a call chain as templates are recursively assembled. For each template
   entering the chain, it checks whether the chain activates any dangerous intent
   topology from `references/red_list.yaml`. Detection via subgraph matching
   (connected path in the intent topology). Fast, deterministic, zero-dependency.

2. **Agent semantic judgment** — The AI Agent's understanding of code semantics.
   No static scanner can distinguish `os.system(user_input)` from `os.path.exists(path)`.
   The Agent provides the final safety verdict using semantic understanding.

### Red List (`references/red_list.yaml`) — Intent Topology Graph

Records **dangerous intent topologies**, not token co-occurrence weights.

Each entry models a dangerous INTENT — "what the malicious code wants to achieve":
- **Nodes**: Operational intents (e.g., "acquire external input", "execute as code")
- **Edges**: Data/control flow dependencies between intents
- **Templates**: Each node maps to code patterns that can realize it
- **Threshold**: Minimum connected nodes matched to trigger an alert

Structure:
```yaml
intents:
  - id: INT-001
    intent: dynamic_code_execution
    risk: CRITICAL
    topology:
      nodes:
        - id: acquire_external_input
          templates: ["input()", "sys.stdin", "argv"]
        - id: dynamic_construction
          templates: ["string_concat", "chr_build", "base64_decode"]
        - id: execute_as_code
          templates: ["eval()", "exec()", "FunctionType"]
      edges:
        - [acquire_external_input, dynamic_construction, "data_flow"]
        - [dynamic_construction, execute_as_code, "data_flow"]
      threshold: 2  # 2 connected nodes = minimum viable attack path
```

Key design decisions:
- **Intent-driven, not token-driven**: Models what the code *wants to do*, not surface tokens.
- **Weight-file style**: Sparse recording — only dangerous topologies, not all combinations.
- **Subgraph matching**: Single nodes are harmless; only connected paths trigger alerts.
- **Extensible**: New template → append to node's template list. New attack → add new intent.

### Safety Check Flow

| Finding | Action |
|---------|--------|
| No intent activated | PASS — proceed to assembly |
| Intent activated, risk=HIGH | WARNING — Agent reviews, may proceed |
| Intent activated, risk=CRITICAL | BLOCKED — Agent MUST make final verdict |

### Why Intent Topology Beats Token Scanning

- Token co-occurrence: `os` + `system` → false positive on `os.path.system`
- AST analysis: defeated by `getattr()` indirection, `chr()` obfuscation
- **Intent topology**: understands *what the code wants to do* and checks whether
  the call chain forms a dangerous operational path, regardless of code disguise

## Layerfile

The Layerfile (`references/layerfile.md`) is the index catalog for all code materials.
It records for each material file:

- **Source path**: Relative path to the file
- **Function**: What this material does (one-line business description)
- **Keywords**: Precise semantic anchors for search matching (few but critical)
- **Interface points**: Hex placeholders with type and role info:
  - `type: variable` — Replace with a business variable name during assembly
  - `type: reference` — Expand into another material file's code (recursive)

## Workflow

### Step 0: Identify Runtime Environment

**输出格式强制**：
```
=== STEP 0/6 | 识别运行环境 | 状态：进行中 ===

（本步骤内容）

=== STEP 0/6 | 完成 ✓ ===
```

Detect the target programming language, platform, available libraries, and version constraints.
This determines which subdirectory of the code library to search.
If the project has a project-level skill (`.workbuddy/skills/avengers-assemble/`), use it;
otherwise fall back to the user-level skill (`~/.workbuddy/skills/avengers-assemble/`).

Project-level skill inherits user-level base materials. Same-name files in project-level
override user-level. Project-level Layerfile is a full copy, independently maintained.

### Step 1: Write Business Pseudocode

**输出格式强制**：
```
=== STEP 1/6 | 业务伪代码 | 状态：进行中 ===

（本步骤内容，纯中文/英文描述，禁止任何代码语法字符）

=== STEP 1/6 | 完成 ✓ ===
```

⛔ **伪代码格式锁死**：
- 只允许：中文、英文、数字、标点（。，！？等）
- 禁止出现任何代码语法字符：`{ } ( ) = ; < > [ ] function def class =>`
- 每行必须以中文/英文动词开头
  - ✅ 正确：`"渲染公告列表，循环遍历 announcements 数组"`
  - ❌ 错误：`"for(let i=0; i<announcements.length; i++)"` ← 判定违规

Decompose the requirement into structured business-level pseudocode.
Pseudocode describes WHAT the system does, not HOW it is coded.
No variable names, no function signatures, no code details — only business entities and logic flow.

Example:
```
1. Receive username and password from user
2. Hash the password for secure storage comparison
3. Query user database for matching credentials
4. If match found, generate session token
5. Return login result (success with token, or failure message)
```

### Step 2: Search the Layerfile

**输出格式强制**：
```
=== STEP 2/6 | Layerfile匹配 | 状态：进行中 ===

（本步骤内容：匹配到的素材列表 + hex 关键点）

=== STEP 2/6 | 完成 ✓ ===
```

Read `references/layerfile.md`. Match each line of business pseudocode to materials
by scanning **function descriptions** and **keywords**. Use semantic understanding —
"排序" matches "bubble-sort", "查找" matches "binary-search".

Prioritize: first match Level 3 materials (most complete), fall back to Level 2, then Level 1.

Output format for matches:
```
| 业务需求 | 匹配素材 | 层级 | hex 关键点 |
|---------|---------|------|-----------|
| ...     | ...     | ...  | ...       |
```

### Step 2.5: Safety Gate (NON-OPTIONAL)

**输出格式强制**：
```
=== STEP 2.5/6 | 安全门 | 状态：进行中 ===

（本步骤内容：每个选中素材的意图拓扑检查结果）

=== STEP 2.5/6 | 完成 ✓ ===
```

For every material selected in Step 2:

1. **Run Avengers.py scan** (if available):
   ```
   python Avengers.py <material_path> --scan-only
   ```
2. **Interpret results**:
   - No intent activated → PASS, proceed to Step 3
   - Intent activated → READ the material code carefully
3. **Agent semantic judgment** (for any intent activation):
   - Read the material source code
   - Understand what each activated node *actually does* in context
   - `os.system(user_input)` → DANGEROUS (command injection: acquire_input → shell_exec)
   - `os.path.exists(filepath)` → SAFE (standard file check, no dangerous path)
   - `open(file, "w")` with hardcoded path → SAFE (material library file)
   - `open(user_input, "w")` → DANGEROUS (filesystem breach: path_traversal → file_write)
4. **Verdict**:
   - Material is semantically safe → proceed to Step 3
   - Material is semantically dangerous → REJECT, explain to user why
   - Agent is uncertain → WARN user, ask for confirmation

The Agent's semantic judgment is the FINAL authority. Avengers.py checks for
intent topology activation in the call chain; the Agent makes the decision.

Output format for safety gate:
```
| Intent ID | 意图 | 激活节点检查 | 判定 |
|-----------|-----|------------|------|
| ...       | ... | ...        | ✅ PASS / ❌ BLOCKED |
```

### Step 3: Read Materials and Identify Interface Points

**输出格式强制**：
```
=== STEP 3/6 | 读取素材+识别接口点 | 状态：进行中 ===

（本步骤内容：读取的素材片段 + 识别出的 hex 占位符列表）

=== STEP 3/6 | 完成 ✓ ===
```

For each matched material, open the source file in `assets/code-library/`.
Read the code. Note all hex placeholders found in the code — these are the interface points
that need to be resolved during assembly.

### Step 4: Build Hex-to-Business Mapping

**输出格式强制**：
```
=== STEP 4/6 | Hex→业务命名映射 | 状态：进行中 ===

（本步骤内容：映射表）

=== STEP 4/6 | 完成 ✓ ===
```

Derive variable/function names from business pseudocode semantics.
Map each hex interface point to a business-meaningful name.

Output format for mapping table:
```
| Hex 占位符 | 业务名称 | 来源素材 | 业务含义 |
|-----------|---------|---------|---------|
| ...       | ...     | ...     | ...     |
```

Example mapping:
```
0xA1B2C3 → username          (from pseudocode: "username")
0xD4E5F6 → password          (from pseudocode: "password")
0xF7A8B9 → login_result      (from pseudocode: "login result")
0x112233 → hash_password()   (from pseudocode: "hash the password")
0x445566 → query_user_db()   (from pseudocode: "query user database")
0x778899 → generate_token()  (from pseudocode: "generate session token")
```

### Step 5: Recursive Assembly

**输出格式强制**：
```
=== STEP 5/6 | 递归拼装 | 状态：进行中 ===

（本步骤内容：各组件的拼装描述，可含伪代码）

=== STEP 5/6 | 完成 ✓ ===
```

Starting from the top-level material:
1. For each `type: reference` interface point → open the referenced material file,
   recursively resolve ITS interface points (Steps 2.5-4), expand its code in place.
2. Continue until all references are expanded to Level 1 atomic operations.
3. For each `type: variable` interface point → replace hex with the mapped business name.
4. Copy the fully resolved code into the target file.

Assembly may produce either:
- **Modular output**: Keep materials as separate files with `import` references
- **Single-file output**: Fully expand all references into one file
Choose based on the project's conventions.

Avengers.py supports automated assembly:
```
# Single-layer: replace hex placeholders
python Avengers.py <material> --mapping 0xA1B2C3:name 0xD4E5F6:name2

# Recursive: expand references + safety scan all files
python Avengers.py <material> --mapping ... --recursive --library <path>
```

### Step 6: Validate

**输出格式强制**：
```
=== STEP 6/6 | 验证+拼装执行 | 状态：进行中 ===

（本步骤内容：验证结果 + 最终产物路径）

=== STEP 6/6 | 全部完成 ✓ ===
```

Run syntax validation on the assembled output (e.g., `python -m py_compile`).
If errors occur, resolve by selecting better-matching materials or adjusting assembly order.
NEVER fix errors by generating new code — only reassemble from library materials.

Also perform **post-assembly safety scan** on the final output:
- Re-scan the assembled file against `references/red_list.yaml`
- Verify no dangerous intent topologies are activated in the final code
- This is the "defense-in-depth" check after assembly

## Open Source & Distribution

### Public Repository (GitHub)

Community-contributed materials live in the public repo:
```
repo/
├── assets/code-library/     ← PR target (community contributions)
├── references/
│   ├── layerfile.md         ← community maintains index
│   └── red_list.yaml        ← intent topology graphs
├── CONTRIBUTING.md          ← contribution guidelines
└── .github/workflows/       ← optional CI pre-checks
```

### Skill Distribution Package

The Skill distributed to users contains private components:
```
avengers-assemble/
├── SKILL.md                 ← this file
├── scripts/
│   └── Avengers.py          ← assembly + safety engine (NOT in public repo)
├── assets/code-library/     ← synced from repo (定期拉取)
└── references/
    ├── layerfile.md
    └── red_list.yaml
```

**Key principle**: `scripts/Avengers.py` is a private asset. It ships only with the
Skill distribution package, never in the public repo. This ensures the safety engine
cannot be stripped or tampered with via PR.

## Constraints

1. **Zero generation**: Never write code from scratch. Always copy from the library.
2. **Verbatim logic**: When copying code, preserve the exact logic and structure.
   Only hex interface points are replaced; internal code stays untouched.
3. **Decomposition over generation**: If no material matches a requirement,
   decompose it further until Level 1 atoms suffice.
4. **Hex discipline**: Only mark interface points (input/output) with hex placeholders.
   Internal implementation variables remain as normal identifiers.
5. **Reference discipline**: Higher-level materials reference lower-level materials;
   do not flat-copy code between material files.
6. **Environment awareness**: Always respect the target runtime environment,
   available libraries, and project naming conventions.
7. **Safety discipline**: NEVER skip Step 2.5. Every material is scanned, every
   positive finding is semantically judged. No exceptions.
8. **Step echo discipline**: Every step MUST be wrapped with `=== STEP X/6 | ... ===` labels.
   Skipping labels, jumping steps, or omitting `完成 ✓` markers = failed assembly.
   This is the user's primary quality signal — if labels are broken, the output is invalid.
9. **Pseudocode purity**: Step 1 output MUST NOT contain any code syntax characters.
   `{ } ( ) = ; < > [ ] function def class` appearing in Step 1 = violation.
   This forces the Agent to think in business logic before touching code.
