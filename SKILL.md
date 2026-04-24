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

Detect the target programming language, platform, available libraries, and version constraints.
This determines which subdirectory of the code library to search.
If the project has a project-level skill (`.workbuddy/skills/avengers-assemble/`), use it;
otherwise fall back to the user-level skill (`~/.workbuddy/skills/avengers-assemble/`).

Project-level skill inherits user-level base materials. Same-name files in project-level
override user-level. Project-level Layerfile is a full copy, independently maintained.

### Step 1: Write Business Pseudocode

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

Read `references/layerfile.md`. Match each line of business pseudocode to materials
by scanning **function descriptions** and **keywords**. Use semantic understanding —
"排序" matches "bubble-sort", "查找" matches "binary-search".

Prioritize: first match Level 3 materials (most complete), fall back to Level 2, then Level 1.

### Step 2.5: Safety Gate (NON-OPTIONAL)

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

### Step 3: Read Materials and Identify Interface Points

For each matched material, open the source file in `assets/code-library/`.
Read the code. Note all hex placeholders found in the code — these are the interface points
that need to be resolved during assembly.

### Step 4: Build Hex-to-Business Mapping

Derive variable/function names from business pseudocode semantics.
Map each hex interface point to a business-meaningful name.

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

Run syntax validation on the assembled output (e.g., `python -m py_compile`).
If errors occur, resolve by selecting better-matching materials or adjusting assembly order.
NEVER fix errors by generating new code — only reassemble from library materials.

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
