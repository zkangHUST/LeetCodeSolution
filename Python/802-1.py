# 染色法
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        color = [0 for i in range(len(graph))]
        ans = []
        for i in range(len(graph)):
            if self.dfs(graph, color, i):
                ans.append(i)
        return ans

    def dfs(self, graph, color, i):
        if color[i] > 0:
            return color[i] == 2
        color[i] = 1
        for v in graph[i]:
            if color[v] == 2:
                continue
            if color[v] == 1:
                return False
            if not self.dfs(graph, color, v):
                return False
        color[i] = 2
        return True