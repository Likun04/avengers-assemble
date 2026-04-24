#!/usr/bin/env python3
"""
Avengers, Assemble! — Lego Coder Assembly & Safety Engine v2

Safety Architecture: Process Control via Intent Topology Matching
═══════════════════════════════════════════════════════════════

Instead of scanning the final assembled code for token co-occurrences
(a "product scan"), this engine performs safety checks DURING assembly
("process control"):

1. Maintains a CALL CHAIN as templates are recursively assembled
2. For each template entering the chain, checks if the chain activates
   any dangerous intent topology from red_list.yaml
3. Detection method: SUBGRAPH MATCHING — does the current call chain
   cover enough nodes of a dangerous topology to form a connected path?

The red_list.yaml records dangerous INTENT topologies:
- Nodes = operational intents (what the code wants to do)
- Edges = data/control flow dependencies between intents
- Each node maps to template patterns that can realize it
- Threshold = minimum nodes matched to trigger an alert

Assembly Engine:
- Replaces hex placeholders (type: variable) with business names
- Recursively expands reference pointers (type: reference)
- Scans every material BEFORE it enters the assembly chain

Usage:
  python Avengers.py <material_file> --mapping <hex:name>... [--recursive] [--library <path>]
  python Avengers.py <material_file> --scan-only
"""

import re
import sys
import os

HEX_PATTERN = re.compile(r'0x[0-9A-Fa-f]{6}')


# ═══════════════════════════════════════════════════════════
# YAML Parser — Indentation-based state machine for red_list.yaml v2
# ═══════════════════════════════════════════════════════════

def _parse_yaml_value(raw):
    """Parse a single YAML value string into a Python object."""
    raw = raw.strip()
    if not raw or raw == '~' or raw.lower() == 'null':
        return None
    if raw.lower() in ('true', 'yes'):
        return True
    if raw.lower() in ('false', 'no'):
        return False
    try:
        return int(raw)
    except ValueError:
        pass
    try:
        return float(raw)
    except ValueError:
        pass
    if (raw.startswith('"') and raw.endswith('"')) or \
       (raw.startswith("'") and raw.endswith("'")):
        return raw[1:-1]
    return raw


def _parse_inline_list(text):
    """Parse an inline YAML list like [a, b, c] into Python list."""
    text = text.strip()
    if not text.startswith('[') or not text.endswith(']'):
        return [_parse_yaml_value(text)]
    inner = text[1:-1].strip()
    if not inner:
        return []
    items = []
    # Split by comma, respecting quoted strings
    current = ''
    in_quote = None
    for ch in inner:
        if ch in ('"', "'") and in_quote is None:
            in_quote = ch
            current += ch
        elif ch == in_quote:
            in_quote = None
            current += ch
        elif ch == ',' and in_quote is None:
            item = current.strip()
            if item:
                items.append(_parse_yaml_value(item))
            current = ''
        else:
            current += ch
    item = current.strip()
    if item:
        items.append(_parse_yaml_value(item))
    return items


def _parse_edge_list(text):
    """Parse an edge entry like [a, b, 'relation'] into dict."""
    items = _parse_inline_list(text)
    if len(items) >= 3:
        return {'source': str(items[0]), 'target': str(items[1]), 'relation': str(items[2])}
    return None


def load_red_list(red_list_path):
    """Parse red_list.yaml v2 using indentation-based state machine.

    Expected structure:
      version: "2.0"
      intents:
        - id: INT-001        (indent 2)
          lang: python        (indent 4)
          topology:           (indent 4)
            nodes:            (indent 6)
              - id: xxx       (indent 8)
                desc: ...     (indent 10)
                templates: [...] (indent 10)
            edges:            (indent 6)
              - [a, b, c]     (indent 8)
            threshold: 2      (indent 6)
    """
    if not os.path.exists(red_list_path):
        return []

    with open(red_list_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    intents = []

    # State machine states
    S_TOP = 'top'           # Before intents: or inside top-level
    S_INTENT = 'intent'     # Inside an intent entry (indent 4 keys)
    S_TOPO = 'topo'        # Inside topology: (indent 6 keys)
    S_NODE = 'node'         # Inside a node entry (indent 10 keys)
    S_EDGES = 'edges'       # After edges: key, collecting edge items

    state = S_TOP
    current_intent = None
    current_node = None
    last_node_list_item_indent = 0

    for raw_line in lines:
        stripped = raw_line.rstrip()
        if not stripped or stripped.lstrip().startswith('#'):
            continue

        indent = len(stripped) - len(stripped.lstrip())
        content = stripped.lstrip()

        # ── State: TOP ──
        if state == S_TOP:
            if content.startswith('intents:'):
                state = S_INTENT
            elif content.startswith('version:'):
                pass  # We don't need version at runtime
            continue

        # ── State: INTENT (expecting indent 2 for -id:, indent 4 for keys) ──
        if state == S_INTENT:
            # New intent entry
            if indent == 2 and content.startswith('- ') and 'id:' in content:
                # Save previous intent
                if current_intent:
                    intents.append(current_intent)
                item = content[2:].strip()
                _, _, val = item.partition(':')
                current_intent = {
                    'id': _parse_yaml_value(val.strip()),
                    'nodes': [],
                    'edges': [],
                }
                continue

            # Intent-level properties (indent 4)
            if indent == 4 and current_intent is not None:
                key, _, val = content.partition(':')
                key = key.strip()
                val = val.strip()

                if key == 'topology':
                    state = S_TOPO
                    continue
                elif key in ('lang', 'intent', 'risk', 'desc'):
                    current_intent[key] = _parse_yaml_value(val)
                    continue
                elif key == 'threshold':
                    current_intent['threshold'] = _parse_yaml_value(val)
                    continue

            # Edges back at intent level (shouldn't happen but be safe)
            continue

        # ── State: TOPO (expecting indent 6 keys) ──
        if state == S_TOPO:
            if indent <= 4:
                # Exited topology section
                if content.startswith('- ') and 'id:' in content:
                    # New intent
                    if current_intent:
                        intents.append(current_intent)
                    item = content[2:].strip()
                    _, _, val = item.partition(':')
                    current_intent = {
                        'id': _parse_yaml_value(val.strip()),
                        'nodes': [],
                        'edges': [],
                    }
                    state = S_INTENT
                else:
                    state = S_INTENT
                continue

            key, _, val = content.partition(':')
            key = key.strip()
            val = val.strip()

            if key == 'nodes':
                state = S_NODE
                current_node = None
                continue
            elif key == 'edges':
                state = S_EDGES
                continue
            elif key == 'threshold':
                current_intent['threshold'] = _parse_yaml_value(val)
                continue

            continue

        # ── State: NODE (indent 8 for - id:, indent 10 for props) ──
        if state == S_NODE:
            # New node entry at indent 8
            if indent == 8 and content.startswith('- '):
                # Save previous node
                if current_node:
                    current_intent['nodes'].append(current_node)
                item = content[2:].strip()
                _, _, val = item.partition(':')
                current_node = {'id': _parse_yaml_value(val.strip())}
                last_node_list_item_indent = 10
                continue

            # Node properties at indent 10
            if indent == 10 and current_node is not None:
                key, _, val = content.partition(':')
                key = key.strip()
                val = val.strip()

                if key == 'desc':
                    current_node['desc'] = _parse_yaml_value(val)
                    continue
                elif key == 'templates':
                    if val.startswith('['):
                        current_node['templates'] = _parse_inline_list(val)
                    else:
                        # Multi-line templates - collect subsequent - items
                        templates = []
                        current_node['templates'] = templates
                        last_node_list_item_indent = indent
                    continue

            # Continuation list items for templates (indent 12+)
            if indent >= 12 and content.startswith('- ') and current_node is not None:
                item = content[2:].strip().strip('"').strip("'")
                current_node['templates'].append(item)
                continue

            # Back to indent 8 but not a list item → new node or section change
            if indent == 8 and not content.startswith('- '):
                # This is a section key (edges:, threshold:, nodes:)
                # Save current node first
                if current_node:
                    current_intent['nodes'].append(current_node)
                    current_node = None

                key, _, val = content.partition(':')
                key = key.strip()
                val = val.strip()

                if key == 'edges':
                    state = S_EDGES
                    continue
                elif key == 'threshold':
                    current_intent['threshold'] = _parse_yaml_value(val)
                    continue
                elif key == 'nodes':
                    continue  # Stay in S_NODE

            # Back to indent 6 → topology keys
            if indent == 6:
                if current_node:
                    current_intent['nodes'].append(current_node)
                    current_node = None
                key, _, val = content.partition(':')
                key = key.strip()
                val = val.strip()
                if key == 'edges':
                    state = S_EDGES
                elif key == 'threshold':
                    current_intent['threshold'] = _parse_yaml_value(val)
                elif key == 'nodes':
                    pass  # Stay in S_NODE
                continue

            # Back to indent 4 → intent keys
            if indent == 4:
                if current_node:
                    current_intent['nodes'].append(current_node)
                    current_node = None
                state = S_INTENT
                key, _, val = content.partition(':')
                key = key.strip()
                val = val.strip()
                if key in ('lang', 'intent', 'risk', 'desc'):
                    current_intent[key] = _parse_yaml_value(val)
                elif key == 'topology':
                    state = S_TOPO
                continue

            # Back to indent 2 → new intent
            if indent == 2 and content.startswith('- '):
                if current_node:
                    current_intent['nodes'].append(current_node)
                    current_node = None
                if current_intent:
                    intents.append(current_intent)
                item = content[2:].strip()
                _, _, val = item.partition(':')
                current_intent = {
                    'id': _parse_yaml_value(val.strip()),
                    'nodes': [],
                    'edges': [],
                }
                state = S_INTENT
                continue

            continue

        # ── State: EDGES (indent 8 for - [a, b, c]) ──
        if state == S_EDGES:
            if indent == 8 and content.startswith('- '):
                item = content[2:].strip()
                if item.startswith('['):
                    edge = _parse_edge_list(item)
                    if edge:
                        current_intent['edges'].append(edge)
                continue

            # Non-edge content at indent 8 → might be a new section
            if indent <= 6:
                if indent == 6:
                    key, _, val = content.partition(':')
                    key = key.strip()
                    val = val.strip()
                    if key == 'threshold':
                        current_intent['threshold'] = _parse_yaml_value(val)
                        continue
                    elif key == 'nodes':
                        state = S_NODE
                        current_node = None
                        continue
                    elif key == 'edges':
                        continue

                if indent == 4:
                    state = S_INTENT
                    key, _, val = content.partition(':')
                    key = key.strip()
                    val = val.strip()
                    if key in ('lang', 'intent', 'risk', 'desc'):
                        current_intent[key] = _parse_yaml_value(val)
                    elif key == 'topology':
                        state = S_TOPO
                    continue

                if indent == 2 and content.startswith('- '):
                    if current_intent:
                        intents.append(current_intent)
                    item = content[2:].strip()
                    _, _, val = item.partition(':')
                    current_intent = {
                        'id': _parse_yaml_value(val.strip()),
                        'nodes': [],
                        'edges': [],
                    }
                    state = S_INTENT
                    continue

            continue

    # Flush last intent
    if current_node and current_intent:
        current_intent['nodes'].append(current_node)
    if current_intent:
        intents.append(current_intent)

    return intents


# ═══════════════════════════════════════════════════════════
# Safety Engine — Intent Topology Subgraph Matching
# ═══════════════════════════════════════════════════════════

class TemplateProfiler:
    """Analyze a template file to determine which intent nodes it can realize.

    Instead of scanning for "dangerous tokens" in isolation, this profiler
    maps a template's code to operational intent nodes from the red list.
    The result is a set of (intent_id, node_id) pairs that this template
    can potentially activate.
    """

    # Map of code patterns → (intent_id, node_id) pairs
    # This is the bridge between "what code looks like" and "what it does"
    PATTERN_MAP = {
        # --- Dynamic Code Execution ---
        'eval':   [('INT-001', 'execute_as_code')],
        'exec':   [('INT-001', 'execute_as_code')],
        'compile': [('INT-001', 'dynamic_construction'), ('INT-001', 'execute_as_code')],
        'FunctionType': [('INT-001', 'execute_as_code')],
        'CodeType': [('INT-001', 'execute_as_code')],
        'getattr': [('INT-001', 'bypass_sandbox'), ('INT-008', 'dynamic_resolution')],
        '__builtins__': [('INT-001', 'bypass_sandbox')],
        '__import__': [('INT-001', 'bypass_sandbox'), ('INT-006', 'dynamic_import')],
        'importlib': [('INT-001', 'bypass_sandbox'), ('INT-006', 'dynamic_import')],
        '__class__': [('INT-001', 'bypass_sandbox'), ('INT-008', 'dynamic_resolution')],
        '__subclasses__': [('INT-001', 'bypass_sandbox'), ('INT-008', 'dynamic_resolution')],
        '__init__': [('INT-001', 'bypass_sandbox')],
        '__globals__': [('INT-001', 'bypass_sandbox')],
        'chr(': [('INT-001', 'dynamic_construction'), ('INT-008', 'string_obfuscation')],
        'base64': [('INT-001', 'dynamic_construction'), ('INT-004', 'data_serialization'),
                    ('INT-008', 'string_obfuscation')],
        'b64decode': [('INT-008', 'string_obfuscation')],
        'encode': [('INT-004', 'data_serialization'), ('INT-008', 'string_obfuscation')],
        'decode': [('INT-008', 'string_obfuscation')],
        'ctypes': [('INT-001', 'bypass_sandbox'), ('INT-005', 'process_injection')],
        'CDLL': [('INT-001', 'bypass_sandbox'), ('INT-005', 'process_injection')],

        # --- External Input ---
        'input(': [('INT-001', 'acquire_external_input'), ('INT-002', 'acquire_external_input'),
                    ('INT-003', 'acquire_external_input'), ('INT-007', 'acquire_untrusted_data')],
        'argv': [('INT-002', 'acquire_external_input'), ('INT-003', 'acquire_external_input')],
        'sys.stdin': [('INT-001', 'acquire_external_input')],
        'environ': [('INT-001', 'acquire_external_input'), ('INT-002', 'acquire_external_input'),
                     ('INT-003', 'acquire_external_input'), ('INT-004', 'data_collection'),
                     ('INT-006', 'env_poison')],
        'socket_recv': [('INT-001', 'acquire_external_input'), ('INT-004', 'network_outbound')],

        # --- Command Execution ---
        'os.system': [('INT-002', 'shell_execution')],
        'os.popen': [('INT-002', 'shell_execution')],
        'subprocess': [('INT-002', 'shell_execution'), ('INT-005', 'process_injection')],
        'Popen': [('INT-002', 'shell_execution'), ('INT-005', 'process_injection')],
        'shell=True': [('INT-002', 'shell_execution')],

        # --- Filesystem ---
        'open(': [('INT-003', 'file_write'), ('INT-003', 'file_read')],
        '"w"': [('INT-003', 'file_write')],
        "'w'": [('INT-003', 'file_write')],
        '"wb"': [('INT-003', 'file_write')],
        "'wb'": [('INT-003', 'file_write')],
        '"a"': [('INT-003', 'file_write')],
        "'a'": [('INT-003', 'file_write')],
        '"r"': [('INT-003', 'file_read')],
        "'r'": [('INT-003', 'file_read')],
        'shutil.rmtree': [('INT-003', 'file_delete'), ('INT-005', 'self_replication')],
        'shutil.move': [('INT-003', 'file_relocate')],
        'os.remove': [('INT-003', 'file_delete')],
        'os.unlink': [('INT-003', 'file_delete')],
        'os.rename': [('INT-003', 'file_relocate')],
        'os.replace': [('INT-003', 'file_relocate')],
        'os.symlink': [('INT-003', 'privilege_escalation')],
        'os.link': [('INT-003', 'privilege_escalation')],

        # --- Network ---
        'requests': [('INT-004', 'network_outbound')],
        'urllib': [('INT-004', 'network_outbound')],
        'urlopen': [('INT-004', 'network_outbound')],
        'socket.socket': [('INT-004', 'network_outbound')],
        'socket.connect': [('INT-004', 'network_outbound')],
        'http.client': [('INT-004', 'network_outbound')],
        'ftplib': [('INT-004', 'network_outbound')],
        'smtplib': [('INT-004', 'network_outbound')],

        # --- Serialization ---
        'pickle': [('INT-004', 'data_collection'), ('INT-007', 'deserialize')],
        'pickle.load': [('INT-007', 'deserialize')],
        'pickle.loads': [('INT-007', 'deserialize')],
        'marshal': [('INT-007', 'deserialize')],
        'marshal.loads': [('INT-007', 'deserialize')],
        'shelve': [('INT-007', 'deserialize')],
        'json.load': [('INT-004', 'data_collection')],
        'json.dumps': [('INT-004', 'data_serialization')],

        # --- Environment ---
        'sys.path.insert': [('INT-006', 'path_hijack')],
        'sys.path.append': [('INT-006', 'path_hijack')],
        'PYTHONPATH': [('INT-006', 'path_hijack')],

        # --- Concurrency abuse ---
        'multiprocessing': [('INT-005', 'process_injection')],
        'threading': [('INT-005', 'process_injection')],
    }

    def profile(self, code):
        """Analyze code and return set of (intent_id, node_id) it activates."""
        activated = set()

        for pattern, node_mappings in self.PATTERN_MAP.items():
            if pattern in code:
                for intent_id, node_id in node_mappings:
                    activated.add((intent_id, node_id))

        return activated


class CallChainTracker:
    """Tracks the assembly call chain and performs subgraph matching
    against dangerous intent topologies.

    The call chain is a list of (material_path, activated_nodes) entries.
    Each entry records which intent nodes that material can realize.
    """

    def __init__(self, intents, profiler=None):
        """
        Args:
            intents: List of intent topology dicts from red_list.yaml
            profiler: TemplateProfiler instance (creates default if None)
        """
        self.intents = intents
        self.profiler = profiler or TemplateProfiler()
        self.chain = []  # List of (material_name, activated_nodes_set)

    def push(self, material_path, code):
        """Add a material to the call chain and check for topology activation.

        Returns:
            (is_safe, findings, message)
            - is_safe: False if any intent topology is activated beyond threshold
            - findings: list of { intent_id, risk, matched_nodes, matched_edges }
            - message: human-readable report
        """
        activated = self.profiler.profile(code)
        material_name = os.path.basename(material_path)
        self.chain.append((material_name, activated))

        return self._check_topologies(material_name, activated)

    def pop(self):
        """Remove the last material from the call chain (for backtracking)."""
        if self.chain:
            self.chain.pop()

    def _check_topologies(self, new_material_name, new_activated):
        """Check if the current chain activates any dangerous topology."""
        if not self.intents:
            return True, [], "[PASS] No intent topologies loaded"

        # Aggregate all activated nodes across the entire chain
        chain_activated = set()
        for _, nodes in self.chain:
            chain_activated.update(nodes)

        findings = []
        is_safe = True

        for intent in self.intents:
            intent_id = intent.get('id', 'UNKNOWN')
            risk = intent.get('risk', 'HIGH')
            threshold = intent.get('threshold', 2)

            # Collect nodes and edges for this intent
            intent_nodes = intent.get('nodes', [])
            intent_edges = intent.get('edges', [])

            # Find which intent nodes are activated by the chain
            matched_node_ids = set()
            matched_node_details = []
            for node in intent_nodes:
                node_id = node.get('id', '')
                if (intent_id, node_id) in chain_activated:
                    matched_node_ids.add(node_id)
                    matched_node_details.append({
                        'id': node_id,
                        'desc': node.get('desc', ''),
                    })

            # Check threshold
            if len(matched_node_ids) < threshold:
                continue

            # Check if matched nodes form a connected subgraph via edges
            connected = self._check_connectivity(matched_node_ids, intent_edges)

            if connected:
                # Build edge details for matched path
                matched_edges = [
                    e for e in intent_edges
                    if e['source'] in matched_node_ids and e['target'] in matched_node_ids
                ]

                findings.append({
                    'intent_id': intent_id,
                    'risk': risk,
                    'intent_desc': intent.get('desc', ''),
                    'matched_nodes': matched_node_details,
                    'matched_edges': matched_edges,
                    'threshold': threshold,
                    'activation_count': len(matched_node_ids),
                    'chain_depth': len(self.chain),
                    'latest_material': new_material_name,
                })

                if risk == 'CRITICAL':
                    is_safe = False

        if not findings:
            return True, [], f"[PASS] {new_material_name} — no dangerous intent activated"

        # Build report
        msg_lines = []
        for f in findings:
            marker = "[BLOCKED]" if f['risk'] == 'CRITICAL' else "[WARNING]"
            msg_lines.append(f"{marker} Intent {f['intent_id']}: {f['intent_desc']}")
            msg_lines.append(f"  Activated {f['activation_count']}/{f['threshold']} nodes "
                           f"across {f['chain_depth']} chain levels")
            msg_lines.append(f"  Latest material: {f['latest_material']}")
            for node in f['matched_nodes']:
                msg_lines.append(f"    ● {node['id']}: {node['desc']}")
            for edge in f['matched_edges']:
                msg_lines.append(f"    → {edge['source']} --({edge['relation']})--> {edge['target']}")

        message = '\n'.join(msg_lines)
        return is_safe, findings, message

    def _check_connectivity(self, matched_nodes, edges):
        """Check if matched nodes form a connected subgraph through edges.

        Uses BFS: starting from any matched node, check if all other
        matched nodes are reachable via edges between matched nodes.
        """
        if len(matched_nodes) <= 1:
            return len(matched_nodes) >= 1

        # Build adjacency among matched nodes only
        adj = {n: set() for n in matched_nodes}
        for edge in edges:
            src, tgt = edge['source'], edge['target']
            if src in matched_nodes and tgt in matched_nodes:
                adj[src].add(tgt)
                adj[tgt].add(src)

        # BFS from first matched node
        start = next(iter(matched_nodes))
        visited = set()
        queue = [start]
        visited.add(start)

        while queue:
            current = queue.pop(0)
            for neighbor in adj[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return visited == matched_nodes


class SafetyEngine:
    """High-level safety engine that orchestrates scanning.

    Provides two interfaces:
    1. scan_material() — standalone scan of a single material (legacy/scan-only mode)
    2. CallChainTracker — process-control mode during assembly
    """

    def __init__(self, red_list_path=None, lang='python'):
        self.lang = lang
        self.intents = []
        if red_list_path:
            self.intents = load_red_list(red_list_path)
        self.profiler = TemplateProfiler()

    def scan_material(self, material_path):
        """Scan a single material file and return safety verdict.

        This is a simplified check: profile the material's code and
        check if it alone activates any dangerous intent topology.

        For full assembly-time safety, use CallChainTracker instead.
        """
        with open(material_path, 'r', encoding='utf-8') as f:
            code = f.read()

        if not self.intents:
            return True, 0, [], "[WARN] No intent topologies loaded — safety check skipped"

        # Create a temporary single-element chain for scanning
        tracker = CallChainTracker(self.intents, self.profiler)
        is_safe, findings, message = tracker.push(material_path, code)

        # Calculate a simple score for backward compatibility
        score = sum(
            (1.0 if f['risk'] == 'CRITICAL' else 0.5) * f['activation_count']
            for f in findings
        )

        return is_safe, score, findings, message

    def create_tracker(self):
        """Create a CallChainTracker for assembly-time process control."""
        return CallChainTracker(self.intents, self.profiler)


# ═══════════════════════════════════════════════════════════
# Assembly Engine — Hex Replacement & Recursive Expansion
# ═══════════════════════════════════════════════════════════

def read_mapping(args):
    """Parse --mapping arguments into a dict: hex_code -> business_name."""
    mapping = {}
    for item in args:
        if ':' not in item:
            print(f"Warning: skipping invalid mapping (no colon): {item}", file=sys.stderr)
            continue
        hex_code, name = item.split(':', 1)
        mapping[hex_code.strip()] = name.strip()
    return mapping


def read_layerfile(layerfile_path):
    """Extract interface point definitions from a Layerfile.

    Supports two formats:
    1. Markdown table rows: | 0xA1B2C3 | variable | input(param) | description |
    2. Legacy YAML-style: 0xA1B2C3: type: variable, role: input(param)

    Returns a dict: hex_code -> { type, role, description? }
    """
    if not os.path.exists(layerfile_path):
        return {}

    with open(layerfile_path, 'r', encoding='utf-8') as f:
        content = f.read()

    points = {}

    # ── Format 1: Markdown table rows ──
    # Match lines like: | 0xA1B2C3  | variable | input           | description |
    table_rows = re.findall(
        r'\|\s*(0x[0-9A-Fa-f]{6})\s*\|\s*(\w+)\s*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|',
        content
    )
    for hex_code, htype, role, desc in table_rows:
        points[hex_code] = {
            'type': htype.strip(),
            'role': role.strip(),
            'description': desc.strip(),
        }

    # ── Format 2: Legacy YAML-style blocks ──
    if not points:
        hex_blocks = re.findall(
            r'(0x[0-9A-Fa-f]{6}):\s*\n((?:  .+\n)*)',
            content
        )
        for hex_code, block in hex_blocks:
            info = {}
            type_match = re.search(r'type:\s*(\w+)', block)
            if type_match:
                info['type'] = type_match.group(1)
            role_match = re.search(r'role:\s*(.+)', block)
            if role_match:
                info['role'] = role_match.group(1).strip()
            points[hex_code] = info

    return points


def parse_cross_file_reference(ref_string):
    """Parse a cross-file reference like 'OS.py.0xB1C4B3' into (filename, hex_code).

    Returns:
        (filename, hex_code) if valid cross-file reference
        (None, hex_code) if it's a plain hex code
        (None, None) if invalid
    """
    # Pattern: something.py.0xHEXCODE or just 0xHEXCODE
    match = re.match(r'^([A-Za-z_]\w*\.py)\.(0x[0-9A-Fa-f]{6})$', ref_string.strip())
    if match:
        return match.group(1), match.group(2)

    # Plain hex code
    if re.match(r'^0x[0-9A-Fa-f]{6}$', ref_string.strip()):
        return None, ref_string.strip()

    return None, None


def resolve_cross_file_reference(target_file, target_hex, library_path, layerfile_path):
    """Resolve a cross-file reference by reading the target material's code.

    Args:
        target_file: Filename like 'OS.py'
        target_hex: Hex code like '0xB1C4B3'
        library_path: Root of code library
        layerfile_path: Path to layerfile.md

    Returns:
        The relevant code snippet from the target material, or an error comment.
    """
    # Search for the target file across the library
    for root, dirs, files in os.walk(library_path):
        if target_file in files:
            target_path = os.path.join(root, target_file)
            with open(target_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract lines containing the target hex code (including surrounding context)
            lines = content.split('\n')
            snippet_lines = []
            for line in lines:
                if target_hex in line:
                    snippet_lines.append(line)

            if snippet_lines:
                return '\n'.join(snippet_lines)
            else:
                return f"# [hex {target_hex} not found in {target_file}]"

    return f"# [file {target_file} not found in library]"


def replace_placeholders(code, mapping):
    """Replace all hex placeholders in code with their mapped business names."""
    def replacer(match):
        hex_code = match.group(0)
        if hex_code in mapping:
            return mapping[hex_code]
        return hex_code

    return HEX_PATTERN.sub(replacer, code)


def find_references(layerfile_points):
    """Return list of hex codes that are type=reference."""
    return [
        hex_code for hex_code, info in layerfile_points.items()
        if info.get('type') == 'reference'
    ]


def find_cross_file_references(material_path):
    """Scan a material file for cross-file reference annotations.

    Looks for patterns like: # → 0xD0E1F2: description  or  → file.py.0xHEX
    Also checks comment blocks at the top for References: section.

    Returns list of (source_hex, target_file, target_hex) tuples.
    """
    if not os.path.exists(material_path):
        return []

    with open(material_path, 'r', encoding='utf-8') as f:
        content = f.read()

    refs = []

    # Match inline reference annotations: → OS.py.0xB1C4B3 or → 0xD0E1F2
    # Patterns: "→" followed by optional filename.hex or just hex
    ref_patterns = re.findall(r'→\s*([A-Za-z_]\w*\.py\.)?(0x[0-9A-Fa-f]{6})', content)
    for filename_part, hex_code in ref_patterns:
        if filename_part:
            target_file = filename_part.rstrip('.')
            refs.append((None, target_file, hex_code))
        else:
            refs.append((None, None, hex_code))

    # Match References: section in header comments
    refs_section = re.search(r'#\s*References:(.+?)(?=\n#|\n\n|\Z)', content, re.DOTALL)
    if refs_section:
        refs_text = refs_section.group(1)
        # Match: 0x112233→file.py.0xHEX(description)
        header_refs = re.findall(
            r'(0x[0-9A-Fa-f]{6})\s*→\s*([A-Za-z_]\w*\.py)\.(0x[0-9A-Fa-f]{6})',
            refs_text
        )
        for src_hex, target_file, target_hex in header_refs:
            refs.append((src_hex, target_file, target_hex))

    return refs


def assemble_recursive(material_path, mapping, library_path, layerfile_path,
                       tracker, visited=None, depth=0):
    """Recursively assemble a material, performing process-control safety checks.

    Supports two types of references:
    1. Layerfile references (type=reference): hex → expand target material code
    2. Cross-file references (→ file.py.0xHEX): inline annotations linking to
       specific hex interface points in other material files

    Args:
        material_path: Path to the material file
        mapping: hex -> business name mapping
        library_path: Root of the code library
        layerfile_path: Path to layerfile.md
        tracker: CallChainTracker instance for safety checks
        visited: Set of already-visited material paths (circular ref protection)
        depth: Current recursion depth (for indentation)
    """
    if visited is None:
        visited = set()

    abs_material = os.path.abspath(material_path)
    if abs_material in visited:
        return "# [circular reference avoided: {}]".format(os.path.basename(material_path))
    visited.add(abs_material)

    # Read material code
    with open(material_path, 'r', encoding='utf-8') as f:
        code = f.read()

    # ── Process Control Safety Check (non-optional) ──
    # Push this material onto the call chain and check topologies
    is_safe, findings, scan_msg = tracker.push(material_path, code)
    print("{}{}".format("  " * depth + "[SAFETY] " if depth else "[SAFETY] ", scan_msg),
          file=sys.stderr)

    if not is_safe:
        print("\n[FATAL] Assembly aborted — material '{}' activated dangerous intent topology."
              .format(os.path.basename(material_path)), file=sys.stderr)
        tracker.pop()
        sys.exit(1)

    # ── Resolve cross-file references (→ file.py.0xHEX annotations) ──
    cross_refs = find_cross_file_references(material_path)
    for src_hex, target_file, target_hex in cross_refs:
        if not target_file or not target_hex:
            continue
        snippet = resolve_cross_file_reference(
            target_file, target_hex, library_path, layerfile_path
        )
        # Replace the annotation comment with the actual code
        annotation = f"→ {target_file}.{target_hex}"
        # Replace both forms: with and without source hex prefix
        if src_hex:
            annotation = f"{src_hex}: {annotation}"
        # Find the line containing the annotation and replace the comment
        lines = code.split('\n')
        new_lines = []
        for line in lines:
            if annotation in line:
                # Replace the comment with the actual code snippet
                indent = len(line) - len(line.lstrip())
                prefix = ' ' * indent
                for snippet_line in snippet.split('\n'):
                    new_lines.append(prefix + snippet_line)
            else:
                new_lines.append(line)
        code = '\n'.join(new_lines)

    # ── Resolve layerfile references (type=reference) ──
    layerfile_points = read_layerfile(layerfile_path)
    references = find_references(layerfile_points)

    for hex_code in references:
        ref_info = layerfile_points.get(hex_code, {})
        target = ref_info.get('target', '')
        if not target:
            continue

        target_path = os.path.join(library_path, target)
        if not os.path.exists(target_path):
            code = code.replace(hex_code, "# [unresolved reference: {}]".format(target))
            continue

        # Recursively expand the referenced material
        expanded = assemble_recursive(
            target_path, mapping, library_path, layerfile_path,
            tracker, visited, depth + 1
        )
        indented = '\n'.join('    ' + line for line in expanded.split('\n'))
        code = code.replace(hex_code, indented)

    # ── Replace variable placeholders ──
    code = replace_placeholders(code, mapping)

    # Pop this material from chain (assembly complete for this subtree)
    tracker.pop()

    return code


# ═══════════════════════════════════════════════════════════
# Path Detection Utilities
# ═══════════════════════════════════════════════════════════

def find_layerfile(material_path):
    """Search upward from material to find layerfile.md."""
    search_dir = os.path.dirname(os.path.abspath(material_path))
    while search_dir != os.path.dirname(search_dir):
        candidate = os.path.join(search_dir, '..', 'references', 'layerfile.md')
        if os.path.exists(candidate):
            return candidate
        candidate = os.path.join(search_dir, 'layerfile.md')
        if os.path.exists(candidate):
            return candidate
        search_dir = os.path.dirname(search_dir)
    return None


def find_library(material_path):
    """Search upward from material to find the code library root."""
    material_dir = os.path.dirname(os.path.abspath(material_path))
    check = material_dir
    while check != os.path.dirname(check):
        if any(os.path.isdir(os.path.join(check, l)) for l in ['Level1', 'Level2', 'Level3']):
            return check
        check = os.path.dirname(check)
    return None


def find_red_list(material_path):
    """Search upward from material to find red_list.yaml."""
    search_dir = os.path.dirname(os.path.abspath(material_path))
    while search_dir != os.path.dirname(search_dir):
        candidate = os.path.join(search_dir, '..', 'references', 'red_list.yaml')
        if os.path.exists(candidate):
            return candidate
        candidate = os.path.join(search_dir, 'red_list.yaml')
        if os.path.exists(candidate):
            return candidate
        search_dir = os.path.dirname(search_dir)
    return None


# ═══════════════════════════════════════════════════════════
# Entry Point
# ═══════════════════════════════════════════════════════════

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Avengers, Assemble! — Lego Coder Assembly & Safety Engine v2'
    )
    parser.add_argument('material', help='Path to the material file to assemble')
    parser.add_argument('--mapping', nargs='+', default=[],
                        help='Hex-to-name mappings: 0xA1B2C3:business_name')
    parser.add_argument('--recursive', action='store_true',
                        help='Recursively expand reference pointers')
    parser.add_argument('--library', default=None,
                        help='Path to the code library root (e.g., assets/code-library/Python/)')
    parser.add_argument('--layerfile', default=None,
                        help='Path to the Layerfile')
    parser.add_argument('--red-list', default=None,
                        help='Path to the Red List (red_list.yaml)')
    parser.add_argument('--lang', default='python',
                        help='Target language for safety scanning (default: python)')
    parser.add_argument('--output', default=None,
                        help='Output file path (default: stdout)')
    parser.add_argument('--scan-only', action='store_true',
                        help='Only scan for safety, do not assemble')

    args = parser.parse_args()

    if not os.path.exists(args.material):
        print("Error: material file not found: {}".format(args.material), file=sys.stderr)
        sys.exit(1)

    # Auto-detect paths
    layerfile_path = args.layerfile or find_layerfile(args.material)
    red_list_path = args.red_list or find_red_list(args.material)

    if not red_list_path:
        print("[WARN] No Red List found. Running without safety checks.", file=sys.stderr)

    # ── Scan-only mode ──
    if args.scan_only:
        engine = SafetyEngine(red_list_path, args.lang)
        is_safe, score, findings, msg = engine.scan_material(args.material)
        print(msg)
        if findings:
            print("\nDetailed findings:")
            for f in findings:
                marker = "[CRITICAL]" if f['risk'] == 'CRITICAL' else "[WARNING]"
                print("  {} {}: {}".format(marker, f['intent_id'], f['intent_desc']))
                for node in f['matched_nodes']:
                    print("      Node: {} — {}".format(node['id'], node['desc']))
                for edge in f.get('matched_edges', []):
                    print("      Edge: {} --({})--> {}".format(edge['source'], edge['relation'], edge['target']))
        sys.exit(0 if is_safe else 1)

    # ── Assembly mode ──
    mapping = read_mapping(args.mapping)
    engine = SafetyEngine(red_list_path, args.lang)

    if args.recursive:
        library_path = args.library or find_library(args.material)
        if not library_path:
            print("Error: --library path required for recursive assembly", file=sys.stderr)
            sys.exit(1)

        tracker = engine.create_tracker()
        result = assemble_recursive(
            args.material, mapping, library_path, layerfile_path, tracker
        )
    else:
        # Non-recursive: still scan the single material
        is_safe, score, findings, scan_msg = engine.scan_material(args.material)
        print(scan_msg, file=sys.stderr)
        if not is_safe:
            print("\n[FATAL] Assembly aborted — material failed safety scan.", file=sys.stderr)
            sys.exit(1)

        with open(args.material, 'r', encoding='utf-8') as f:
            code = f.read()
        result = replace_placeholders(code, mapping)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(result)
        print("Assembled output written to: {}".format(args.output))
    else:
        print(result)


if __name__ == '__main__':
    main()
