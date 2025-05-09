from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reverse_graph = [[] for _ in range(n)]
        indegree = [0] * n

        # Build reversed graph and count indegree in one loop
        for u in range(n):
            for v in graph[u]:
                reverse_graph[v].append(u)
                indegree[u] += 1

        stack = [i for i in range(n) if indegree[i] == 0]
        safe = []

        while stack:
            node = stack.pop()
            safe.append(node)
            for neighbor in reverse_graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    stack.append(neighbor)

        return sorted(safe)
