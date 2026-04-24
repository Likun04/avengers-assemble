// Level 2: DFS & BFS
// Interface: 0xE1F2A3=input(图邻接表), 0xB4C5D6=input(起始节点), 0xD7E8F9=output(遍历结果)
// 意图：四种图遍历方式 — DFS递归、DFS迭代、BFS、最短路径

type Graph = Map<string | number, (string | number)[]>;

## DFS (Depth-First Search) — Recursive
function dfs_recursive(0xE1F2A3: Graph, 0xB4C5D6: string | number, visited: Set<string | number> = new Set()): Set<string | number> {
    visited.add(0xB4C5D6);
    const 0xD7E8F9: Set<string | number> = visited;
    for (const neighbor of (0xE1F2A3.get(0xB4C5D6) ?? [])) {
        if (!visited.has(neighbor)) {
            dfs_recursive(0xE1F2A3, neighbor, visited);
        }
    }
    return 0xD7E8F9;
}

## DFS — Iterative (Stack)
function dfs_iterative(0xE1F2A3: Graph, 0xB4C5D6: string | number): Set<string | number> {
    const visited: Set<string | number> = new Set();
    const stack: (string | number)[] = [0xB4C5D6];
    while (stack.length > 0) {
        const node = stack.pop()!;
        if (!visited.has(node)) {
            visited.add(node);
            for (const neighbor of ((0xE1F2A3.get(node) ?? []).slice().reverse())) {
                if (!visited.has(neighbor)) stack.push(neighbor);
            }
        }
    }
    const 0xD7E8F9: Set<string | number> = visited;
    return 0xD7E8F9;
}

## BFS (Breadth-First Search) — Queue
function bfs(0xE1F2A3: Graph, 0xB4C5D6: string | number): Set<string | number> {
    const visited: Set<string | number> = new Set([0xB4C5D6]);
    const queue: (string | number)[] = [0xB4C5D6];
    while (queue.length > 0) {
        const node = queue.shift()!;
        for (const neighbor of (0xE1F2A3.get(node) ?? [])) {
            if (!visited.has(neighbor)) {
                visited.add(neighbor);
                queue.push(neighbor);
            }
        }
    }
    const 0xD7E8F9: Set<string | number> = visited;
    return 0xD7E8F9;
}

## Shortest Path (BFS)
function shortest_path(0xE1F2A3: Graph, start: string | number, end: string | number): (string | number)[] | null {
    const visited: Set<string | number> = new Set([start]);
    const queue: [(string | number)[], (string | number)[]][] = [[start, [start]]];
    while (queue.length > 0) {
        const [node, path] = queue.shift()!;
        if (node === end) return path;
        for (const neighbor of (0xE1F2A3.get(node) ?? [])) {
            if (!visited.has(neighbor)) {
                visited.add(neighbor);
                queue.push([neighbor, [...path, neighbor]]);
            }
        }
    }
    return null;
}
