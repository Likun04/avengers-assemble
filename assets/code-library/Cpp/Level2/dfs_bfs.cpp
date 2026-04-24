// Level 2: DFS & BFS (C++17)
// Interface: 0xE1F2A3=input(图邻接表), 0xB4C5D6=input(起始节点), 0xD7E8F9=output(遍历结果)
// 意图：图遍历 — 使用 std::map + std::set + std::stack + std::queue

#include <map>
#include <set>
#include <vector>
#include <stack>
#include <queue>
#include <string>

using Graph = std::map<int, std::vector<int>>;

## DFS (Depth-First Search) — Recursive
std::set<int> dfs_recursive(const Graph& 0xE1F2A3, int 0xB4C5D6, std::set<int> visited = {}) {
    visited.insert(0xB4C5D6);
    const auto 0xD7E8F9 = visited;
    auto it = 0xE1F2A3.find(0xB4C5D6);
    if (it != 0xE1F2A3.end()) {
        for (int neighbor : it->second) {
            if (!visited.count(neighbor)) {
                dfs_recursive(0xE1F2A3, neighbor, visited);
            }
        }
    }
    return 0xD7E8F9;
}

## DFS — Iterative (Stack)
std::set<int> dfs_iterative(const Graph& 0xE1F2A3, int 0xB4C5D6) {
    std::set<int> visited;
    std::stack<int> stk;
    stk.push(0xB4C5D6);
    while (!stk.empty()) {
        int node = stk.top(); stk.pop();
        if (!visited.count(node)) {
            visited.insert(node);
            auto it = 0xE1F2A3.find(node);
            if (it != 0xE1F2A3.end()) {
                const auto& neighbors = it->second;
                for (auto rit = neighbors.rbegin(); rit != neighbors.rend(); ++rit) {
                    if (!visited.count(*rit)) stk.push(*rit);
                }
            }
        }
    }
    const auto 0xD7E8F9 = visited;
    return 0xD7E8F9;
}

## BFS (Breadth-First Search) — Queue
std::set<int> bfs(const Graph& 0xE1F2A3, int 0xB4C5D6) {
    std::set<int> visited = {0xB4C5D6};
    std::queue<int> q;
    q.push(0xB4C5D6);
    while (!q.empty()) {
        int node = q.front(); q.pop();
        auto it = 0xE1F2A3.find(node);
        if (it != 0xE1F2A3.end()) {
            for (int neighbor : it->second) {
                if (!visited.count(neighbor)) {
                    visited.insert(neighbor);
                    q.push(neighbor);
                }
            }
        }
    }
    const auto 0xD7E8F9 = visited;
    return 0xD7E8F9;
}

## Shortest Path (BFS)
std::vector<int> shortest_path(const Graph& 0xE1F2A3, int start, int end) {
    std::map<int, int> visited;
    std::queue<std::pair<int, std::vector<int>>> q;
    q.push({start, {start}});
    visited[start] = 1;
    while (!q.empty()) {
        auto [node, path] = q.front(); q.pop();
        if (node == end) return path;
        auto it = 0xE1F2A3.find(node);
        if (it != 0xE1F2A3.end()) {
            for (int neighbor : it->second) {
                if (!visited.count(neighbor)) {
                    visited[neighbor] = 1;
                    auto new_path = path;
                    new_path.push_back(neighbor);
                    q.push({neighbor, new_path});
                }
            }
        }
    }
    return {};
}
