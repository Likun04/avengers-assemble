# Level 2: DFS & BFS
# Interface: 0xE1F2A3=input(图邻接表), 0xB4C5D6=input(起始节点), 0xD7E8F9=output(遍历结果)

from collections import deque

## DFS (Depth-First Search) — Recursive
def dfs_recursive(0xE1F2A3, 0xB4C5D6, visited=None):
    if visited is None:
        visited = set()
    visited.add(0xB4C5D6)
    0xD7E8F9 = visited
    for neighbor in 0xE1F2A3[0xB4C5D6]:
        if neighbor not in visited:
            dfs_recursive(0xE1F2A3, neighbor, visited)
    return 0xD7E8F9

## DFS — Iterative (Stack)
def dfs_iterative(0xE1F2A3, 0xB4C5D6):
    visited = set()
    stack = [0xB4C5D6]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in reversed(0xE1F2A3[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
    0xD7E8F9 = visited
    return 0xD7E8F9

## BFS (Breadth-First Search) — Queue
def bfs(0xE1F2A3, 0xB4C5D6):
    visited = set([0xB4C5D6])
    queue = deque([0xB4C5D6])
    while queue:
        node = queue.popleft()
        for neighbor in 0xE1F2A3[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    0xD7E8F9 = visited
    return 0xD7E8F9

## Shortest Path (BFS)
def shortest_path(0xE1F2A3, start, end):
    visited = {start}
    queue = deque([(start, [start])])
    while queue:
        node, path = queue.popleft()
        if node == end:
            return path
        for neighbor in 0xE1F2A3[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None
